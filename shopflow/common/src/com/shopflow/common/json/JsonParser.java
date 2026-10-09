package com.shopflow.common.json;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/**
 * Minimal recursive-descent JSON parser. Objects become
 * {@code LinkedHashMap<String,Object>}, arrays become {@code List<Object>},
 * numbers become {@code Double}, and the rest map to their natural Java types.
 */
public final class JsonParser {

    private final String text;
    private int pos;

    private JsonParser(String text) {
        this.text = text;
    }

    public static Object parse(String text) {
        if (text == null || text.isBlank()) {
            return null;
        }
        JsonParser parser = new JsonParser(text);
        Object value = parser.readValue();
        parser.skipWhitespace();
        if (parser.pos != text.length()) {
            throw parser.error("Unexpected trailing content");
        }
        return value;
    }

    @SuppressWarnings("unchecked")
    public static Map<String, Object> parseObject(String text) {
        Object value = parse(text);
        if (value instanceof Map<?, ?> map) {
            return (Map<String, Object>) map;
        }
        throw new JsonException("Expected a JSON object");
    }

    @SuppressWarnings("unchecked")
    public static List<Object> parseArray(String text) {
        Object value = parse(text);
        if (value instanceof List<?> list) {
            return (List<Object>) list;
        }
        throw new JsonException("Expected a JSON array");
    }

    private Object readValue() {
        skipWhitespace();
        if (pos >= text.length()) {
            throw error("Unexpected end of input");
        }
        char c = text.charAt(pos);
        return switch (c) {
            case '{' -> readObject();
            case '[' -> readArray();
            case '"' -> readString();
            case 't' -> readLiteral("true", Boolean.TRUE);
            case 'f' -> readLiteral("false", Boolean.FALSE);
            case 'n' -> readLiteral("null", null);
            default -> readNumber();
        };
    }

    private Map<String, Object> readObject() {
        Map<String, Object> map = new LinkedHashMap<>();
        pos++;
        skipWhitespace();
        if (peek() == '}') {
            pos++;
            return map;
        }
        while (true) {
            skipWhitespace();
            if (peek() != '"') {
                throw error("Expected string key");
            }
            String key = readString();
            skipWhitespace();
            expect(':');
            map.put(key, readValue());
            skipWhitespace();
            char next = peek();
            pos++;
            if (next == '}') {
                return map;
            }
            if (next != ',') {
                throw error("Expected ',' or '}'");
            }
        }
    }

    private List<Object> readArray() {
        List<Object> list = new ArrayList<>();
        pos++;
        skipWhitespace();
        if (peek() == ']') {
            pos++;
            return list;
        }
        while (true) {
            list.add(readValue());
            skipWhitespace();
            char next = peek();
            pos++;
            if (next == ']') {
                return list;
            }
            if (next != ',') {
                throw error("Expected ',' or ']'");
            }
        }
    }

    private String readString() {
        StringBuilder builder = new StringBuilder();
        pos++;
        while (pos < text.length()) {
            char c = text.charAt(pos++);
            if (c == '"') {
                return builder.toString();
            }
            if (c != '\\') {
                builder.append(c);
                continue;
            }
            char escaped = text.charAt(pos++);
            switch (escaped) {
                case 'n' -> builder.append('\n');
                case 'r' -> builder.append('\r');
                case 't' -> builder.append('\t');
                case 'b' -> builder.append('\b');
                case 'f' -> builder.append('\f');
                case 'u' -> {
                    builder.append((char) Integer.parseInt(text.substring(pos, pos + 4), 16));
                    pos += 4;
                }
                default -> builder.append(escaped);
            }
        }
        throw error("Unterminated string");
    }

    private Object readLiteral(String literal, Object value) {
        if (!text.startsWith(literal, pos)) {
            throw error("Invalid literal");
        }
        pos += literal.length();
        return value;
    }

    private Double readNumber() {
        int start = pos;
        while (pos < text.length() && "+-0123456789.eE".indexOf(text.charAt(pos)) >= 0) {
            pos++;
        }
        if (start == pos) {
            throw error("Unexpected character '" + text.charAt(pos) + "'");
        }
        try {
            return Double.parseDouble(text.substring(start, pos));
        } catch (NumberFormatException e) {
            throw error("Invalid number");
        }
    }

    private void expect(char expected) {
        if (peek() != expected) {
            throw error("Expected '" + expected + "'");
        }
        pos++;
    }

    private char peek() {
        return pos < text.length() ? text.charAt(pos) : '\0';
    }

    private void skipWhitespace() {
        while (pos < text.length() && Character.isWhitespace(text.charAt(pos))) {
            pos++;
        }
    }

    private JsonException error(String message) {
        return new JsonException(message + " at position " + pos);
    }
}
