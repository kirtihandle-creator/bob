package com.shopflow.common.model;

import java.util.LinkedHashMap;
import java.util.Map;

/**
 * A customer who can place orders.
 */
public class Customer implements Identifiable {

    private String id;
    private String name;
    private String email;
    private String phone;
    private String address;
    private long createdAt;

    public Customer() {
        this.createdAt = System.currentTimeMillis();
    }

    public Customer(String id, String name, String email, String phone, String address) {
        this();
        this.id = id;
        this.name = name;
        this.email = email;
        this.phone = phone;
        this.address = address;
    }

    @Override
    public String getId() {
        return id;
    }

    @Override
    public void setId(String id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public long getCreatedAt() {
        return createdAt;
    }

    public void setCreatedAt(long createdAt) {
        this.createdAt = createdAt;
    }

    @Override
    public Map<String, Object> toJson() {
        Map<String, Object> map = new LinkedHashMap<>();
        map.put("id", id);
        map.put("name", name);
        map.put("email", email);
        map.put("phone", phone);
        map.put("address", address);
        map.put("createdAt", createdAt);
        return map;
    }

    public static Customer fromJson(Map<String, Object> map) {
        Customer customer = new Customer();
        customer.id = Identifiable.idOrNull(Identifiable.str(map, "id"));
        customer.name = Identifiable.str(map, "name");
        customer.email = Identifiable.str(map, "email");
        customer.phone = Identifiable.str(map, "phone");
        customer.address = Identifiable.str(map, "address");
        long created = Identifiable.lng(map, "createdAt");
        customer.createdAt = created == 0 ? System.currentTimeMillis() : created;
        return customer;
    }

    @Override
    public String toString() {
        return name == null ? "" : name;
    }
}
