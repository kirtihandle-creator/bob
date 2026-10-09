package com.shopflow.backend.util;

import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.util.Base64;

/**
 * Salted, iterated SHA-256 password hashing. Stored format is
 * {@code iterations$base64salt$base64hash}. This is intentionally
 * dependency-free; for production use prefer PBKDF2, bcrypt or Argon2.
 */
public final class PasswordHasher {

    private static final int DEFAULT_ITERATIONS = 20_000;
    private static final int SALT_BYTES = 16;
    private static final SecureRandom RANDOM = new SecureRandom();

    private PasswordHasher() {
    }

    public static String hash(String password) {
        byte[] salt = new byte[SALT_BYTES];
        RANDOM.nextBytes(salt);
        byte[] digest = digest(password, salt, DEFAULT_ITERATIONS);
        return DEFAULT_ITERATIONS + "$"
                + Base64.getEncoder().encodeToString(salt) + "$"
                + Base64.getEncoder().encodeToString(digest);
    }

    public static boolean verify(String password, String stored) {
        if (password == null || stored == null) {
            return false;
        }
        String[] parts = stored.split("\\$");
        if (parts.length != 3) {
            return false;
        }
        try {
            int iterations = Integer.parseInt(parts[0]);
            byte[] salt = Base64.getDecoder().decode(parts[1]);
            byte[] expected = Base64.getDecoder().decode(parts[2]);
            byte[] actual = digest(password, salt, iterations);
            return MessageDigest.isEqual(expected, actual);
        } catch (IllegalArgumentException e) {
            return false;
        }
    }

    private static byte[] digest(String password, byte[] salt, int iterations) {
        try {
            MessageDigest sha = MessageDigest.getInstance("SHA-256");
            byte[] current = password.getBytes(StandardCharsets.UTF_8);
            for (int i = 0; i < iterations; i++) {
                sha.reset();
                sha.update(salt);
                sha.update(current);
                current = sha.digest();
            }
            return current;
        } catch (NoSuchAlgorithmException e) {
            throw new IllegalStateException("SHA-256 not available", e);
        }
    }

    /** Basic strength rule shared by the register and change-password paths. */
    public static String weaknessReason(String password) {
        if (password == null || password.length() < 6) {
            return "Password must be at least 6 characters";
        }
        boolean hasLetter = password.chars().anyMatch(Character::isLetter);
        boolean hasDigit = password.chars().anyMatch(Character::isDigit);
        if (!hasLetter || !hasDigit) {
            return "Password must contain both letters and digits";
        }
        return null;
    }
}
