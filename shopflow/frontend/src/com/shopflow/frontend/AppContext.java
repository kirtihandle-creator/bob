package com.shopflow.frontend;

import com.shopflow.frontend.api.ApiClient;
import com.shopflow.frontend.api.AuthApi;
import com.shopflow.frontend.api.CategoryApi;
import com.shopflow.frontend.api.CustomerApi;
import com.shopflow.frontend.api.OrderApi;
import com.shopflow.frontend.api.ProductApi;
import com.shopflow.frontend.api.ReportApi;
import com.shopflow.frontend.session.Session;

/**
 * Wires the session, HTTP client and typed API facades together so the
 * UI classes receive one object instead of seven.
 */
public class AppContext {

    public static final String DEFAULT_BASE_URL = "http://localhost:8080";

    private final Session session;
    private final ApiClient client;
    private final AuthApi auth;
    private final CategoryApi categories;
    private final ProductApi products;
    private final CustomerApi customers;
    private final OrderApi orders;
    private final ReportApi reports;

    public AppContext(String baseUrl) {
        this.session = new Session();
        this.client = new ApiClient(baseUrl, session);
        this.auth = new AuthApi(client, session);
        this.categories = new CategoryApi(client);
        this.products = new ProductApi(client);
        this.customers = new CustomerApi(client);
        this.orders = new OrderApi(client);
        this.reports = new ReportApi(client);
    }

    public static String resolveBaseUrl(String[] args) {
        for (String arg : args) {
            if (arg.startsWith("--url=")) {
                return arg.substring("--url=".length());
            }
        }
        String property = System.getProperty("shopflow.url");
        if (property != null && !property.isBlank()) {
            return property;
        }
        String env = System.getenv("SHOPFLOW_URL");
        if (env != null && !env.isBlank()) {
            return env;
        }
        return DEFAULT_BASE_URL;
    }

    public Session session() {
        return session;
    }

    public ApiClient client() {
        return client;
    }

    public AuthApi auth() {
        return auth;
    }

    public CategoryApi categories() {
        return categories;
    }

    public ProductApi products() {
        return products;
    }

    public CustomerApi customers() {
        return customers;
    }

    public OrderApi orders() {
        return orders;
    }

    public ReportApi reports() {
        return reports;
    }
}
