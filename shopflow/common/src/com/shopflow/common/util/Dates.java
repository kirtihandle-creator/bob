package com.shopflow.common.util;

import java.time.Instant;
import java.time.LocalDate;
import java.time.ZoneId;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;

/**
 * Formatting helpers for epoch-millisecond timestamps used across the app.
 */
public final class Dates {

    private static final DateTimeFormatter DATE_TIME = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm");
    private static final DateTimeFormatter DATE_ONLY = DateTimeFormatter.ofPattern("yyyy-MM-dd");

    private Dates() {
    }

    public static long now() {
        return System.currentTimeMillis();
    }

    public static ZonedDateTime toZoned(long epochMillis) {
        return Instant.ofEpochMilli(epochMillis).atZone(ZoneId.systemDefault());
    }

    /** Formats as "2026-10-09 14:30" in the local time zone. */
    public static String formatDateTime(long epochMillis) {
        if (epochMillis <= 0) {
            return "";
        }
        return DATE_TIME.format(toZoned(epochMillis));
    }

    /** Formats as "2026-10-09" in the local time zone. */
    public static String formatDate(long epochMillis) {
        if (epochMillis <= 0) {
            return "";
        }
        return DATE_ONLY.format(toZoned(epochMillis));
    }

    /** Local calendar date of a timestamp, used for grouping daily totals. */
    public static LocalDate toLocalDate(long epochMillis) {
        return toZoned(epochMillis).toLocalDate();
    }

    /** Timestamp for midnight at the start of N days ago. */
    public static long startOfDaysAgo(int days) {
        return LocalDate.now().minusDays(days)
                .atStartOfDay(ZoneId.systemDefault())
                .toInstant()
                .toEpochMilli();
    }

    /** Human friendly relative string such as "3 minutes ago". */
    public static String relative(long epochMillis) {
        long diff = now() - epochMillis;
        if (diff < 0) {
            return "just now";
        }
        long seconds = diff / 1000;
        if (seconds < 60) {
            return "just now";
        }
        long minutes = seconds / 60;
        if (minutes < 60) {
            return minutes + (minutes == 1 ? " minute ago" : " minutes ago");
        }
        long hours = minutes / 60;
        if (hours < 24) {
            return hours + (hours == 1 ? " hour ago" : " hours ago");
        }
        long days = hours / 24;
        return days + (days == 1 ? " day ago" : " days ago");
    }
}
