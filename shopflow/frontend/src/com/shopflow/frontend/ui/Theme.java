package com.shopflow.frontend.ui;

import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JComponent;
import javax.swing.JLabel;
import javax.swing.JTable;
import javax.swing.UIManager;
import javax.swing.border.Border;
import java.awt.Color;
import java.awt.Font;

/**
 * Central place for colors, fonts and small styling helpers so every
 * panel looks consistent.
 */
public final class Theme {

    public static final Color PRIMARY = new Color(0x2F6FED);
    public static final Color PRIMARY_DARK = new Color(0x1E4FB5);
    public static final Color DANGER = new Color(0xD64545);
    public static final Color SUCCESS = new Color(0x2E9E5B);
    public static final Color WARNING = new Color(0xE0A100);
    public static final Color MUTED = new Color(0x6B7280);
    public static final Color SURFACE = new Color(0xF7F8FA);
    public static final Color BORDER = new Color(0xDDE1E6);
    public static final Color LOW_STOCK_BG = new Color(0xFFF4E5);

    public static final Font TITLE = new Font(Font.SANS_SERIF, Font.BOLD, 20);
    public static final Font HEADING = new Font(Font.SANS_SERIF, Font.BOLD, 14);
    public static final Font BODY = new Font(Font.SANS_SERIF, Font.PLAIN, 13);
    public static final Font MONO = new Font(Font.MONOSPACED, Font.PLAIN, 12);
    public static final Font STAT = new Font(Font.SANS_SERIF, Font.BOLD, 26);

    public static final int GAP = 8;
    public static final int PAD = 12;

    private Theme() {
    }

    /** Applies the system look and feel, falling back silently. */
    public static void install() {
        try {
            UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
        } catch (Exception ignored) {
            // Default Swing look and feel is acceptable.
        }
        UIManager.put("Table.rowHeight", 24);
        UIManager.put("Button.font", BODY);
        UIManager.put("Label.font", BODY);
        UIManager.put("TextField.font", BODY);
        UIManager.put("Table.font", BODY);
    }

    public static Border padding() {
        return BorderFactory.createEmptyBorder(PAD, PAD, PAD, PAD);
    }

    public static Border padding(int top, int left, int bottom, int right) {
        return BorderFactory.createEmptyBorder(top, left, bottom, right);
    }

    public static Border card() {
        return BorderFactory.createCompoundBorder(
                BorderFactory.createLineBorder(BORDER),
                padding());
    }

    public static JLabel title(String text) {
        JLabel label = new JLabel(text);
        label.setFont(TITLE);
        return label;
    }

    public static JLabel heading(String text) {
        JLabel label = new JLabel(text);
        label.setFont(HEADING);
        return label;
    }

    public static JLabel muted(String text) {
        JLabel label = new JLabel(text);
        label.setForeground(MUTED);
        return label;
    }

    public static JButton primaryButton(String text) {
        JButton button = new JButton(text);
        button.setBackground(PRIMARY);
        button.setForeground(Color.WHITE);
        button.setFocusPainted(false);
        button.setOpaque(true);
        button.setBorderPainted(false);
        return button;
    }

    public static JButton dangerButton(String text) {
        JButton button = new JButton(text);
        button.setForeground(DANGER);
        return button;
    }

    public static void styleTable(JTable table) {
        table.setFillsViewportHeight(true);
        table.setAutoCreateRowSorter(true);
        table.setShowGrid(false);
        table.setIntercellSpacing(new java.awt.Dimension(0, 0));
        table.getTableHeader().setReorderingAllowed(false);
        table.getTableHeader().setFont(HEADING.deriveFont(12f));
    }

    public static void pad(JComponent component) {
        component.setBorder(padding());
    }
}
