package com.shopflow.backend.controller;

import com.shopflow.backend.server.ApiException;
import com.shopflow.backend.server.JsonResponse;
import com.shopflow.backend.server.RequestContext;
import com.shopflow.backend.server.Router;
import com.shopflow.backend.service.ProductService;
import com.shopflow.common.model.Identifiable;
import com.shopflow.common.model.Product;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

/**
 * Endpoints under /api/products.
 *
 * <pre>
 * GET    /api/products?q=&category=&lowStock=&offset=&limit=
 * GET    /api/products/{id}
 * POST   /api/products
 * PUT    /api/products/{id}
 * POST   /api/products/{id}/stock     {delta: -3}
 * DELETE /api/products/{id}
 * </pre>
 */
public class ProductController {

    private final ProductService service;

    public ProductController(ProductService service) {
        this.service = service;
    }

    public void register(Router router) {
        router.get("/api/products", this::list);
        router.get("/api/products/{id}", this::get);
        router.post("/api/products", this::create);
        router.put("/api/products/{id}", this::update);
        router.post("/api/products/{id}/stock", this::adjustStock);
        router.delete("/api/products/{id}", this::delete);
    }

    private Object list(RequestContext ctx) {
        String search = ctx.query("q", "");
        String category = ctx.query("category", "");
        boolean lowStock = "true".equalsIgnoreCase(ctx.query("lowStock", "false"));
        int offset = Math.max(0, ctx.queryInt("offset", 0));
        int limit = Math.max(1, Math.min(500, ctx.queryInt("limit", 200)));

        List<Product> all = service.list(search, category, lowStock);
        List<Object> items = new ArrayList<>();
        for (int i = offset; i < all.size() && items.size() < limit; i++) {
            items.add(service.enrich(all.get(i)));
        }
        return JsonResponse.page(items, all.size(), offset, limit);
    }

    private Object get(RequestContext ctx) {
        return service.enrich(service.get(ctx.pathParam("id")));
    }

    private Object create(RequestContext ctx) throws IOException {
        Product created = service.create(ctx.jsonBody());
        ctx.setResponseStatus(201);
        return service.enrich(created);
    }

    private Object update(RequestContext ctx) throws IOException {
        Product updated = service.update(ctx.pathParam("id"), ctx.jsonBody());
        return service.enrich(updated);
    }

    private Object adjustStock(RequestContext ctx) throws IOException {
        Map<String, Object> body = ctx.jsonBody();
        if (!body.containsKey("delta")) {
            throw ApiException.badRequest("Body must contain a numeric 'delta'");
        }
        int delta = Identifiable.integer(body, "delta");
        return service.enrich(service.adjustStock(ctx.pathParam("id"), delta));
    }

    private Object delete(RequestContext ctx) {
        service.delete(ctx.pathParam("id"));
        ctx.setResponseStatus(204);
        return null;
    }
}
