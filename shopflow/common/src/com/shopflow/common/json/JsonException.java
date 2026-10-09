package com.shopflow.common.json;

/**
 * Raised when JSON text cannot be parsed or has an unexpected shape.
 */
public class JsonException extends RuntimeException {

    private static final long serialVersionUID = 1L;

    public JsonException(String message) {
        super(message);
    }

    public JsonException(String message, Throwable cause) {
        super(message, cause);
    }
}
