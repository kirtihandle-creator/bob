package com.shopflow.frontend.api;

import com.shopflow.common.json.Json;
import com.shopflow.common.model.Customer;
import com.shopflow.common.model.Identifiable;
import com.shopflow.common.model.Order;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

/**
 * Calls under /api/customers. List responses include order statistics
 * which are carried in {@link Row}.
 */
public class CustomerApi {

    /** A customer plus order count and lifetime value. */
    public record Row(Customer customer, int orderCount, double lifetimeValue) {
    }

    private final ApiClient client;

    public CustomerApi(ApiClient client) {
        this.client = client;
    }

    public List<Row> list(String search) {
        List<Row> rows = new ArrayList<>();
        String query = ApiClient.query("q", search);
        for (Map<String, Object> map : Json.mapList(client.getItems("/api/customers" + query), m -> m)) {
            rows.add(toRow(map));
        }
        return rows;
    }

    public List<Customer> listAll() {
        List<Customer> customers = new ArrayList<>();
        for (Row row : list("")) {
            customers.add(row.customer());
        }
        return customers;
    }

    public Row get(String id) {
        return toRow(client.getObject("/api/customers/" + id));
    }

    public List<Order> orders(String customerId) {
        return Json.mapList(client.getItems("/api/customers/" + customerId + "/orders"), Order::fromJson);
    }

    public Row create(Customer customer) {
        return toRow(client.post("/api/customers", customer.toJson()));
    }

    public Row update(Customer customer) {
        return toRow(client.put("/api/customers/" + customer.getId(), customer.toJson()));
    }

    public void delete(String id) {
        client.delete("/api/customers/" + id);
    }

    private static Row toRow(Map<String, Object> map) {
        return new Row(Customer.fromJson(map),
                Identifiable.integer(map, "orderCount"),
                Identifiable.dbl(map, "lifetimeValue"));
    }
}
