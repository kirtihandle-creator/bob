package com.shopflow.frontend.ui.components;

import com.shopflow.frontend.ui.Theme;

import javax.swing.Box;
import javax.swing.JButton;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.Timer;
import java.awt.FlowLayout;
import java.util.function.Consumer;

/**
 * Creates the standard toolbar used above each list: a debounced search
 * box on the left and action buttons on the right.
 */
public final class ToolbarFactory {

    private static final int DEBOUNCE_MS = 300;

    private ToolbarFactory() {
    }

    /** A toolbar with a search field and arbitrary buttons. */
    public static JPanel create(Consumer<String> onSearch, JButton... buttons) {
        JPanel bar = new JPanel(new FlowLayout(FlowLayout.LEFT, Theme.GAP, Theme.GAP));
        if (onSearch != null) {
            bar.add(searchField(onSearch));
            bar.add(Box.createHorizontalStrut(Theme.GAP));
        }
        for (JButton button : buttons) {
            bar.add(button);
        }
        return bar;
    }

    /** A text field that calls back after the user stops typing briefly. */
    public static JTextField searchField(Consumer<String> onSearch) {
        JTextField field = new JTextField(22);
        field.putClientProperty("JTextField.placeholderText", "Search...");
        field.setToolTipText("Type to filter");
        Timer timer = new Timer(DEBOUNCE_MS, event -> onSearch.accept(field.getText().trim()));
        timer.setRepeats(false);
        field.getDocument().addDocumentListener(new javax.swing.event.DocumentListener() {
            @Override
            public void insertUpdate(javax.swing.event.DocumentEvent e) {
                timer.restart();
            }

            @Override
            public void removeUpdate(javax.swing.event.DocumentEvent e) {
                timer.restart();
            }

            @Override
            public void changedUpdate(javax.swing.event.DocumentEvent e) {
                timer.restart();
            }
        });
        return field;
    }

    public static JButton button(String text, Runnable action) {
        JButton button = new JButton(text);
        button.addActionListener(event -> action.run());
        return button;
    }

    public static JButton primary(String text, Runnable action) {
        JButton button = Theme.primaryButton(text);
        button.addActionListener(event -> action.run());
        return button;
    }

    public static JButton danger(String text, Runnable action) {
        JButton button = Theme.dangerButton(text);
        button.addActionListener(event -> action.run());
        return button;
    }
}
