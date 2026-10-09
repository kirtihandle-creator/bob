package com.shopflow.frontend.api;

import com.shopflow.common.json.Json;
import com.shopflow.common.model.Identifiable;
import com.shopflow.common.model.User;
import com.shopflow.frontend.session.Session;

import java.util.List;
import java.util.Map;

/**
 * Calls under /api/auth and /api/users.
 */
public class AuthApi {

    private final ApiClient client;
    private final Session session;

    public AuthApi(ApiClient client, Session session) {
        this.client = client;
        this.session = session;
    }

    /** Logs in and stores the token in the session. */
    public User login(String username, String password) {
        Map<String, Object> response = client.post("/api/auth/login",
                Json.map("username", username, "password", password));
        User user = User.fromJson(Json.nested(response, "user"));
        session.login(Identifiable.str(response, "token"), Identifiable.lng(response, "expiresAt"), user);
        return user;
    }

    public void logout() {
        try {
            if (session.isLoggedIn()) {
                client.post("/api/auth/logout", Json.map());
            }
        } catch (ApiException ignored) {
            // The token is dropped locally regardless of what the server says.
        } finally {
            session.logout();
        }
    }

    public User me() {
        return User.fromJson(client.getObject("/api/auth/me"));
    }

    public void changePassword(String currentPassword, String newPassword) {
        client.post("/api/auth/password",
                Json.map("currentPassword", currentPassword, "newPassword", newPassword));
    }

    public List<User> listUsers() {
        return Json.mapList(client.getItems("/api/users"), User::fromJson);
    }

    public User createUser(String username, String password, String role, String displayName) {
        return User.fromJson(client.post("/api/users", Json.map(
                "username", username,
                "password", password,
                "role", role,
                "displayName", displayName)));
    }

    public void deleteUser(String id) {
        client.delete("/api/users/" + id);
    }

    public boolean ping() {
        try {
            client.getObject("/api/health");
            return true;
        } catch (ApiException e) {
            return false;
        }
    }
}
