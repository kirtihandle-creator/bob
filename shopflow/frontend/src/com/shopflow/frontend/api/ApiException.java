package com.shopflow.frontend.api;

/**
 * Raised by the API client when the backend returns an error status or
 * cannot be reached. The status is 0 for connection failures.
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

    public boolean isUnauthorized() {
        return status == 401;
    }

    public boolean isConnectionFailure() {
        return status == 0;
    }

    /** Short description for status bars and dialogs. */
    public String userMessage() {
        if (isConnectionFailure()) {
            return "Cannot reach the backend: " + getMessage();
        }
        return getMessage() + " (HTTP " + status + ")";
    }
}
