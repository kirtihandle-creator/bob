package com.shopflow.backend.controller;

import com.shopflow.backend.server.ApiException;
import com.shopflow.backend.server.JsonResponse;
import com.shopflow.backend.server.RequestContext;
import com.shopflow.backend.server.Router;
import com.shopflow.backend.service.OrderService;
import com.shopflow.common.json.Json;
import com.shopflow.common.model.Identifiable;
import com.shopflow.common.model.Order;
import com.shopflow.common.model.OrderStatus;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

/**
 * Endpoints under /api/orders.
 *
 * <pre>
 * GET    /api/orders?status=&customer=
 * GET    /api/orders/{id}
 * GET    /api/orders/statuses
 * POST   /api/orders                  {customerId, notes, items:[{productId, quantity}]}
 * POST   /api/orders/{id}/status      {status: "PAID"}
 * DELETE /api/orders/{id}             (admin only)
 * </pre>
 */
public class OrderController {

    private final OrderService service;

    public OrderController(OrderService service) {
        this.service = service;
    }

    public void register(Router router) {
        router.get("/api/orders/statuses", this::statuses);
        router.get("/api/orders", this::list);
        router.get("/api/orders/{id}", this::get);
        router.post("/api/orders", this::create);
        router.post("/api/orders/{id}/status", this::changeStatus);
        router.delete("/api/orders/{id}", this::delete);
    }

    private Object statuses(RequestContext ctx) {
        List<Object> items = new ArrayList<>();
        for (OrderStatus status : OrderStatus.values()) {
            List<String> next = new ArrayList<>();
            for (OrderStatus target : status.allowedTransitions()) {
                next.add(target.name());
            }
            items.add(Json.map("name", status.name(), "label", status.getLabel(), "next", next));
        }
        return Json.map("items", items);
    }

    private Object list(RequestContext ctx) {
        List<Order> orders = service.list(ctx.query("status", ""), ctx.query("customer", ""));
        List<Object> items = Json.toJsonList(orders, Order::toJson);
        return JsonResponse.page(items, items.size(), 0, items.size());
    }

    private Object get(RequestContext ctx) {
        return service.get(ctx.pathParam("id")).toJson();
    }

    private Object create(RequestContext ctx) throws IOException {
        Order created = service.create(ctx.jsonBody());
        ctx.setResponseStatus(201);
        return created.toJson();
    }

    private Object changeStatus(RequestContext ctx) throws IOException {
        Map<String, Object> body = ctx.jsonBody();
        String status = Identifiable.str(body, "status");
        if (status.isBlank()) {
            throw ApiException.badRequest("Body must contain 'status'");
        }
        return service.changeStatus(ctx.pathParam("id"), status).toJson();
    }

    private Object delete(RequestContext ctx) {
        if (!ctx.user().isAdmin()) {
            throw ApiException.forbidden("Only administrators can delete orders");
        }
        service.delete(ctx.pathParam("id"));
        ctx.setResponseStatus(204);
        return null;
    }
}
