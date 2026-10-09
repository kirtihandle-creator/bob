package com.shopflow.backend.service;

import com.shopflow.backend.repository.CustomerRepository;
import com.shopflow.backend.repository.OrderRepository;
import com.shopflow.backend.server.ApiException;
import com.shopflow.common.model.Customer;
import com.shopflow.common.model.Order;
import com.shopflow.common.util.Validation;

import java.util.List;
import java.util.Map;

/**
 * Business rules for customers: unique email, required name and no
 * deletion while the customer has open orders.
 */
public class CustomerService {

    private final CustomerRepository customers;
    private final OrderRepository orders;

    public CustomerService(CustomerRepository customers, OrderRepository orders) {
        this.customers = customers;
        this.orders = orders;
    }

    public List<Customer> list(String search) {
        return customers.search(search);
    }

    public Customer get(String id) {
        return customers.findById(id).orElseThrow(() -> ApiException.notFound("Customer", id));
    }

    public Customer create(Map<String, Object> body) {
        Customer customer = Customer.fromJson(body);
        customer.setId(null);
        customer.setEmail(customer.getEmail().trim().toLowerCase());
        validate(customer);
        return customers.save(customer);
    }

    public Customer update(String id, Map<String, Object> body) {
        Customer existing = get(id);
        Customer incoming = Customer.fromJson(body);
        incoming.setId(id);
        incoming.setEmail(incoming.getEmail().trim().toLowerCase());
        validate(incoming);
        existing.setName(incoming.getName());
        existing.setEmail(incoming.getEmail());
        existing.setPhone(incoming.getPhone());
        existing.setAddress(incoming.getAddress());
        Customer saved = customers.save(existing);
        renameOnOrders(saved);
        return saved;
    }

    public void delete(String id) {
        get(id);
        if (orders.hasOpenOrdersForCustomer(id)) {
            throw ApiException.conflict("Customer has open orders and cannot be deleted");
        }
        customers.delete(id);
    }

    public Map<String, Object> enrich(Customer customer) {
        Map<String, Object> json = customer.toJson();
        List<Order> history = orders.findByCustomer(customer.getId());
        json.put("orderCount", history.size());
        json.put("lifetimeValue", orders.revenue(history));
        return json;
    }

    /** Keeps the denormalized customer name on orders in sync after a rename. */
    private void renameOnOrders(Customer customer) {
        for (Order order : orders.findByCustomer(customer.getId())) {
            if (!customer.getName().equals(order.getCustomerName())) {
                order.setCustomerName(customer.getName());
                orders.save(order);
            }
        }
    }

    private void validate(Customer customer) {
        Validation.begin()
                .require(customer.getName(), "Name")
                .maxLength(customer.getName(), 80, "Name")
                .require(customer.getEmail(), "Email")
                .email(customer.getEmail(), "Email")
                .maxLength(customer.getPhone(), 30, "Phone")
                .maxLength(customer.getAddress(), 200, "Address")
                .check(!customers.emailTakenByOther(customer.getEmail(), customer.getId()),
                        "A customer with that email already exists")
                .throwIfInvalid();
    }
}
