package com.shopflow.backend.repository;

import com.shopflow.common.model.Customer;

import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.Optional;

/**
 * Store for {@link Customer} entities with email uniqueness helpers.
 */
public class CustomerRepository extends InMemoryRepository<Customer> {

    public CustomerRepository() {
        super("cus");
    }

    @Override
    public String getName() {
        return "customers";
    }

    @Override
    public Customer fromJson(Map<String, Object> map) {
        return Customer.fromJson(map);
    }

    public Optional<Customer> findByEmail(String email) {
        if (email == null || email.isBlank()) {
            return Optional.empty();
        }
        return findFirst(customer -> email.trim().equalsIgnoreCase(customer.getEmail()));
    }

    public boolean emailTakenByOther(String email, String excludeId) {
        return findByEmail(email)
                .map(found -> !found.getId().equals(excludeId))
                .orElse(false);
    }

    /** Case-insensitive match on name, email or phone. */
    public List<Customer> search(String term) {
        if (term == null || term.isBlank()) {
            return findAll();
        }
        String needle = term.toLowerCase(Locale.ROOT);
        return findWhere(customer ->
                contains(customer.getName(), needle)
                        || contains(customer.getEmail(), needle)
                        || contains(customer.getPhone(), needle));
    }

    public String nameOf(String customerId) {
        return findById(customerId).map(Customer::getName).orElse("Unknown customer");
    }

    private static boolean contains(String haystack, String needle) {
        return haystack != null && haystack.toLowerCase(Locale.ROOT).contains(needle);
    }
}
