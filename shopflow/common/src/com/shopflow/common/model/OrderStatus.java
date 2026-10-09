package com.shopflow.common.model;

import java.util.EnumSet;
import java.util.Set;

/**
 * Lifecycle of an order. Transitions are restricted so that, for example,
 * a shipped order cannot be cancelled and a cancelled order is final.
 */
public enum OrderStatus {

    NEW("New"),
    PAID("Paid"),
    SHIPPED("Shipped"),
    DELIVERED("Delivered"),
    CANCELLED("Cancelled");

    private final String label;

    OrderStatus(String label) {
        this.label = label;
    }

    public String getLabel() {
        return label;
    }

    /** @return the set of statuses this one may legally move to. */
    public Set<OrderStatus> allowedTransitions() {
        return switch (this) {
            case NEW -> EnumSet.of(PAID, CANCELLED);
            case PAID -> EnumSet.of(SHIPPED, CANCELLED);
            case SHIPPED -> EnumSet.of(DELIVERED);
            case DELIVERED, CANCELLED -> EnumSet.noneOf(OrderStatus.class);
        };
    }

    public boolean canTransitionTo(OrderStatus target) {
        return allowedTransitions().contains(target);
    }

    /** True when the order still reserves stock and may be cancelled. */
    public boolean isOpen() {
        return this == NEW || this == PAID;
    }

    public boolean isFinal() {
        return allowedTransitions().isEmpty();
    }

    /**
     * Parses a status name leniently; unknown or blank values map to NEW.
     */
    public static OrderStatus parse(String raw) {
        if (raw == null || raw.isBlank()) {
            return NEW;
        }
        for (OrderStatus status : values()) {
            if (status.name().equalsIgnoreCase(raw.trim())
                    || status.label.equalsIgnoreCase(raw.trim())) {
                return status;
            }
        }
        return NEW;
    }

    @Override
    public String toString() {
        return label;
    }
}
