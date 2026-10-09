package com.shopflow.common.model;

import java.util.LinkedHashMap;
import java.util.Map;

/**
 * A sellable product with a price and a stock level.
 */
public class Product implements Identifiable {

    public static final int LOW_STOCK_THRESHOLD = 5;

    private String id;
    private String name;
    private String sku;
    private String categoryId;
    private String description;
    private double price;
    private int stock;

    public Product() {
    }

    public Product(String id, String name, String sku, String categoryId,
                   String description, double price, int stock) {
        this.id = id;
        this.name = name;
        this.sku = sku;
        this.categoryId = categoryId;
        this.description = description;
        this.price = price;
        this.stock = stock;
    }

    @Override
    public String getId() {
        return id;
    }

    @Override
    public void setId(String id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getSku() {
        return sku;
    }

    public void setSku(String sku) {
        this.sku = sku;
    }

    public String getCategoryId() {
        return categoryId;
    }

    public void setCategoryId(String categoryId) {
        this.categoryId = categoryId;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public int getStock() {
        return stock;
    }

    public void setStock(int stock) {
        this.stock = stock;
    }

    public boolean isLowStock() {
        return stock <= LOW_STOCK_THRESHOLD;
    }

    @Override
    public Map<String, Object> toJson() {
        Map<String, Object> map = new LinkedHashMap<>();
        map.put("id", id);
        map.put("name", name);
        map.put("sku", sku);
        map.put("categoryId", categoryId);
        map.put("description", description);
        map.put("price", price);
        map.put("stock", stock);
        return map;
    }

    public static Product fromJson(Map<String, Object> map) {
        Product product = new Product();
        product.id = Identifiable.idOrNull(Identifiable.str(map, "id"));
        product.name = Identifiable.str(map, "name");
        product.sku = Identifiable.str(map, "sku");
        product.categoryId = Identifiable.str(map, "categoryId");
        product.description = Identifiable.str(map, "description");
        product.price = Identifiable.dbl(map, "price");
        product.stock = Identifiable.integer(map, "stock");
        return product;
    }

    @Override
    public String toString() {
        return name + " (" + sku + ")";
    }
}
