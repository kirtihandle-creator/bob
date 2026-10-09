package com.shopflow.backend.persistence;

import com.shopflow.backend.repository.CategoryRepository;
import com.shopflow.backend.repository.CustomerRepository;
import com.shopflow.backend.repository.OrderRepository;
import com.shopflow.backend.repository.ProductRepository;
import com.shopflow.backend.repository.UserRepository;
import com.shopflow.backend.util.PasswordHasher;
import com.shopflow.common.model.Category;
import com.shopflow.common.model.Customer;
import com.shopflow.common.model.Order;
import com.shopflow.common.model.OrderItem;
import com.shopflow.common.model.OrderStatus;
import com.shopflow.common.model.Product;
import com.shopflow.common.model.User;

import java.util.logging.Logger;

/**
 * Populates empty repositories with demo data so the desktop client has
 * something to show on first launch. Default login: admin / admin123.
 */
public final class SeedData {

    private static final Logger LOG = Logger.getLogger(SeedData.class.getName());

    private SeedData() {
    }

    public static void seedIfEmpty(UserRepository users, CategoryRepository categories,
                                   ProductRepository products, CustomerRepository customers,
                                   OrderRepository orders) {
        if (users.isEmpty()) {
            users.save(new User(null, "admin", PasswordHasher.hash("admin123"), User.ROLE_ADMIN, "Administrator"));
            users.save(new User(null, "staff", PasswordHasher.hash("staff123"), User.ROLE_STAFF, "Store Staff"));
            LOG.info("Seeded default users (admin/admin123, staff/staff123)");
        }
        if (!categories.isEmpty() || !products.isEmpty()) {
            return;
        }
        Category electronics = categories.save(new Category(null, "Electronics", "Gadgets and devices"));
        Category books = categories.save(new Category(null, "Books", "Printed and digital books"));
        Category home = categories.save(new Category(null, "Home", "Kitchen and living"));

        Product laptop = products.save(new Product(null, "Laptop 14\"", "LAP-14", electronics.getId(),
                "Lightweight 14 inch laptop", 899.00, 12));
        Product headphones = products.save(new Product(null, "Wireless Headphones", "HP-200", electronics.getId(),
                "Noise cancelling over-ear headphones", 149.99, 4));
        Product mouse = products.save(new Product(null, "Ergonomic Mouse", "MS-ERG", electronics.getId(),
                "Vertical ergonomic mouse", 39.50, 30));
        Product novel = products.save(new Product(null, "The Silent Harbor", "BK-SH1", books.getId(),
                "Mystery novel, paperback", 12.99, 50));
        Product cookbook = products.save(new Product(null, "Weeknight Cooking", "BK-WC2", books.getId(),
                "Quick recipes for busy evenings", 24.00, 3));
        Product kettle = products.save(new Product(null, "Electric Kettle", "HM-KET", home.getId(),
                "1.7 litre stainless steel kettle", 34.95, 18));

        Customer alice = customers.save(new Customer(null, "Alice Johnson", "alice@example.com",
                "555-0101", "12 Harbor St, Springfield"));
        Customer bob = customers.save(new Customer(null, "Bob Martinez", "bob@example.com",
                "555-0102", "88 Elm Ave, Shelbyville"));
        Customer chen = customers.save(new Customer(null, "Chen Wei", "chen@example.com",
                "555-0103", "5 Lotus Rd, Capital City"));

        Order first = new Order();
        first.setCustomerId(alice.getId());
        first.setCustomerName(alice.getName());
        first.addItem(OrderItem.of(laptop, 1));
        first.addItem(OrderItem.of(mouse, 2));
        first.setStatus(OrderStatus.PAID);
        orders.save(first);

        Order second = new Order();
        second.setCustomerId(bob.getId());
        second.setCustomerName(bob.getName());
        second.addItem(OrderItem.of(novel, 3));
        second.addItem(OrderItem.of(cookbook, 1));
        second.setStatus(OrderStatus.SHIPPED);
        orders.save(second);

        Order third = new Order();
        third.setCustomerId(chen.getId());
        third.setCustomerName(chen.getName());
        third.addItem(OrderItem.of(headphones, 1));
        third.addItem(OrderItem.of(kettle, 1));
        third.setNotes("Gift wrap please");
        orders.save(third);

        LOG.info("Seeded demo categories, products, customers and orders");
    }
}
