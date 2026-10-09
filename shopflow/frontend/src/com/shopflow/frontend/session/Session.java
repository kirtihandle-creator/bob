package com.shopflow.frontend.session;

import com.shopflow.common.model.User;

import java.util.List;
import java.util.concurrent.CopyOnWriteArrayList;

/**
 * Holds the logged-in user and bearer token for the desktop client and
 * notifies listeners when the login state changes.
 */
public class Session {

    /** Callback invoked on the Swing thread when login state changes. */
    @FunctionalInterface
    public interface Listener {
        void onSessionChanged(Session session);
    }

    private volatile String token;
    private volatile long expiresAt;
    private volatile User user;
    private final List<Listener> listeners = new CopyOnWriteArrayList<>();

    public boolean isLoggedIn() {
        return token != null && user != null;
    }

    public String getToken() {
        return token;
    }

    public User getUser() {
        return user;
    }

    public long getExpiresAt() {
        return expiresAt;
    }

    public boolean isAdmin() {
        return user != null && user.isAdmin();
    }

    public String displayName() {
        if (user == null) {
            return "Not signed in";
        }
        String name = user.getDisplayName();
        return name == null || name.isBlank() ? user.getUsername() : name;
    }

    public void login(String token, long expiresAt, User user) {
        this.token = token;
        this.expiresAt = expiresAt;
        this.user = user;
        fire();
    }

    public void logout() {
        this.token = null;
        this.expiresAt = 0;
        this.user = null;
        fire();
    }

    public void addListener(Listener listener) {
        listeners.add(listener);
    }

    public void removeListener(Listener listener) {
        listeners.remove(listener);
    }

    private void fire() {
        for (Listener listener : listeners) {
            listener.onSessionChanged(this);
        }
    }
}
