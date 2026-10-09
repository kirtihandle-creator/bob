package com.shopflow.backend.server;

import com.shopflow.backend.service.AuthService;
import com.shopflow.common.model.User;
import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;

import java.io.IOException;
import java.io.UncheckedIOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 * Dispatches incoming requests to the first matching {@link Route}.
 * Also enforces bearer-token authentication and converts exceptions
 * into JSON error responses.
 */
public class Router implements HttpHandler {

    private static final Logger LOG = Logger.getLogger(Router.class.getName());

    private final List<Route> routes = new ArrayList<>();
    private final AuthService authService;

    public Router(AuthService authService) {
        this.authService = authService;
    }

    public Router get(String template, RouteHandler handler) {
        return add("GET", template, handler, true);
    }

    public Router post(String template, RouteHandler handler) {
        return add("POST", template, handler, true);
    }

    public Router put(String template, RouteHandler handler) {
        return add("PUT", template, handler, true);
    }

    public Router delete(String template, RouteHandler handler) {
        return add("DELETE", template, handler, true);
    }

    public Router open(String method, String template, RouteHandler handler) {
        return add(method, template, handler, false);
    }

    private Router add(String method, String template, RouteHandler handler, boolean auth) {
        routes.add(new Route(method, template, handler, auth));
        return this;
    }

    public List<Route> getRoutes() {
        return List.copyOf(routes);
    }

    @Override
    public void handle(HttpExchange exchange) throws IOException {
        String method = exchange.getRequestMethod();
        String path = exchange.getRequestURI().getPath();
        long started = System.nanoTime();
        try {
            if ("OPTIONS".equalsIgnoreCase(method)) {
                JsonResponse.sendEmpty(exchange, 204);
                return;
            }
            dispatch(exchange, method, path);
        } catch (ApiException e) {
            JsonResponse.sendError(exchange, e.getStatus(), e.getMessage());
        } catch (IllegalArgumentException e) {
            JsonResponse.sendError(exchange, 400, e.getMessage());
        } catch (UncheckedIOException e) {
            LOG.log(Level.SEVERE, "Persistence failure on " + method + " " + path, e);
            JsonResponse.sendError(exchange, 500, "Data could not be saved: " + e.getMessage());
        } catch (Exception e) {
            LOG.log(Level.SEVERE, "Unhandled error on " + method + " " + path, e);
            JsonResponse.sendError(exchange, 500, "Internal server error");
        } finally {
            long millis = (System.nanoTime() - started) / 1_000_000;
            LOG.info(() -> method + " " + path + " (" + millis + " ms)");
        }
    }

    private void dispatch(HttpExchange exchange, String method, String path) throws IOException {
        boolean pathKnown = false;
        for (Route route : routes) {
            Map<String, String> params = route.match(method, path);
            if (params == null) {
                pathKnown |= route.matchesPath(path);
                continue;
            }
            RequestContext ctx = new RequestContext(exchange, params);
            if (route.requiresAuth()) {
                ctx.setUser(authenticate(ctx));
            }
            Object result = route.getHandler().handle(ctx);
            if (result == null) {
                JsonResponse.sendEmpty(exchange, ctx.responseStatus() == 200 ? 204 : ctx.responseStatus());
            } else {
                JsonResponse.send(exchange, ctx.responseStatus(), result);
            }
            return;
        }
        if (pathKnown) {
            throw new ApiException(405, "Method " + method + " not allowed for " + path);
        }
        throw new ApiException(404, "No route for " + method + " " + path);
    }

    private User authenticate(RequestContext ctx) {
        String header = ctx.header("Authorization");
        if (header == null || !header.startsWith("Bearer ")) {
            throw ApiException.unauthorized("Missing bearer token");
        }
        String token = header.substring("Bearer ".length()).trim();
        return authService.requireUser(token);
    }
}
