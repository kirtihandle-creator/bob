package com.shopflow.backend.repository;

import com.shopflow.common.model.User;

import java.util.Map;
import java.util.Optional;

/**
 * Store for {@link User} accounts, keyed by id with username lookup.
 */
public class UserRepository extends InMemoryRepository<User> {

    public UserRepository() {
        super("usr");
    }

    @Override
    public String getName() {
        return "users";
    }

    @Override
    public User fromJson(Map<String, Object> map) {
        return User.fromJson(map);
    }

    public Optional<User> findByUsername(String username) {
        if (username == null || username.isBlank()) {
            return Optional.empty();
        }
        return findFirst(user -> username.trim().equalsIgnoreCase(user.getUsername()));
    }

    public boolean usernameTaken(String username) {
        return findByUsername(username).isPresent();
    }

    public long countAdmins() {
        return findAll().stream().filter(User::isAdmin).count();
    }
}
