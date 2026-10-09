package com.shopflow.backend.service;

import com.shopflow.backend.repository.OrderRepository;
import com.shopflow.backend.server.ApiException;
import com.shopflow.common.json.Json;
import com.shopflow.common.model.Customer;
import com.shopflow.common.model.Identifiable;
import com.shopflow.common.model.Order;
import com.shopflow.common.model.OrderItem;
import com.shopflow.common.model.OrderStatus;
import com.shopflow.common.model.Product;

import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/**
 * Business rules for orders: stock is reserved when an order is created,
 * released when it is cancelled, and status changes must follow the
 * transitions defined on {@link OrderStatus}.
 */
public class OrderService {

    private final OrderRepository orders;
    private final ProductService productService;
    private final CustomerService customerService;

    public OrderService(OrderRepository orders, ProductService productService, CustomerService customerService) {
        this.orders = orders;
        this.productService = productService;
        this.customerService = customerService;
    }

    public List<Order> list(String status, String customerId) {
        if (customerId != null && !customerId.isBlank()) {
            return orders.findByCustomer(customerId);
        }
        if (status != null && !status.isBlank()) {
            return orders.findByStatus(OrderStatus.parse(status));
        }
        return orders.findAll();
    }

    public Order get(String id) {
        return orders.findById(id).orElseThrow(() -> ApiException.notFound("Order", id));
    }

    /**
     * Creates an order from a body like
     * {@code {"customerId": "...", "notes": "...", "items": [{"productId": "...", "quantity": 2}]}}.
     * Stock is checked for every line before any stock is deducted.
     */
    public synchronized Order create(Map<String, Object> body) {
        Customer customer = customerService.get(Identifiable.str(body, "customerId"));
        List<Object> rawItems = Json.nestedList(body, "items");
        if (rawItems.isEmpty()) {
            throw ApiException.badRequest("An order needs at least one item");
        }
        Order order = new Order();
        order.setCustomerId(customer.getId());
        order.setCustomerName(customer.getName());
        order.setNotes(Identifiable.str(body, "notes"));
        // Merge lines that repeat the same product so the stock check sees the combined quantity.
        Map<String, Integer> quantities = new LinkedHashMap<>();
        for (Map<String, Object> raw : Json.mapList(rawItems, map -> map)) {
            String productId = Identifiable.str(raw, "productId");
            int quantity = Identifiable.integer(raw, "quantity");
            if (quantity <= 0) {
                throw ApiException.badRequest("Quantity must be positive for "
                        + productService.get(productId).getName());
            }
            try {
                quantities.merge(productId, quantity, Math::addExact);
            } catch (ArithmeticException overflow) {
                throw ApiException.badRequest("Combined quantity for product " + productId + " is too large");
            }
        }
        // Check-and-deduct happens atomically inside the product service lock.
        List<Product> reserved = productService.reserveStock(quantities);
        for (Product product : reserved) {
            order.addItem(OrderItem.of(product, quantities.get(product.getId())));
        }
        try {
            return orders.save(order);
        } catch (RuntimeException e) {
            productService.releaseStock(quantities);
            throw e;
        }
    }

    public synchronized Order changeStatus(String id, String rawStatus) {
        Order order = get(id);
        OrderStatus target = OrderStatus.parse(rawStatus);
        if (order.getStatus() == target) {
            return order;
        }
        if (!order.getStatus().canTransitionTo(target)) {
            throw ApiException.conflict("Cannot move order from " + order.getStatus() + " to " + target);
        }
        if (target == OrderStatus.CANCELLED) {
            releaseStock(order);
        }
        order.setStatus(target);
        return orders.save(order);
    }

    public synchronized void delete(String id) {
        Order order = get(id);
        if (order.getStatus().isOpen()) {
            releaseStock(order);
        }
        orders.delete(id);
    }

    private void releaseStock(Order order) {
        Map<String, Integer> quantities = new LinkedHashMap<>();
        for (OrderItem item : order.getItems()) {
            quantities.merge(item.getProductId(), item.getQuantity(), Integer::sum);
        }
        productService.releaseStock(quantities);
    }
}
