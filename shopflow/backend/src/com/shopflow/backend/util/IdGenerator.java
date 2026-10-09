package com.shopflow.backend.util;

import java.security.SecureRandom;
import java.util.concurrent.atomic.AtomicLong;

/**
 * Produces short, readable, unique identifiers such as {@code prd-00042-k3f9}.
 * A monotonically increasing counter keeps ids sortable while a random
 * suffix prevents guessing. The counter is seeded from the clock on startup
 * so that restarts never collide with ids created earlier.
 */
public final class IdGenerator {

    private static final String ALPHABET = "abcdefghijklmnopqrstuvwxyz0123456789";
    private static final SecureRandom RANDOM = new SecureRandom();
    private static final AtomicLong COUNTER = new AtomicLong(System.currentTimeMillis() % 100_000);

    private IdGenerator() {
    }

    public static String next(String prefix) {
        long sequence = COUNTER.incrementAndGet();
        return prefix + "-" + String.format("%05d", sequence % 100_000) + "-" + randomSuffix(4);
    }

    public static String token() {
        return randomSuffix(32);
    }

    /**
     * Ensures the counter is above the largest sequence already in use, so
     * that ids loaded from disk and new ids never overlap.
     */
    public static void bumpPast(String existingId) {
        if (existingId == null) {
            return;
        }
        String[] parts = existingId.split("-");
        if (parts.length < 2) {
            return;
        }
        try {
            long sequence = Long.parseLong(parts[1]);
            COUNTER.accumulateAndGet(sequence, Math::max);
        } catch (NumberFormatException ignored) {
            // Not an id produced by this generator; nothing to do.
        }
    }

    private static String randomSuffix(int length) {
        StringBuilder builder = new StringBuilder(length);
        for (int i = 0; i < length; i++) {
            builder.append(ALPHABET.charAt(RANDOM.nextInt(ALPHABET.length())));
        }
        return builder.toString();
    }
}
