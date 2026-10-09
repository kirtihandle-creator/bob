package com.shopflow.backend;

import com.shopflow.backend.controller.AuthController;
import com.shopflow.backend.controller.CategoryController;
import com.shopflow.backend.controller.CustomerController;
import com.shopflow.backend.controller.OrderController;
import com.shopflow.backend.controller.ProductController;
import com.shopflow.backend.controller.ReportController;
import com.shopflow.backend.persistence.FileStore;
import com.shopflow.backend.persistence.SeedData;
import com.shopflow.backend.repository.CategoryRepository;
import com.shopflow.backend.repository.CustomerRepository;
import com.shopflow.backend.repository.OrderRepository;
import com.shopflow.backend.repository.ProductRepository;
import com.shopflow.backend.repository.UserRepository;
import com.shopflow.backend.server.Route;
import com.shopflow.backend.server.Router;
import com.shopflow.backend.server.ServerConfig;
import com.shopflow.backend.service.AuthService;
import com.shopflow.backend.service.CategoryService;
import com.shopflow.backend.service.CustomerService;
import com.shopflow.backend.service.OrderService;
import com.shopflow.backend.service.ProductService;
import com.shopflow.backend.service.ReportService;
import com.sun.net.httpserver.HttpServer;

import java.io.IOException;
import java.net.InetSocketAddress;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.logging.Logger;

/**
 * Backend entry point. Wires repositories, services and controllers
 * together and starts the JDK HTTP server.
 *
 * <pre>
 * java -cp out/backend com.shopflow.backend.Main
 * </pre>
 */
public final class Main {

    private static final Logger LOG = Logger.getLogger(Main.class.getName());

    private Main() {
    }

    public static void main(String[] args) throws IOException {
        ServerConfig config = ServerConfig.fromEnvironment();
        LOG.info(() -> "Starting with " + config);

        FileStore fileStore = new FileStore(config.getDataDir());
        fileStore.ensureDirectory();

        UserRepository users = new UserRepository();
        CategoryRepository categories = new CategoryRepository();
        ProductRepository products = new ProductRepository();
        CustomerRepository customers = new CustomerRepository();
        OrderRepository orders = new OrderRepository();
        fileStore.attach(users);
        fileStore.attach(categories);
        fileStore.attach(products);
        fileStore.attach(customers);
        fileStore.attach(orders);

        if (config.isSeedOnEmpty()) {
            SeedData.seedIfEmpty(users, categories, products, customers, orders);
        }

        AuthService authService = new AuthService(users, config.getTokenTtlMillis());
        CategoryService categoryService = new CategoryService(categories, products);
        ProductService productService = new ProductService(products, categories, orders);
        CustomerService customerService = new CustomerService(customers, orders);
        OrderService orderService = new OrderService(orders, productService, customerService);
        ReportService reportService = new ReportService(config, fileStore);

        Router router = new Router(authService);
        new AuthController(authService, users).register(router);
        new CategoryController(categoryService).register(router);
        new ProductController(productService).register(router);
        new CustomerController(customerService, orderService).register(router);
        new OrderController(orderService).register(router);
        new ReportController(reportService, authService).register(router);

        for (Route route : router.getRoutes()) {
            LOG.fine(() -> "Route " + route);
        }

        ExecutorService executor = Executors.newFixedThreadPool(config.getThreadPoolSize());
        HttpServer server = HttpServer.create(new InetSocketAddress(config.getPort()), 0);
        server.createContext("/", router);
        server.setExecutor(executor);
        server.start();
        LOG.info(() -> "ShopFlow backend listening on http://localhost:" + config.getPort()
                + " with " + router.getRoutes().size() + " routes");

        Runtime.getRuntime().addShutdownHook(new Thread(() -> {
            LOG.info("Shutting down");
            server.stop(1);
            executor.shutdownNow();
        }, "shutdown"));
    }
}
