package com.shopflow.frontend.api;

import com.shopflow.common.json.Json;
import com.shopflow.common.model.Order;
import com.shopflow.common.model.OrderStatus;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

/**
 * Calls under /api/orders.
 */
public class OrderApi {

    /** One line of a new order request. */
    public record NewLine(String productId, int quantity) {
    }

    private final ApiClient client;

    public OrderApi(ApiClient client) {
        this.client = client;
    }

    public List<Order> list(OrderStatus status) {
        String query = ApiClient.query("status", status == null ? "" : status.name());
        return Json.mapList(client.getItems("/api/orders" + query), Order::fromJson);
    }

    public Order get(String id) {
        return Order.fromJson(client.getObject("/api/orders/" + id));
    }

    public Order create(String customerId, String notes, List<NewLine> lines) {
        List<Object> items = new ArrayList<>();
        for (NewLine line : lines) {
            items.add(Json.map("productId", line.productId(), "quantity", line.quantity()));
        }
        Map<String, Object> body = Json.map(
                "customerId", customerId,
                "notes", notes,
                "items", items);
        return Order.fromJson(client.post("/api/orders", body));
    }

    public Order changeStatus(String id, OrderStatus status) {
        return Order.fromJson(client.post("/api/orders/" + id + "/status", Json.map("status", status.name())));
    }

    public void delete(String id) {
        client.delete("/api/orders/" + id);
    }
}
