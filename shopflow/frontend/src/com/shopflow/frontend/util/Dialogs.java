package com.shopflow.frontend.util;

import com.shopflow.frontend.api.ApiException;

import javax.swing.JOptionPane;
import java.awt.Component;

/**
 * Small wrappers around {@link JOptionPane} so every panel shows errors
 * and confirmations in the same way.
 */
public final class Dialogs {

    private Dialogs() {
    }

    public static void error(Component parent, String title, Throwable error) {
        String message;
        if (error instanceof ApiException api) {
            message = api.userMessage();
        } else if (error == null || error.getMessage() == null) {
            message = String.valueOf(error);
        } else {
            message = error.getMessage();
        }
        JOptionPane.showMessageDialog(parent, wrap(message), title, JOptionPane.ERROR_MESSAGE);
    }

    public static void error(Component parent, String message) {
        JOptionPane.showMessageDialog(parent, wrap(message), "Error", JOptionPane.ERROR_MESSAGE);
    }

    public static void info(Component parent, String message) {
        JOptionPane.showMessageDialog(parent, wrap(message), "Information", JOptionPane.INFORMATION_MESSAGE);
    }

    public static void warn(Component parent, String message) {
        JOptionPane.showMessageDialog(parent, wrap(message), "Warning", JOptionPane.WARNING_MESSAGE);
    }

    public static boolean confirm(Component parent, String title, String message) {
        int choice = JOptionPane.showConfirmDialog(parent, wrap(message), title,
                JOptionPane.YES_NO_OPTION, JOptionPane.QUESTION_MESSAGE);
        return choice == JOptionPane.YES_OPTION;
    }

    public static boolean confirmDelete(Component parent, String what) {
        return confirm(parent, "Delete " + what, "Delete " + what + "? This cannot be undone.");
    }

    public static String prompt(Component parent, String title, String message, String initial) {
        Object result = JOptionPane.showInputDialog(parent, message, title,
                JOptionPane.QUESTION_MESSAGE, null, null, initial);
        return result == null ? null : result.toString();
    }

    /** Wraps long messages in HTML so the dialog does not stretch across the screen. */
    private static String wrap(String message) {
        if (message == null) {
            return "";
        }
        String escaped = message.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;");
        return "<html><body style='width: 360px'>" + escaped.replace("\n", "<br>") + "</body></html>";
    }
}
