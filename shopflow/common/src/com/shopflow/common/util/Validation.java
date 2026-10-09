package com.shopflow.common.util;

import java.util.ArrayList;
import java.util.List;
import java.util.regex.Pattern;

/**
 * Collects validation failures for a single input form or request so
 * callers can report every problem at once instead of one at a time.
 */
public final class Validation {

    private static final Pattern EMAIL = Pattern.compile("^[\\w.+-]+@[\\w-]+(\\.[\\w-]+)+$");
    private static final Pattern SKU = Pattern.compile("^[A-Z0-9][A-Z0-9-]{2,19}$");

    private final List<String> errors = new ArrayList<>();

    public static Validation begin() {
        return new Validation();
    }

    public Validation require(String value, String field) {
        if (value == null || value.isBlank()) {
            errors.add(field + " is required");
        }
        return this;
    }

    public Validation maxLength(String value, int max, String field) {
        if (value != null && value.length() > max) {
            errors.add(field + " must be at most " + max + " characters");
        }
        return this;
    }

    public Validation email(String value, String field) {
        if (value != null && !value.isBlank() && !EMAIL.matcher(value).matches()) {
            errors.add(field + " is not a valid email address");
        }
        return this;
    }

    public Validation sku(String value, String field) {
        if (value != null && !value.isBlank() && !SKU.matcher(value).matches()) {
            errors.add(field + " must be 3-20 uppercase letters, digits or dashes");
        }
        return this;
    }

    public Validation nonNegative(double value, String field) {
        if (value < 0) {
            errors.add(field + " cannot be negative");
        }
        return this;
    }

    public Validation positive(double value, String field) {
        if (value <= 0) {
            errors.add(field + " must be greater than zero");
        }
        return this;
    }

    public Validation check(boolean condition, String message) {
        if (!condition) {
            errors.add(message);
        }
        return this;
    }

    public boolean isValid() {
        return errors.isEmpty();
    }

    public List<String> getErrors() {
        return List.copyOf(errors);
    }

    public String getMessage() {
        return String.join("; ", errors);
    }

    /** Throws an {@link IllegalArgumentException} with all errors if any exist. */
    public void throwIfInvalid() {
        if (!isValid()) {
            throw new IllegalArgumentException(getMessage());
        }
    }
}
