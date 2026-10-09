package com.shopflow.backend.repository;

import com.shopflow.common.model.Category;

import java.util.Map;
import java.util.Optional;

/**
 * Store for {@link Category} entities.
 */
public class CategoryRepository extends InMemoryRepository<Category> {

    public CategoryRepository() {
        super("cat");
    }

    @Override
    public String getName() {
        return "categories";
    }

    @Override
    public Category fromJson(Map<String, Object> map) {
        return Category.fromJson(map);
    }

    public Optional<Category> findByName(String name) {
        if (name == null) {
            return Optional.empty();
        }
        return findFirst(category -> name.trim().equalsIgnoreCase(category.getName()));
    }

    public boolean nameTakenByOther(String name, String excludeId) {
        return findByName(name)
                .map(found -> !found.getId().equals(excludeId))
                .orElse(false);
    }

    public String nameOf(String categoryId) {
        return findById(categoryId).map(Category::getName).orElse("Uncategorized");
    }
}
