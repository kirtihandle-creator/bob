package com.shopflow.frontend.ui.components;

import com.shopflow.frontend.ui.Theme;

import javax.swing.JComponent;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.Insets;

/**
 * Builds a two-column label/field form using {@link GridBagLayout}
 * without repeating constraint boilerplate in every dialog.
 */
public class FormBuilder {

    private final JPanel panel = new JPanel(new GridBagLayout());
    private int row;

    public FormBuilder() {
        panel.setBorder(Theme.padding());
    }

    public FormBuilder add(String label, JComponent field) {
        return add(label, field, 1.0, false);
    }

    /** Adds a field; {@code grow} lets it take vertical space (text areas). */
    public FormBuilder add(String label, JComponent field, double weightX, boolean grow) {
        GridBagConstraints labelConstraints = new GridBagConstraints();
        labelConstraints.gridx = 0;
        labelConstraints.gridy = row;
        labelConstraints.anchor = GridBagConstraints.NORTHEAST;
        labelConstraints.insets = new Insets(4, 0, 4, Theme.GAP);
        JLabel jLabel = new JLabel(label);
        panel.add(jLabel, labelConstraints);

        GridBagConstraints fieldConstraints = new GridBagConstraints();
        fieldConstraints.gridx = 1;
        fieldConstraints.gridy = row;
        fieldConstraints.weightx = weightX;
        fieldConstraints.weighty = grow ? 1.0 : 0.0;
        fieldConstraints.fill = grow ? GridBagConstraints.BOTH : GridBagConstraints.HORIZONTAL;
        fieldConstraints.insets = new Insets(4, 0, 4, 0);
        panel.add(field, fieldConstraints);
        row++;
        return this;
    }

    public FormBuilder addTextArea(String label, JTextArea area) {
        area.setLineWrap(true);
        area.setWrapStyleWord(true);
        JScrollPane scroll = new JScrollPane(area);
        scroll.setPreferredSize(new java.awt.Dimension(280, 70));
        return add(label, scroll, 1.0, true);
    }

    /** Adds a full-width component spanning both columns. */
    public FormBuilder addFullWidth(JComponent component) {
        GridBagConstraints constraints = new GridBagConstraints();
        constraints.gridx = 0;
        constraints.gridy = row;
        constraints.gridwidth = 2;
        constraints.weightx = 1.0;
        constraints.fill = GridBagConstraints.HORIZONTAL;
        constraints.insets = new Insets(4, 0, 4, 0);
        panel.add(component, constraints);
        row++;
        return this;
    }

    public JPanel build() {
        return panel;
    }
}
