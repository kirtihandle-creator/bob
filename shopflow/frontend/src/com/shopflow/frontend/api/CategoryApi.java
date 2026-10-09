package com.shopflow.frontend.api;

import com.shopflow.common.json.Json;
import com.shopflow.common.model.Category;
import com.shopflow.common.model.Identifiable;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

/**
 * Calls under /api/categories. The list response also carries a
 * {@code productCount} per category which is exposed via {@link Row}.
 */
public class CategoryApi {

    /** A category plus how many products use it. */
    public record Row(Category category, int productCount) {
    }

    private final ApiClient client;

    public CategoryApi(ApiClient client) {
        this.client = client;
    }

    public List<Row> listRows() {
        List<Row> rows = new ArrayList<>();
        for (Map<String, Object> map : Json.mapList(client.getItems("/api/categories"), m -> m)) {
            rows.add(new Row(Category.fromJson(map), Identifiable.integer(map, "productCount")));
        }
        return rows;
    }

    public List<Category> list() {
        List<Category> categories = new ArrayList<>();
        for (Row row : listRows()) {
            categories.add(row.category());
        }
        return categories;
    }

    public Category get(String id) {
        return Category.fromJson(client.getObject("/api/categories/" + id));
    }

    public Category create(Category category) {
        return Category.fromJson(client.post("/api/categories", category.toJson()));
    }

    public Category update(Category category) {
        return Category.fromJson(client.put("/api/categories/" + category.getId(), category.toJson()));
    }

    public void delete(String id) {
        client.delete("/api/categories/" + id);
    }
}
