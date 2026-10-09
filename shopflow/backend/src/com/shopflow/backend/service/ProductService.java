package com.shopflow.backend.service;

import com.shopflow.backend.repository.CategoryRepository;
import com.shopflow.backend.repository.OrderRepository;
import com.shopflow.backend.repository.ProductRepository;
import com.shopflow.backend.server.ApiException;
import com.shopflow.common.model.Product;
import com.shopflow.common.util.Money;
import com.shopflow.common.util.Validation;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

/**
 * Business rules for products: unique SKU, valid category, non-negative
 * price and stock, and protection against deleting products that open
 * orders still reference.
 */
public class ProductService {

    private final ProductRepository products;
    private final CategoryRepository categories;
    private final OrderRepository orders;

    public ProductService(ProductRepository products, CategoryRepository categories, OrderRepository orders) {
        this.products = products;
        this.categories = categories;
        this.orders = orders;
    }

    public List<Product> list(String search, String categoryId, boolean lowStockOnly) {
        List<Product> result = products.search(search);
        if (categoryId != null && !categoryId.isBlank()) {
            result.removeIf(product -> !categoryId.equals(product.getCategoryId()));
        }
        if (lowStockOnly) {
            result.removeIf(product -> !product.isLowStock());
        }
        return result;
    }

    public Product get(String id) {
        return products.findById(id).orElseThrow(() -> ApiException.notFound("Product", id));
    }

    public Product create(Map<String, Object> body) {
        Product product = Product.fromJson(body);
        product.setId(null);
        product.setSku(normalizeSku(product.getSku()));
        product.setPrice(Money.round(product.getPrice()));
        validate(product);
        return products.save(product);
    }

    public Product update(String id, Map<String, Object> body) {
        Product existing = get(id);
        Product incoming = Product.fromJson(body);
        incoming.setId(id);
        incoming.setSku(normalizeSku(incoming.getSku()));
        incoming.setPrice(Money.round(incoming.getPrice()));
        validate(incoming);
        existing.setName(incoming.getName());
        existing.setSku(incoming.getSku());
        existing.setCategoryId(incoming.getCategoryId());
        existing.setDescription(incoming.getDescription());
        existing.setPrice(incoming.getPrice());
        existing.setStock(incoming.getStock());
        return products.save(existing);
    }

    public synchronized Product adjustStock(String id, int delta) {
        Product product = get(id);
        int newStock = product.getStock() + delta;
        if (newStock < 0) {
            throw ApiException.conflict("Insufficient stock for " + product.getName()
                    + ": have " + product.getStock() + ", need " + (-delta));
        }
        product.setStock(newStock);
        return products.save(product);
    }

    /**
     * Atomically reserves stock for several products. Every quantity is
     * checked before any product is changed, and all changes happen under
     * the same lock as {@link #adjustStock}, so a concurrent manual
     * adjustment can never interleave with an order's reservation.
     *
     * @return the products in the same order as the map, with updated stock
     */
    public synchronized List<Product> reserveStock(Map<String, Integer> quantities) {
        List<Product> resolved = new ArrayList<>();
        for (Map.Entry<String, Integer> entry : quantities.entrySet()) {
            Product product = get(entry.getKey());
            int quantity = entry.getValue();
            if (product.getStock() < quantity) {
                throw ApiException.conflict("Insufficient stock for " + product.getName()
                        + ": have " + product.getStock() + ", need " + quantity);
            }
            resolved.add(product);
        }
        List<Product> updated = new ArrayList<>();
        for (Product product : resolved) {
            int quantity = quantities.get(product.getId());
            product.setStock(product.getStock() - quantity);
            try {
                updated.add(products.save(product));
            } catch (RuntimeException e) {
                product.setStock(product.getStock() + quantity);
                for (Product done : updated) {
                    done.setStock(done.getStock() + quantities.get(done.getId()));
                    products.save(done);
                }
                throw e;
            }
        }
        return updated;
    }

    /** Returns reserved stock, ignoring products that no longer exist. */
    public synchronized void releaseStock(Map<String, Integer> quantities) {
        for (Map.Entry<String, Integer> entry : quantities.entrySet()) {
            products.findById(entry.getKey()).ifPresent(product -> {
                product.setStock(product.getStock() + entry.getValue());
                products.save(product);
            });
        }
    }

    public void delete(String id) {
        get(id);
        if (orders.referencesProduct(id)) {
            throw ApiException.conflict("Product is part of an open order and cannot be deleted");
        }
        products.delete(id);
    }

    public Map<String, Object> enrich(Product product) {
        Map<String, Object> json = product.toJson();
        json.put("categoryName", categories.nameOf(product.getCategoryId()));
        json.put("lowStock", product.isLowStock());
        return json;
    }

    private static String normalizeSku(String sku) {
        return sku == null ? null : sku.trim().toUpperCase();
    }

    private void validate(Product product) {
        Validation.begin()
                .require(product.getName(), "Name")
                .maxLength(product.getName(), 80, "Name")
                .require(product.getSku(), "SKU")
                .sku(product.getSku(), "SKU")
                .require(product.getCategoryId(), "Category")
                .check(categories.exists(product.getCategoryId()), "Category does not exist")
                .nonNegative(product.getPrice(), "Price")
                .nonNegative(product.getStock(), "Stock")
                .check(!products.skuTakenByOther(product.getSku(), product.getId()),
                        "SKU " + product.getSku() + " is already in use")
                .throwIfInvalid();
    }
}
