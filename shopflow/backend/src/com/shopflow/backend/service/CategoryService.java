package com.shopflow.backend.service;

import com.shopflow.backend.repository.CategoryRepository;
import com.shopflow.backend.repository.ProductRepository;
import com.shopflow.backend.server.ApiException;
import com.shopflow.common.model.Category;
import com.shopflow.common.util.Validation;

import java.util.List;
import java.util.Map;

/**
 * Business rules for categories: unique names and no deletion while
 * products still reference the category.
 */
public class CategoryService {

    private final CategoryRepository categories;
    private final ProductRepository products;

    public CategoryService(CategoryRepository categories, ProductRepository products) {
        this.categories = categories;
        this.products = products;
    }

    public List<Category> list() {
        return categories.findAll();
    }

    public Category get(String id) {
        return categories.findById(id).orElseThrow(() -> ApiException.notFound("Category", id));
    }

    public Category create(Map<String, Object> body) {
        Category category = Category.fromJson(body);
        category.setId(null);
        validate(category);
        return categories.save(category);
    }

    public Category update(String id, Map<String, Object> body) {
        Category existing = get(id);
        Category incoming = Category.fromJson(body);
        incoming.setId(id);
        validate(incoming);
        existing.setName(incoming.getName());
        existing.setDescription(incoming.getDescription());
        return categories.save(existing);
    }

    public void delete(String id) {
        get(id);
        int inUse = products.findByCategory(id).size();
        if (inUse > 0) {
            throw ApiException.conflict("Category is used by " + inUse + " product(s)");
        }
        categories.delete(id);
    }

    public Map<String, Object> withProductCount(Category category) {
        Map<String, Object> json = category.toJson();
        json.put("productCount", products.findByCategory(category.getId()).size());
        return json;
    }

    private void validate(Category category) {
        Validation.begin()
                .require(category.getName(), "Name")
                .maxLength(category.getName(), 60, "Name")
                .maxLength(category.getDescription(), 250, "Description")
                .check(!categories.nameTakenByOther(category.getName(), category.getId()),
                        "A category with that name already exists")
                .throwIfInvalid();
    }
}
