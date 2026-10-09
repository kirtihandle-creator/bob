package com.shopflow.backend.repository;

import com.shopflow.common.model.Order;
import com.shopflow.common.model.OrderStatus;

import java.util.Comparator;
import java.util.List;
import java.util.Map;

/**
 * Store for {@link Order} entities. Orders are returned newest first.
 */
public class OrderRepository extends InMemoryRepository<Order> {

    private static final Comparator<Order> NEWEST_FIRST =
            Comparator.comparingLong(Order::getCreatedAt).reversed();

    public OrderRepository() {
        super("ord");
    }

    @Override
    public String getName() {
        return "orders";
    }

    @Override
    public Order fromJson(Map<String, Object> map) {
        return Order.fromJson(map);
    }

    @Override
    public List<Order> findAll() {
        List<Order> orders = super.findAll();
        orders.sort(NEWEST_FIRST);
        return orders;
    }

    public List<Order> findByCustomer(String customerId) {
        List<Order> orders = findWhere(order -> customerId != null && customerId.equals(order.getCustomerId()));
        orders.sort(NEWEST_FIRST);
        return orders;
    }

    public List<Order> findByStatus(OrderStatus status) {
        List<Order> orders = findWhere(order -> order.getStatus() == status);
        orders.sort(NEWEST_FIRST);
        return orders;
    }

    public List<Order> findSince(long epochMillis) {
        List<Order> orders = findWhere(order -> order.getCreatedAt() >= epochMillis);
        orders.sort(NEWEST_FIRST);
        return orders;
    }

    public boolean hasOpenOrdersForCustomer(String customerId) {
        return findByCustomer(customerId).stream().anyMatch(order -> order.getStatus().isOpen());
    }

    public boolean referencesProduct(String productId) {
        return findWhere(order -> order.getStatus().isOpen()).stream()
                .flatMap(order -> order.getItems().stream())
                .anyMatch(item -> productId != null && productId.equals(item.getProductId()));
    }

    public double revenue(List<Order> orders) {
        return orders.stream()
                .filter(order -> order.getStatus() != OrderStatus.CANCELLED)
                .mapToDouble(Order::getTotal)
                .sum();
    }
}
