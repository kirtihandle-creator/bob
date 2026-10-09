package com.shopflow.common.model;

import java.util.Map;

/**
 * Contract for every domain entity stored in a repository.
 * Entities carry a string identifier and know how to convert
 * themselves into a JSON-friendly map. The static helpers make
 * reading loosely typed JSON maps safe and null-free.
 */
public interface Identifiable {

    /** @return the unique identifier of the entity, or null if not yet persisted. */
    String getId();

    /** Assigns an identifier, used when a repository stores a brand new entity. */
    void setId(String id);

    /** @return a map representation suitable for JSON serialization. */
    Map<String, Object> toJson();

    /**
     * Returns the value under the given key as a string.
     * A null value produces an empty string so callers never deal with nulls.
     */
    static String str(Map<String, Object> map, String key) {
        Object value = map.get(key);
        return value == null ? "" : String.valueOf(value);
    }

    /** Returns the value under the given key as a double, defaulting to zero. */
    static double dbl(Map<String, Object> map, String key) {
        Object value = map.get(key);
        if (value instanceof Number number) {
            return number.doubleValue();
        }
        if (value instanceof String text && !text.isBlank()) {
            try {
                return Double.parseDouble(text);
            } catch (NumberFormatException ignored) {
                return 0.0;
            }
        }
        return 0.0;
    }

    /** Returns the value under the given key as an int, defaulting to zero. */
    static int integer(Map<String, Object> map, String key) {
        return (int) Math.round(dbl(map, key));
    }

    /** Returns the value under the given key as a long, defaulting to zero. */
    static long lng(Map<String, Object> map, String key) {
        return Math.round(dbl(map, key));
    }

    /** Returns the value under the given key as a boolean, defaulting to false. */
    static boolean bool(Map<String, Object> map, String key) {
        Object value = map.get(key);
        if (value instanceof Boolean flag) {
            return flag;
        }
        return "true".equalsIgnoreCase(String.valueOf(value));
    }

    /** Returns an id-safe version of a raw string: null when blank. */
    static String idOrNull(String raw) {
        return raw == null || raw.isBlank() ? null : raw;
    }
}
