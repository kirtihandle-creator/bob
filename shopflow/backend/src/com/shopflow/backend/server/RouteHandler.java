package com.shopflow.backend.server;

import java.io.IOException;

/**
 * A single endpoint implementation. The returned object is serialized
 * to JSON; return {@code null} to send an empty body (204 by default,
 * or whatever status was set on the context).
 */
@FunctionalInterface
public interface RouteHandler {

    Object handle(RequestContext ctx) throws IOException;
}
