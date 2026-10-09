package com.shopflow.backend.service;

import com.shopflow.backend.repository.UserRepository;
import com.shopflow.backend.server.ApiException;
import com.shopflow.backend.util.IdGenerator;
import com.shopflow.backend.util.PasswordHasher;
import com.shopflow.common.json.Json;
import com.shopflow.common.model.User;

import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

/**
 * Handles login, bearer tokens and user administration. Tokens live in
 * memory only and expire after the configured time-to-live.
 */
public class AuthService {

    private record Session(String userId, long expiresAt) {
    }

    private final UserRepository users;
    private final long tokenTtlMillis;
    private final Map<String, Session> sessions = new ConcurrentHashMap<>();

    public AuthService(UserRepository users, long tokenTtlMillis) {
        this.users = users;
        this.tokenTtlMillis = tokenTtlMillis;
    }

    public Map<String, Object> login(String username, String password) {
        User user = users.findByUsername(username)
                .filter(found -> PasswordHasher.verify(password, found.getPasswordHash()))
                .orElseThrow(() -> ApiException.unauthorized("Invalid username or password"));
        String token = IdGenerator.token();
        long expiresAt = System.currentTimeMillis() + tokenTtlMillis;
        sessions.put(token, new Session(user.getId(), expiresAt));
        return Json.map(
                "token", token,
                "expiresAt", expiresAt,
                "user", user.toPublicJson());
    }

    public void logout(String token) {
        if (token != null) {
            sessions.remove(token);
        }
    }

    /** Resolves a token to its user or throws 401. */
    public User requireUser(String token) {
        Session session = sessions.get(token);
        if (session == null) {
            throw ApiException.unauthorized("Invalid or expired token");
        }
        if (session.expiresAt() < System.currentTimeMillis()) {
            sessions.remove(token);
            throw ApiException.unauthorized("Token expired, please log in again");
        }
        return users.findById(session.userId())
                .orElseThrow(() -> ApiException.unauthorized("User no longer exists"));
    }

    public void requireAdmin(User user) {
        if (user == null || !user.isAdmin()) {
            throw ApiException.forbidden("Administrator role required");
        }
    }

    public User register(User actor, String username, String password, String role, String displayName) {
        requireAdmin(actor);
        if (username == null || username.isBlank()) {
            throw ApiException.badRequest("Username is required");
        }
        if (users.usernameTaken(username)) {
            throw ApiException.conflict("Username already taken: " + username);
        }
        String weakness = PasswordHasher.weaknessReason(password);
        if (weakness != null) {
            throw ApiException.badRequest(weakness);
        }
        String resolvedRole = User.ROLE_ADMIN.equalsIgnoreCase(role) ? User.ROLE_ADMIN : User.ROLE_STAFF;
        String name = displayName == null || displayName.isBlank() ? username : displayName;
        return users.save(new User(null, username.trim(), PasswordHasher.hash(password), resolvedRole, name));
    }

    public void changePassword(User actor, String currentPassword, String newPassword) {
        if (!PasswordHasher.verify(currentPassword, actor.getPasswordHash())) {
            throw ApiException.badRequest("Current password is incorrect");
        }
        String weakness = PasswordHasher.weaknessReason(newPassword);
        if (weakness != null) {
            throw ApiException.badRequest(weakness);
        }
        actor.setPasswordHash(PasswordHasher.hash(newPassword));
        users.save(actor);
    }

    public void deleteUser(User actor, String userId) {
        requireAdmin(actor);
        if (actor.getId().equals(userId)) {
            throw ApiException.badRequest("You cannot delete your own account");
        }
        if (!users.delete(userId)) {
            throw ApiException.notFound("User", userId);
        }
        sessions.values().removeIf(session -> session.userId().equals(userId));
    }

    public int activeSessionCount() {
        long now = System.currentTimeMillis();
        sessions.values().removeIf(session -> session.expiresAt() < now);
        return sessions.size();
    }
}
