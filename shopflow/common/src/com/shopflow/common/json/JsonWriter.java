package com.shopflow.common.json;

import com.shopflow.common.model.Identifiable;

import java.util.Collection;
import java.util.Iterator;
import java.util.Map;

/**
 * Minimal JSON serializer. Supports maps, collections, strings, numbers,
 * booleans, null, enums and any {@link Identifiable} entity.
 * Output is compact; {@link #pretty(Object)} adds indentation for files.
 */
public final class JsonWriter {

    private JsonWriter() {
    }

    public static String write(Object value) {
        StringBuilder builder = new StringBuilder();
        append(builder, value, -1, 0);
        return builder.toString();
    }

    public static String pretty(Object value) {
        StringBuilder builder = new StringBuilder();
        append(builder, value, 2, 0);
        return builder.toString();
    }

    private static void append(StringBuilder out, Object value, int indent, int depth) {
        if (value == null) {
            out.append("null");
        } else if (value instanceof String text) {
            quote(out, text);
        } else if (value instanceof Boolean || value instanceof Integer || value instanceof Long) {
            out.append(value);
        } else if (value instanceof Number number) {
            appendNumber(out, number.doubleValue());
        } else if (value instanceof Enum<?> constant) {
            quote(out, constant.name());
        } else if (value instanceof Identifiable entity) {
            append(out, entity.toJson(), indent, depth);
        } else if (value instanceof Map<?, ?> map) {
            appendMap(out, map, indent, depth);
        } else if (value instanceof Collection<?> collection) {
            appendCollection(out, collection, indent, depth);
        } else {
            quote(out, String.valueOf(value));
        }
    }

    private static void appendNumber(StringBuilder out, double number) {
        if (Double.isNaN(number) || Double.isInfinite(number)) {
            out.append("null");
        } else if (number == Math.rint(number) && Math.abs(number) < 1e15) {
            out.append((long) number);
        } else {
            out.append(number);
        }
    }

    private static void appendMap(StringBuilder out, Map<?, ?> map, int indent, int depth) {
        out.append('{');
        Iterator<? extends Map.Entry<?, ?>> iterator = map.entrySet().iterator();
        while (iterator.hasNext()) {
            Map.Entry<?, ?> entry = iterator.next();
            newline(out, indent, depth + 1);
            quote(out, String.valueOf(entry.getKey()));
            out.append(':');
            if (indent >= 0) {
                out.append(' ');
            }
            append(out, entry.getValue(), indent, depth + 1);
            if (iterator.hasNext()) {
                out.append(',');
            }
        }
        if (!map.isEmpty()) {
            newline(out, indent, depth);
        }
        out.append('}');
    }

    private static void appendCollection(StringBuilder out, Collection<?> items, int indent, int depth) {
        out.append('[');
        Iterator<?> iterator = items.iterator();
        while (iterator.hasNext()) {
            newline(out, indent, depth + 1);
            append(out, iterator.next(), indent, depth + 1);
            if (iterator.hasNext()) {
                out.append(',');
            }
        }
        if (!items.isEmpty()) {
            newline(out, indent, depth);
        }
        out.append(']');
    }

    private static void newline(StringBuilder out, int indent, int depth) {
        if (indent < 0) {
            return;
        }
        out.append('\n');
        out.append(" ".repeat(indent * depth));
    }

    private static void quote(StringBuilder out, String text) {
        out.append('"');
        for (int i = 0; i < text.length(); i++) {
            char c = text.charAt(i);
            switch (c) {
                case '"' -> out.append("\\\"");
                case '\\' -> out.append("\\\\");
                case '\n' -> out.append("\\n");
                case '\r' -> out.append("\\r");
                case '\t' -> out.append("\\t");
                case '\b' -> out.append("\\b");
                case '\f' -> out.append("\\f");
                default -> {
                    if (c < 0x20) {
                        out.append(String.format("\\u%04x", (int) c));
                    } else {
                        out.append(c);
                    }
                }
            }
        }
        out.append('"');
    }
}
