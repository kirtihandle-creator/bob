package com.shopflow.backend.server;

/**
 * An error that should be reported to the HTTP client with a specific
 * status code. Controllers and services throw these; the router turns
 * them into JSON error responses.
 */
public class ApiException extends RuntimeException {

    private static final long serialVersionUID = 1L;

    private final int status;

    public ApiException(int status, String message) {
        super(message);
        this.status = status;
    }

    public ApiException(int status, String message, Throwable cause) {
        super(message, cause);
        this.status = status;
    }

    public int getStatus() {
        return status;
    }

    public static ApiException badRequest(String message) {
        return new ApiException(400, message);
    }

    public static ApiException unauthorized(String message) {
        return new ApiException(401, message);
    }

    public static ApiException forbidden(String message) {
        return new ApiException(403, message);
    }

    public static ApiException notFound(String what, String id) {
        return new ApiException(404, what + " not found: " + id);
    }

    public static ApiException conflict(String message) {
        return new ApiException(409, message);
    }

    public static ApiException internal(String message, Throwable cause) {
        return new ApiException(500, message, cause);
    }
}
