package com.shopflow.backend.persistence;

import com.shopflow.backend.repository.CategoryRepository;
import com.shopflow.backend.repository.CustomerRepository;
import com.shopflow.backend.repository.OrderRepository;
import com.shopflow.backend.repository.ProductRepository;
import com.shopflow.backend.repository.UserRepository;
import com.shopflow.backend.server.ServerConfig;
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
 * Populates empty repositories on first start.
 *
 * <p>No credentials are hardcoded. The first administrator is created only
 * from an explicitly configured bootstrap password
 * ({@code -Dshopflow.adminPassword=...} or {@code SHOPFLOW_ADMIN_PASSWORD}).
 * When the user store is empty and no password is configured, startup is
 * refused so the backend is never exposed with a guessable account.
 *
 * <p>Demo catalog data (categories, products, customers, orders) contains no
 * secrets and is seeded when {@code seedOnEmpty} is enabled.
 */
public final class SeedData {

    private static final Logger LOG = Logger.getLogger(SeedData.class.getName());

    private SeedData() {
    }

    /**
     * Creates the bootstrap administrator if no users exist yet.
     *
     * @throws IllegalStateException when users are empty and no password is configured
     */
    public static void bootstrapAdmin(UserRepository users, ServerConfig config) {
        if (!users.isEmpty()) {
            if (config.hasBootstrapAdminPassword()) {
                LOG.warning("Bootstrap admin password is set but users already exist; it is ignored");
            }
            return;
        }
        if (!config.hasBootstrapAdminPassword()) {
            throw new IllegalStateException("No users exist and no bootstrap administrator password is "
                    + "configured. Start once with -Dshopflow.adminPassword=<password> "
                    + "(or SHOPFLOW_ADMIN_PASSWORD) to create the first administrator.");
        }
        String weakness = PasswordHasher.weaknessReason(config.getBootstrapAdminPassword());
        if (weakness != null) {
            throw new IllegalStateException("Bootstrap administrator password rejected: " + weakness);
        }
        String username = config.getBootstrapAdminUser();
        users.save(new User(null, username, PasswordHasher.hash(config.getBootstrapAdminPassword()),
                User.ROLE_ADMIN, "Administrator"));
        LOG.info(() -> "Created bootstrap administrator '" + username
                + "'. Remove the bootstrap password from the environment now.");
    }

    public static void seedCatalogIfEmpty(CategoryRepository categories, ProductRepository products,
                                          CustomerRepository customers, OrderRepository orders) {
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

        orders.save(order(alice, OrderStatus.PAID, "", OrderItem.of(laptop, 1), OrderItem.of(mouse, 2)));
        orders.save(order(bob, OrderStatus.SHIPPED, "", OrderItem.of(novel, 3), OrderItem.of(cookbook, 1)));
        orders.save(order(chen, OrderStatus.NEW, "Gift wrap please",
                OrderItem.of(headphones, 1), OrderItem.of(kettle, 1)));

        LOG.info("Seeded demo categories, products, customers and orders");
    }

    private static Order order(Customer customer, OrderStatus status, String notes, OrderItem... items) {
        Order order = new Order();
        order.setCustomerId(customer.getId());
        order.setCustomerName(customer.getName());
        order.setNotes(notes);
        for (OrderItem item : items) {
            order.addItem(item);
        }
        order.setStatus(status);
        return order;
    }
}
