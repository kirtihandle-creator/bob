package com.shopflow.backend.controller;

import com.shopflow.backend.server.JsonResponse;
import com.shopflow.backend.server.RequestContext;
import com.shopflow.backend.server.Router;
import com.shopflow.backend.service.AuthService;
import com.shopflow.backend.repository.UserRepository;
import com.shopflow.common.json.Json;
import com.shopflow.common.model.Identifiable;
import com.shopflow.common.model.User;

import java.io.IOException;
import java.util.List;
import java.util.Map;

/**
 * Endpoints under /api/auth and /api/users.
 *
 * <pre>
 * POST   /api/auth/login            {username,password} -> {token,user}
 * POST   /api/auth/logout
 * GET    /api/auth/me
 * POST   /api/auth/password         {currentPassword,newPassword}
 * GET    /api/users                 (admin)
 * POST   /api/users                 (admin) {username,password,role,displayName}
 * DELETE /api/users/{id}            (admin)
 * </pre>
 */
public class AuthController {

    private final AuthService authService;
    private final UserRepository users;

    public AuthController(AuthService authService, UserRepository users) {
        this.authService = authService;
        this.users = users;
    }

    public void register(Router router) {
        router.open("POST", "/api/auth/login", this::login);
        router.post("/api/auth/logout", this::logout);
        router.get("/api/auth/me", this::me);
        router.post("/api/auth/password", this::changePassword);
        router.get("/api/users", this::listUsers);
        router.post("/api/users", this::createUser);
        router.delete("/api/users/{id}", this::deleteUser);
    }

    private Object login(RequestContext ctx) throws IOException {
        Map<String, Object> body = ctx.jsonBody();
        return authService.login(
                Identifiable.str(body, "username"),
                Identifiable.str(body, "password"));
    }

    private Object logout(RequestContext ctx) {
        String header = ctx.header("Authorization");
        if (header != null && header.startsWith("Bearer ")) {
            authService.logout(header.substring("Bearer ".length()).trim());
        }
        return JsonResponse.ok("Logged out");
    }

    private Object me(RequestContext ctx) {
        return ctx.user().toPublicJson();
    }

    private Object changePassword(RequestContext ctx) throws IOException {
        Map<String, Object> body = ctx.jsonBody();
        authService.changePassword(ctx.user(),
                Identifiable.str(body, "currentPassword"),
                Identifiable.str(body, "newPassword"));
        return JsonResponse.ok("Password updated");
    }

    private Object listUsers(RequestContext ctx) {
        authService.requireAdmin(ctx.user());
        List<Object> list = Json.toJsonList(users.findAll(), User::toPublicJson);
        return JsonResponse.page(list, list.size(), 0, list.size());
    }

    private Object createUser(RequestContext ctx) throws IOException {
        Map<String, Object> body = ctx.jsonBody();
        User created = authService.register(ctx.user(),
                Identifiable.str(body, "username"),
                Identifiable.str(body, "password"),
                Identifiable.str(body, "role"),
                Identifiable.str(body, "displayName"));
        ctx.setResponseStatus(201);
        return created.toPublicJson();
    }

    private Object deleteUser(RequestContext ctx) {
        authService.deleteUser(ctx.user(), ctx.pathParam("id"));
        ctx.setResponseStatus(204);
        return null;
    }
}
