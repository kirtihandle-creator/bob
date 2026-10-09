package com.shopflow.backend.controller;

import com.shopflow.backend.server.JsonResponse;
import com.shopflow.backend.server.RequestContext;
import com.shopflow.backend.server.Router;
import com.shopflow.backend.service.CustomerService;
import com.shopflow.backend.service.OrderService;
import com.shopflow.common.json.Json;
import com.shopflow.common.model.Customer;
import com.shopflow.common.model.Order;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * Endpoints under /api/customers.
 *
 * <pre>
 * GET    /api/customers?q=
 * GET    /api/customers/{id}
 * GET    /api/customers/{id}/orders
 * POST   /api/customers
 * PUT    /api/customers/{id}
 * DELETE /api/customers/{id}
 * </pre>
 */
public class CustomerController {

    private final CustomerService service;
    private final OrderService orderService;

    public CustomerController(CustomerService service, OrderService orderService) {
        this.service = service;
        this.orderService = orderService;
    }

    public void register(Router router) {
        router.get("/api/customers", this::list);
        router.get("/api/customers/{id}", this::get);
        router.get("/api/customers/{id}/orders", this::orders);
        router.post("/api/customers", this::create);
        router.put("/api/customers/{id}", this::update);
        router.delete("/api/customers/{id}", this::delete);
    }

    private Object list(RequestContext ctx) {
        List<Object> items = new ArrayList<>();
        for (Customer customer : service.list(ctx.query("q", ""))) {
            items.add(service.enrich(customer));
        }
        return JsonResponse.page(items, items.size(), 0, items.size());
    }

    private Object get(RequestContext ctx) {
        return service.enrich(service.get(ctx.pathParam("id")));
    }

    private Object orders(RequestContext ctx) {
        Customer customer = service.get(ctx.pathParam("id"));
        List<Order> history = orderService.list(null, customer.getId());
        List<Object> items = Json.toJsonList(history, Order::toJson);
        return JsonResponse.page(items, items.size(), 0, items.size());
    }

    private Object create(RequestContext ctx) throws IOException {
        Customer created = service.create(ctx.jsonBody());
        ctx.setResponseStatus(201);
        return service.enrich(created);
    }

    private Object update(RequestContext ctx) throws IOException {
        Customer updated = service.update(ctx.pathParam("id"), ctx.jsonBody());
        return service.enrich(updated);
    }

    private Object delete(RequestContext ctx) {
        service.delete(ctx.pathParam("id"));
        ctx.setResponseStatus(204);
        return null;
    }
}
