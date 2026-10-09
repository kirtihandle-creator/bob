package com.shopflow.common.util;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.text.NumberFormat;
import java.util.Locale;

/**
 * Formatting and rounding helpers for currency values.
 * Monetary math inside the app uses doubles for simplicity, so every
 * value is rounded to two decimals before display or persistence.
 */
public final class Money {

    private static final NumberFormat CURRENCY = NumberFormat.getCurrencyInstance(Locale.US);
    private static final NumberFormat PLAIN = NumberFormat.getNumberInstance(Locale.US);

    static {
        PLAIN.setMinimumFractionDigits(2);
        PLAIN.setMaximumFractionDigits(2);
    }

    private Money() {
    }

    /** Rounds to two decimal places using HALF_UP. */
    public static double round(double value) {
        return BigDecimal.valueOf(value).setScale(2, RoundingMode.HALF_UP).doubleValue();
    }

    /** Formats with a currency symbol, e.g. "$1,234.50". */
    public static String format(double value) {
        synchronized (CURRENCY) {
            return CURRENCY.format(round(value));
        }
    }

    /** Formats without a symbol, e.g. "1,234.50". */
    public static String plain(double value) {
        synchronized (PLAIN) {
            return PLAIN.format(round(value));
        }
    }

    /**
     * Parses user input such as "$1,234.50" or "1234.5".
     *
     * @throws NumberFormatException when the text has no numeric content
     */
    public static double parse(String text) {
        if (text == null) {
            throw new NumberFormatException("empty");
        }
        String cleaned = text.replace("$", "").replace(",", "").trim();
        if (cleaned.isEmpty()) {
            throw new NumberFormatException("empty");
        }
        return round(Double.parseDouble(cleaned));
    }

    /** Multiplies and rounds, convenient for line totals. */
    public static double multiply(double unitPrice, int quantity) {
        return round(unitPrice * quantity);
    }

    /** Applies a percentage, e.g. tax or discount. */
    public static double percentOf(double value, double percent) {
        return round(value * percent / 100.0);
    }
}
