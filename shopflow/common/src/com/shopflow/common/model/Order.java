package com.shopflow.common.model;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/**
 * A customer order composed of one or more line items.
 */
public class Order implements Identifiable {

    private String id;
    private String customerId;
    private String customerName;
    private OrderStatus status = OrderStatus.NEW;
    private long createdAt = System.currentTimeMillis();
    private long updatedAt = createdAt;
    private String notes = "";
    private final List<OrderItem> items = new ArrayList<>();

    @Override
    public String getId() {
        return id;
    }

    @Override
    public void setId(String id) {
        this.id = id;
    }

    public String getCustomerId() {
        return customerId;
    }

    public void setCustomerId(String customerId) {
        this.customerId = customerId;
    }

    public String getCustomerName() {
        return customerName;
    }

    public void setCustomerName(String customerName) {
        this.customerName = customerName;
    }

    public OrderStatus getStatus() {
        return status;
    }

    public void setStatus(OrderStatus status) {
        this.status = status;
        this.updatedAt = System.currentTimeMillis();
    }

    public long getCreatedAt() {
        return createdAt;
    }

    public long getUpdatedAt() {
        return updatedAt;
    }

    public String getNotes() {
        return notes;
    }

    public void setNotes(String notes) {
        this.notes = notes == null ? "" : notes;
    }

    public List<OrderItem> getItems() {
        return items;
    }

    public void addItem(OrderItem item) {
        items.add(item);
    }

    public int getItemCount() {
        return items.stream().mapToInt(OrderItem::getQuantity).sum();
    }

    public double getTotal() {
        return items.stream().mapToDouble(OrderItem::getLineTotal).sum();
    }

    @Override
    public Map<String, Object> toJson() {
        Map<String, Object> map = new LinkedHashMap<>();
        map.put("id", id);
        map.put("customerId", customerId);
        map.put("customerName", customerName);
        map.put("status", status.name());
        map.put("createdAt", createdAt);
        map.put("updatedAt", updatedAt);
        map.put("notes", notes);
        List<Object> itemList = new ArrayList<>();
        for (OrderItem item : items) {
            itemList.add(item.toJson());
        }
        map.put("items", itemList);
        map.put("total", getTotal());
        return map;
    }

    @SuppressWarnings("unchecked")
    public static Order fromJson(Map<String, Object> map) {
        Order order = new Order();
        order.id = Identifiable.idOrNull(Identifiable.str(map, "id"));
        order.customerId = Identifiable.str(map, "customerId");
        order.customerName = Identifiable.str(map, "customerName");
        order.status = OrderStatus.parse(Identifiable.str(map, "status"));
        order.notes = Identifiable.str(map, "notes");
        long created = Identifiable.lng(map, "createdAt");
        order.createdAt = created == 0 ? System.currentTimeMillis() : created;
        long updated = Identifiable.lng(map, "updatedAt");
        order.updatedAt = updated == 0 ? order.createdAt : updated;
        Object rawItems = map.get("items");
        if (rawItems instanceof List<?> list) {
            for (Object element : list) {
                if (element instanceof Map<?, ?> itemMap) {
                    order.items.add(OrderItem.fromJson((Map<String, Object>) itemMap));
                }
            }
        }
        return order;
    }
}
