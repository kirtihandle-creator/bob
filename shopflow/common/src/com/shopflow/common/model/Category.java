package com.shopflow.common.model;

import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Objects;

/**
 * A product category such as "Electronics" or "Books".
 */
public class Category implements Identifiable {

    private String id;
    private String name;
    private String description;

    public Category() {
    }

    public Category(String id, String name, String description) {
        this.id = id;
        this.name = name;
        this.description = description;
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

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    @Override
    public Map<String, Object> toJson() {
        Map<String, Object> map = new LinkedHashMap<>();
        map.put("id", id);
        map.put("name", name);
        map.put("description", description);
        return map;
    }

    public static Category fromJson(Map<String, Object> map) {
        Category category = new Category();
        category.id = Identifiable.idOrNull(Identifiable.str(map, "id"));
        category.name = Identifiable.str(map, "name");
        category.description = Identifiable.str(map, "description");
        return category;
    }

    @Override
    public boolean equals(Object other) {
        if (this == other) {
            return true;
        }
        if (!(other instanceof Category that)) {
            return false;
        }
        return Objects.equals(id, that.id);
    }

    @Override
    public int hashCode() {
        return Objects.hashCode(id);
    }

    @Override
    public String toString() {
        return name == null ? "" : name;
    }
}
