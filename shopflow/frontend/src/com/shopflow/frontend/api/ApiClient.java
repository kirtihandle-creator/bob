package com.shopflow.frontend.api;

import com.shopflow.common.json.Json;
import com.shopflow.common.model.Identifiable;
import com.shopflow.frontend.session.Session;

import java.io.IOException;
import java.net.ConnectException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.util.List;
import java.util.Map;

/**
 * Thin HTTP/JSON client over {@link HttpClient}. Attaches the session's
 * bearer token to every call and converts error envelopes into
 * {@link ApiException}.
 */
public class ApiClient {

    private final HttpClient http;
    private final String baseUrl;
    private final Session session;

    public ApiClient(String baseUrl, Session session) {
        this.baseUrl = baseUrl.endsWith("/") ? baseUrl.substring(0, baseUrl.length() - 1) : baseUrl;
        this.session = session;
        this.http = HttpClient.newBuilder()
                .connectTimeout(Duration.ofSeconds(5))
                .build();
    }

    public String getBaseUrl() {
        return baseUrl;
    }

    public Map<String, Object> getObject(String path) {
        return asObject(send("GET", path, null));
    }

    public List<Object> getItems(String path) {
        return Json.nestedList(getObject(path), "items");
    }

    public Map<String, Object> post(String path, Object body) {
        return asObject(send("POST", path, body));
    }

    public Map<String, Object> put(String path, Object body) {
        return asObject(send("PUT", path, body));
    }

    public void delete(String path) {
        send("DELETE", path, null);
    }

    /** Builds a query string from alternating key/value pairs, skipping blanks. */
    public static String query(Object... keyValues) {
        StringBuilder builder = new StringBuilder();
        for (int i = 0; i + 1 < keyValues.length; i += 2) {
            String value = keyValues[i + 1] == null ? "" : String.valueOf(keyValues[i + 1]);
            if (value.isBlank()) {
                continue;
            }
            builder.append(builder.isEmpty() ? '?' : '&');
            builder.append(URLEncoder.encode(String.valueOf(keyValues[i]), StandardCharsets.UTF_8));
            builder.append('=');
            builder.append(URLEncoder.encode(value, StandardCharsets.UTF_8));
        }
        return builder.toString();
    }

    private String send(String method, String path, Object body) {
        HttpRequest.Builder builder = HttpRequest.newBuilder()
                .uri(URI.create(baseUrl + path))
                .timeout(Duration.ofSeconds(30))
                .header("Accept", "application/json");
        if (session.isLoggedIn()) {
            builder.header("Authorization", "Bearer " + session.getToken());
        }
        HttpRequest.BodyPublisher publisher = body == null
                ? HttpRequest.BodyPublishers.noBody()
                : HttpRequest.BodyPublishers.ofString(Json.stringify(body), StandardCharsets.UTF_8);
        if (body != null) {
            builder.header("Content-Type", "application/json");
        }
        HttpRequest request = builder.method(method, publisher).build();
        try {
            HttpResponse<String> response = http.send(request, HttpResponse.BodyHandlers.ofString());
            if (response.statusCode() >= 400) {
                throw new ApiException(response.statusCode(), errorMessage(response.body()));
            }
            return response.body();
        } catch (ConnectException e) {
            throw new ApiException(0, "connection refused at " + baseUrl, e);
        } catch (IOException e) {
            throw new ApiException(0, e.getMessage() == null ? e.toString() : e.getMessage(), e);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            throw new ApiException(0, "request interrupted", e);
        }
    }

    private static Map<String, Object> asObject(String body) {
        if (body == null || body.isBlank()) {
            return Json.map();
        }
        return Json.object(body);
    }

    private static String errorMessage(String body) {
        try {
            String message = Identifiable.str(Json.object(body), "error");
            return message.isBlank() ? "Request failed" : message;
        } catch (RuntimeException e) {
            return body == null || body.isBlank() ? "Request failed" : body;
        }
    }
}
