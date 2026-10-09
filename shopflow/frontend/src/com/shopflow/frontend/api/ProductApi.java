package com.shopflow.frontend.api;

import com.shopflow.common.json.Json;
import com.shopflow.common.model.Identifiable;
import com.shopflow.common.model.Product;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

/**
 * Calls under /api/products. List responses are enriched by the backend
 * with the category name, which is carried in {@link Row}.
 */
public class ProductApi {

    /** A product plus its resolved category name. */
    public record Row(Product product, String categoryName) {
    }

    private final ApiClient client;

    public ProductApi(ApiClient client) {
        this.client = client;
    }

    public List<Row> list(String search, String categoryId, boolean lowStockOnly) {
        String query = ApiClient.query(
                "q", search,
                "category", categoryId,
                "lowStock", lowStockOnly ? "true" : "",
                "limit", 500);
        List<Row> rows = new ArrayList<>();
        for (Map<String, Object> map : Json.mapList(client.getItems("/api/products" + query), m -> m)) {
            rows.add(toRow(map));
        }
        return rows;
    }

    public List<Product> listAll() {
        List<Product> products = new ArrayList<>();
        for (Row row : list("", "", false)) {
            products.add(row.product());
        }
        return products;
    }

    public Row get(String id) {
        return toRow(client.getObject("/api/products/" + id));
    }

    public Row create(Product product) {
        return toRow(client.post("/api/products", product.toJson()));
    }

    public Row update(Product product) {
        return toRow(client.put("/api/products/" + product.getId(), product.toJson()));
    }

    public Row adjustStock(String id, int delta) {
        return toRow(client.post("/api/products/" + id + "/stock", Json.map("delta", delta)));
    }

    public void delete(String id) {
        client.delete("/api/products/" + id);
    }

    private static Row toRow(Map<String, Object> map) {
        return new Row(Product.fromJson(map), Identifiable.str(map, "categoryName"));
    }
}
