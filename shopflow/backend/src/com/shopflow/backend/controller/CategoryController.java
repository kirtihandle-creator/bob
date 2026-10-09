package com.shopflow.backend.controller;

import com.shopflow.backend.server.JsonResponse;
import com.shopflow.backend.server.RequestContext;
import com.shopflow.backend.server.Router;
import com.shopflow.backend.service.CategoryService;
import com.shopflow.common.model.Category;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * Endpoints under /api/categories.
 *
 * <pre>
 * GET    /api/categories
 * GET    /api/categories/{id}
 * POST   /api/categories          {name, description}
 * PUT    /api/categories/{id}     {name, description}
 * DELETE /api/categories/{id}
 * </pre>
 */
public class CategoryController {

    private final CategoryService service;

    public CategoryController(CategoryService service) {
        this.service = service;
    }

    public void register(Router router) {
        router.get("/api/categories", this::list);
        router.get("/api/categories/{id}", this::get);
        router.post("/api/categories", this::create);
        router.put("/api/categories/{id}", this::update);
        router.delete("/api/categories/{id}", this::delete);
    }

    private Object list(RequestContext ctx) {
        List<Object> items = new ArrayList<>();
        for (Category category : service.list()) {
            items.add(service.withProductCount(category));
        }
        return JsonResponse.page(items, items.size(), 0, items.size());
    }

    private Object get(RequestContext ctx) {
        return service.withProductCount(service.get(ctx.pathParam("id")));
    }

    private Object create(RequestContext ctx) throws IOException {
        Category created = service.create(ctx.jsonBody());
        ctx.setResponseStatus(201);
        return service.withProductCount(created);
    }

    private Object update(RequestContext ctx) throws IOException {
        Category updated = service.update(ctx.pathParam("id"), ctx.jsonBody());
        return service.withProductCount(updated);
    }

    private Object delete(RequestContext ctx) {
        service.delete(ctx.pathParam("id"));
        ctx.setResponseStatus(204);
        return null;
    }
}
