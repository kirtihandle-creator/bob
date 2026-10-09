"""
report_service.py

The ONE backend file written in Python inside an otherwise pure-Java
backend. It is NOT standalone: the Java class
com.shopflow.backend.service.ReportService launches this script with the
Python interpreter every time a client requests /api/reports/summary or
/api/reports/low-stock, and the Swing dashboard renders whatever this
script prints. If Python is missing, or this file is moved, the Java
backend answers 503 and the dashboard shows an error.

Contract with Java:
  argv[1]  -> data directory containing products.json, customers.json,
              orders.json written by com.shopflow.backend.persistence.FileStore
  stdout   -> one JSON object (the report)
  exit 0   -> success; any other exit code is reported as HTTP 502
"""

import json
import os
import sys
from collections import defaultdict
from datetime import datetime

LOW_STOCK_THRESHOLD = 5   # must match Product.LOW_STOCK_THRESHOLD in Java
CANCELLED = "CANCELLED"   # must match OrderStatus.CANCELLED in Java


def load(data_dir, name):
    """Load one repository file written by the Java FileStore."""
    path = os.path.join(data_dir, name + ".json")
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def order_total(order):
    return sum(item.get("quantity", 0) * item.get("unitPrice", 0.0)
               for item in order.get("items", []))


def revenue(orders):
    return round(sum(order_total(o) for o in orders if o.get("status") != CANCELLED), 2)


def status_breakdown(orders):
    counts = defaultdict(int)
    for order in orders:
        counts[order.get("status", "NEW")] += 1
    return dict(counts)


def low_stock(products):
    return [p for p in products if p.get("stock", 0) <= LOW_STOCK_THRESHOLD]


def inventory_value(products):
    return round(sum(p.get("price", 0.0) * p.get("stock", 0) for p in products), 2)


def top_products(orders, limit=5):
    sold = defaultdict(int)
    for order in orders:
        if order.get("status") == CANCELLED:
            continue
        for item in order.get("items", []):
            sold[item.get("productName", "?")] += item.get("quantity", 0)
    ranked = sorted(sold.items(), key=lambda pair: pair[1], reverse=True)
    return [{"product": name, "quantity": qty} for name, qty in ranked[:limit]]


def daily_revenue(orders, days=7):
    buckets = defaultdict(float)
    for order in orders:
        if order.get("status") == CANCELLED:
            continue
        day = datetime.fromtimestamp(order.get("createdAt", 0) / 1000).strftime("%Y-%m-%d")
        buckets[day] += order_total(order)
    recent = sorted(buckets.items())[-days:]
    return [{"date": day, "revenue": round(amount, 2)} for day, amount in recent]


def build_report(data_dir):
    products = load(data_dir, "products")
    customers = load(data_dir, "customers")
    orders = load(data_dir, "orders")
    return {
        "productCount": len(products),
        "customerCount": len(customers),
        "orderCount": len(orders),
        "revenue": revenue(orders),
        "inventoryValue": inventory_value(products),
        "lowStock": low_stock(products),
        "statusBreakdown": status_breakdown(orders),
        "topProducts": top_products(orders),
        "dailyRevenue": daily_revenue(orders),
    }


def main(argv):
    if len(argv) < 2:
        sys.stderr.write("usage: report_service.py <data-dir>\n")
        return 2
    data_dir = argv[1]
    if not os.path.isdir(data_dir):
        sys.stderr.write("data directory not found: %s\n" % data_dir)
        return 3
    print(json.dumps(build_report(data_dir)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
