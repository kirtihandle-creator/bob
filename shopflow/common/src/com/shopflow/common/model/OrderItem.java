package com.shopflow.common.model;

import java.util.LinkedHashMap;
import java.util.Map;

/**
 * A single line on an order: a product, how many, and the unit price
 * at the moment the order was placed. The price is copied so that later
 * product price changes do not rewrite history.
 */
public class OrderItem {

    private String productId;
    private String productName;
    private int quantity;
    private double unitPrice;

    public OrderItem() {
    }

    public OrderItem(String productId, String productName, int quantity, double unitPrice) {
        this.productId = productId;
        this.productName = productName;
        this.quantity = quantity;
        this.unitPrice = unitPrice;
    }

    public static OrderItem of(Product product, int quantity) {
        return new OrderItem(product.getId(), product.getName(), quantity, product.getPrice());
    }

    public String getProductId() {
        return productId;
    }

    public void setProductId(String productId) {
        this.productId = productId;
    }

    public String getProductName() {
        return productName;
    }

    public void setProductName(String productName) {
        this.productName = productName;
    }

    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    public double getUnitPrice() {
        return unitPrice;
    }

    public void setUnitPrice(double unitPrice) {
        this.unitPrice = unitPrice;
    }

    public double getLineTotal() {
        return quantity * unitPrice;
    }

    public Map<String, Object> toJson() {
        Map<String, Object> map = new LinkedHashMap<>();
        map.put("productId", productId);
        map.put("productName", productName);
        map.put("quantity", quantity);
        map.put("unitPrice", unitPrice);
        map.put("lineTotal", getLineTotal());
        return map;
    }

    public static OrderItem fromJson(Map<String, Object> map) {
        OrderItem item = new OrderItem();
        item.productId = Identifiable.str(map, "productId");
        item.productName = Identifiable.str(map, "productName");
        item.quantity = Identifiable.integer(map, "quantity");
        item.unitPrice = Identifiable.dbl(map, "unitPrice");
        return item;
    }

    @Override
    public String toString() {
        return quantity + " x " + productName;
    }
}
