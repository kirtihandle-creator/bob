package com.shopflow.backend.repository;

import com.shopflow.common.model.Product;

import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.Optional;

/**
 * Store for {@link Product} entities with lookups by SKU, category and
 * free-text search.
 */
public class ProductRepository extends InMemoryRepository<Product> {

    public ProductRepository() {
        super("prd");
    }

    @Override
    public String getName() {
        return "products";
    }

    @Override
    public Product fromJson(Map<String, Object> map) {
        return Product.fromJson(map);
    }

    public Optional<Product> findBySku(String sku) {
        if (sku == null) {
            return Optional.empty();
        }
        return findFirst(product -> sku.equalsIgnoreCase(product.getSku()));
    }

    public List<Product> findByCategory(String categoryId) {
        return findWhere(product -> categoryId != null && categoryId.equals(product.getCategoryId()));
    }

    public List<Product> findLowStock() {
        return findWhere(Product::isLowStock);
    }

    /** Case-insensitive match on name, SKU or description. */
    public List<Product> search(String term) {
        if (term == null || term.isBlank()) {
            return findAll();
        }
        String needle = term.toLowerCase(Locale.ROOT);
        return findWhere(product ->
                contains(product.getName(), needle)
                        || contains(product.getSku(), needle)
                        || contains(product.getDescription(), needle));
    }

    public boolean skuTakenByOther(String sku, String excludeId) {
        return findBySku(sku)
                .map(found -> !found.getId().equals(excludeId))
                .orElse(false);
    }

    public double totalInventoryValue() {
        return findAll().stream()
                .mapToDouble(product -> product.getPrice() * product.getStock())
                .sum();
    }

    private static boolean contains(String haystack, String needle) {
        return haystack != null && haystack.toLowerCase(Locale.ROOT).contains(needle);
    }
}
