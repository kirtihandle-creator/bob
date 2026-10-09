package com.shopflow.backend.server;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * A registered route: HTTP method plus a path template such as
 * {@code /api/products/{id}}. Templates are compiled to regular
 * expressions so that path variables can be extracted on match.
 */
public class Route {

    private static final Pattern VARIABLE = Pattern.compile("\\{(\\w+)}");

    private final String method;
    private final String template;
    private final Pattern pattern;
    private final List<String> variableNames = new ArrayList<>();
    private final RouteHandler handler;
    private final boolean requiresAuth;

    public Route(String method, String template, RouteHandler handler, boolean requiresAuth) {
        this.method = method.toUpperCase();
        this.template = template;
        this.handler = handler;
        this.requiresAuth = requiresAuth;
        this.pattern = compile(template);
    }

    private Pattern compile(String template) {
        StringBuilder regex = new StringBuilder("^");
        Matcher matcher = VARIABLE.matcher(template);
        int last = 0;
        while (matcher.find()) {
            regex.append(Pattern.quote(template.substring(last, matcher.start())));
            regex.append("([^/]+)");
            variableNames.add(matcher.group(1));
            last = matcher.end();
        }
        regex.append(Pattern.quote(template.substring(last)));
        regex.append("/?$");
        return Pattern.compile(regex.toString());
    }

    public String getMethod() {
        return method;
    }

    public String getTemplate() {
        return template;
    }

    public RouteHandler getHandler() {
        return handler;
    }

    public boolean requiresAuth() {
        return requiresAuth;
    }

    /** True when the path (ignoring method) matches this template. */
    public boolean matchesPath(String path) {
        return pattern.matcher(path).matches();
    }

    /**
     * Attempts to match method and path, returning the extracted variables
     * or {@code null} when there is no match.
     */
    public Map<String, String> match(String requestMethod, String path) {
        if (!method.equalsIgnoreCase(requestMethod)) {
            return null;
        }
        Matcher matcher = pattern.matcher(path);
        if (!matcher.matches()) {
            return null;
        }
        Map<String, String> values = new LinkedHashMap<>();
        for (int i = 0; i < variableNames.size(); i++) {
            values.put(variableNames.get(i), matcher.group(i + 1));
        }
        return values;
    }

    @Override
    public String toString() {
        return method + " " + template;
    }
}
