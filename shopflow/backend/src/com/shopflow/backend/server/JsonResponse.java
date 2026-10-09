package com.shopflow.backend.server;

import com.shopflow.common.json.Json;
import com.sun.net.httpserver.HttpExchange;

import java.io.IOException;
import java.io.OutputStream;
import java.nio.charset.StandardCharsets;
import java.util.List;
import java.util.Map;

/**
 * Writes JSON responses to an {@link HttpExchange}, including the
 * standard error envelope {@code {"error": "...", "status": 404}}.
 */
public final class JsonResponse {

    private JsonResponse() {
    }

    public static void send(HttpExchange exchange, int status, Object payload) throws IOException {
        byte[] bytes = Json.stringify(payload).getBytes(StandardCharsets.UTF_8);
        exchange.getResponseHeaders().set("Content-Type", "application/json; charset=utf-8");
        applyCors(exchange);
        exchange.sendResponseHeaders(status, bytes.length);
        try (OutputStream out = exchange.getResponseBody()) {
            out.write(bytes);
        }
    }

    public static void sendEmpty(HttpExchange exchange, int status) throws IOException {
        applyCors(exchange);
        exchange.sendResponseHeaders(status, -1);
        exchange.close();
    }

    public static void sendError(HttpExchange exchange, int status, String message) throws IOException {
        send(exchange, status, Json.map("error", message, "status", status));
    }

    public static void sendErrors(HttpExchange exchange, int status, List<String> messages) throws IOException {
        send(exchange, status, Json.map(
                "error", String.join("; ", messages),
                "errors", messages,
                "status", status));
    }

    public static Map<String, Object> ok(String message) {
        return Json.map("ok", true, "message", message);
    }

    public static Map<String, Object> page(List<?> items, int total, int offset, int limit) {
        return Json.map(
                "items", items,
                "total", total,
                "offset", offset,
                "limit", limit);
    }

    /**
     * Permissive CORS so a browser-based client could also talk to the API.
     * The Swing client ignores these headers.
     */
    private static void applyCors(HttpExchange exchange) {
        exchange.getResponseHeaders().set("Access-Control-Allow-Origin", "*");
        exchange.getResponseHeaders().set("Access-Control-Allow-Methods", "GET, POST, PUT, PATCH, DELETE, OPTIONS");
        exchange.getResponseHeaders().set("Access-Control-Allow-Headers", "Content-Type, Authorization");
    }
}
