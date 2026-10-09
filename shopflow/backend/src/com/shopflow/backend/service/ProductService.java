package com.shopflow.backend.service;

import com.shopflow.backend.repository.CategoryRepository;
import com.shopflow.backend.repository.OrderRepository;
import com.shopflow.backend.repository.ProductRepository;
import com.shopflow.backend.server.ApiException;
import com.shopflow.common.model.Product;
import com.shopflow.common.util.Money;
import com.shopflow.common.util.Validation;

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
        product.setSku(product.getSku().trim().toUpperCase());
        product.setPrice(Money.round(product.getPrice()));
        validate(product);
        return products.save(product);
    }

    public Product update(String id, Map<String, Object> body) {
        Product existing = get(id);
        Product incoming = Product.fromJson(body);
        incoming.setId(id);
        incoming.setSku(incoming.getSku().trim().toUpperCase());
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

    public Product adjustStock(String id, int delta) {
        Product product = get(id);
        int newStock = product.getStock() + delta;
        if (newStock < 0) {
            throw ApiException.conflict("Insufficient stock for " + product.getName()
                    + ": have " + product.getStock() + ", need " + (-delta));
        }
        product.setStock(newStock);
        return products.save(product);
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
