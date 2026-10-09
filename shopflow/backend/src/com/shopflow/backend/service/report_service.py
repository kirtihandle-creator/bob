"""
report_service.py

NOTE: This is the ONE backend file written in Python inside an otherwise
pure-Java backend. It is intentionally inconsistent with the rest of the
project: the Java build (javac) ignores it, no Java class calls it, and it
cannot be loaded by the JVM. It exists only to demonstrate a mixed-language
backend file that does NOT belong in this codebase.

It mirrors what a Java ReportService would do: read the JSON files that the
Java backend persists under data/ and compute dashboard statistics.

Run standalone:  python report_service.py ../../../../../../data
"""

import json
import os
import sys
from collections import defaultdict
from datetime import datetime

LOW_STOCK_THRESHOLD = 5
CANCELLED = "CANCELLED"


def load(data_dir, name):
    """Load one repository file (products.json, orders.json, ...)."""
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
    data_dir = argv[1] if len(argv) > 1 else "data"
    report = build_report(data_dir)
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
