package com.shopflow.backend.server;

import com.shopflow.common.json.Json;
import com.shopflow.common.model.User;
import com.sun.net.httpserver.HttpExchange;

import java.io.IOException;
import java.net.URLDecoder;
import java.nio.charset.StandardCharsets;
import java.util.LinkedHashMap;
import java.util.Map;

/**
 * Wraps an {@link HttpExchange} with convenient accessors for path
 * parameters, query parameters, the JSON body and the authenticated user.
 */
public class RequestContext {

    private final HttpExchange exchange;
    private final Map<String, String> pathParams;
    private final Map<String, String> queryParams;
    private String cachedBody;
    private User user;
    private int responseStatus = 200;

    public RequestContext(HttpExchange exchange, Map<String, String> pathParams) {
        this.exchange = exchange;
        this.pathParams = pathParams;
        this.queryParams = parseQuery(exchange.getRequestURI().getRawQuery());
    }

    public String method() {
        return exchange.getRequestMethod();
    }

    public String path() {
        return exchange.getRequestURI().getPath();
    }

    public String header(String name) {
        return exchange.getRequestHeaders().getFirst(name);
    }

    public String pathParam(String name) {
        String value = pathParams.get(name);
        if (value == null) {
            throw ApiException.badRequest("Missing path parameter " + name);
        }
        return value;
    }

    public String query(String name, String defaultValue) {
        return queryParams.getOrDefault(name, defaultValue);
    }

    public int queryInt(String name, int defaultValue) {
        try {
            return Integer.parseInt(queryParams.getOrDefault(name, String.valueOf(defaultValue)));
        } catch (NumberFormatException e) {
            throw ApiException.badRequest("Query parameter " + name + " must be a number");
        }
    }

    public String body() throws IOException {
        if (cachedBody == null) {
            cachedBody = new String(exchange.getRequestBody().readAllBytes(), StandardCharsets.UTF_8);
        }
        return cachedBody;
    }

    public Map<String, Object> jsonBody() throws IOException {
        String raw = body();
        if (raw.isBlank()) {
            throw ApiException.badRequest("Request body is required");
        }
        try {
            return Json.object(raw);
        } catch (RuntimeException e) {
            throw ApiException.badRequest("Malformed JSON body: " + e.getMessage());
        }
    }

    public User user() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

    public void setResponseStatus(int status) {
        this.responseStatus = status;
    }

    public int responseStatus() {
        return responseStatus;
    }

    public HttpExchange exchange() {
        return exchange;
    }

    private static Map<String, String> parseQuery(String rawQuery) {
        Map<String, String> params = new LinkedHashMap<>();
        if (rawQuery == null || rawQuery.isBlank()) {
            return params;
        }
        for (String pair : rawQuery.split("&")) {
            int eq = pair.indexOf('=');
            String key = eq < 0 ? pair : pair.substring(0, eq);
            String value = eq < 0 ? "" : pair.substring(eq + 1);
            params.put(URLDecoder.decode(key, StandardCharsets.UTF_8),
                    URLDecoder.decode(value, StandardCharsets.UTF_8));
        }
        return params;
    }
}
