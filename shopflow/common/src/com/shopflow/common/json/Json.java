package com.shopflow.common.json;

import java.util.ArrayList;
import java.util.Collection;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.function.Function;

/**
 * Convenience facade over {@link JsonParser} and {@link JsonWriter}
 * with helpers to build small response objects and convert lists.
 */
public final class Json {

    private Json() {
    }

    public static String stringify(Object value) {
        return JsonWriter.write(value);
    }

    public static String prettify(Object value) {
        return JsonWriter.pretty(value);
    }

    public static Object parse(String text) {
        return JsonParser.parse(text);
    }

    public static Map<String, Object> object(String text) {
        return JsonParser.parseObject(text);
    }

    public static List<Object> array(String text) {
        return JsonParser.parseArray(text);
    }

    /** Builds a map from alternating key/value arguments. */
    public static Map<String, Object> map(Object... keyValues) {
        if (keyValues.length % 2 != 0) {
            throw new IllegalArgumentException("map() needs an even number of arguments");
        }
        Map<String, Object> result = new LinkedHashMap<>();
        for (int i = 0; i < keyValues.length; i += 2) {
            result.put(String.valueOf(keyValues[i]), keyValues[i + 1]);
        }
        return result;
    }

    /** Converts every map element of a parsed array into a typed object. */
    @SuppressWarnings("unchecked")
    public static <T> List<T> mapList(List<Object> raw, Function<Map<String, Object>, T> mapper) {
        List<T> result = new ArrayList<>();
        if (raw == null) {
            return result;
        }
        for (Object element : raw) {
            if (element instanceof Map<?, ?> map) {
                result.add(mapper.apply((Map<String, Object>) map));
            }
        }
        return result;
    }

    /** Converts every typed object into its JSON map form. */
    public static <T> List<Object> toJsonList(Collection<T> items, Function<T, Map<String, Object>> mapper) {
        List<Object> result = new ArrayList<>();
        for (T item : items) {
            result.add(mapper.apply(item));
        }
        return result;
    }

    /** Reads a nested object, returning an empty map when missing. */
    @SuppressWarnings("unchecked")
    public static Map<String, Object> nested(Map<String, Object> parent, String key) {
        Object value = parent.get(key);
        if (value instanceof Map<?, ?> map) {
            return (Map<String, Object>) map;
        }
        return new LinkedHashMap<>();
    }

    /** Reads a nested array, returning an empty list when missing. */
    @SuppressWarnings("unchecked")
    public static List<Object> nestedList(Map<String, Object> parent, String key) {
        Object value = parent.get(key);
        if (value instanceof List<?> list) {
            return (List<Object>) list;
        }
        return new ArrayList<>();
    }
}
