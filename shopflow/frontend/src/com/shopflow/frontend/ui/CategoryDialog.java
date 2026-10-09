package com.shopflow.frontend.ui;

import com.shopflow.common.model.Category;
import com.shopflow.common.util.Validation;
import com.shopflow.frontend.ui.components.FormBuilder;
import com.shopflow.frontend.util.Dialogs;

import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JPanel;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import java.awt.BorderLayout;
import java.awt.FlowLayout;
import java.awt.Window;

/**
 * Create/edit dialog for a category. Returns the edited entity through
 * {@link #getResult()} or null when cancelled.
 */
public class CategoryDialog extends JDialog {

    private static final long serialVersionUID = 1L;

    private final JTextField name = new JTextField(24);
    private final JTextArea description = new JTextArea(3, 24);
    private final Category original;
    private Category result;

    public CategoryDialog(Window owner, Category existing) {
        super(owner, existing == null ? "New category" : "Edit category", ModalityType.APPLICATION_MODAL);
        this.original = existing;
        if (existing != null) {
            name.setText(existing.getName());
            description.setText(existing.getDescription());
        }
        buildUi();
        pack();
        setLocationRelativeTo(owner);
    }

    private void buildUi() {
        JPanel root = new JPanel(new BorderLayout());
        root.add(new FormBuilder()
                .add("Name", name)
                .addTextArea("Description", description)
                .build(), BorderLayout.CENTER);

        JPanel buttons = new JPanel(new FlowLayout(FlowLayout.RIGHT, Theme.GAP, Theme.GAP));
        JButton cancel = new JButton("Cancel");
        cancel.addActionListener(event -> dispose());
        JButton save = Theme.primaryButton("Save");
        save.addActionListener(event -> save());
        buttons.add(cancel);
        buttons.add(save);
        root.add(buttons, BorderLayout.SOUTH);
        getRootPane().setDefaultButton(save);
        setContentPane(root);
    }

    private void save() {
        Validation validation = Validation.begin()
                .require(name.getText(), "Name")
                .maxLength(name.getText(), 60, "Name")
                .maxLength(description.getText(), 250, "Description");
        if (!validation.isValid()) {
            Dialogs.error(this, validation.getMessage());
            return;
        }
        result = new Category(original == null ? null : original.getId(),
                name.getText().trim(), description.getText().trim());
        dispose();
    }

    public Category getResult() {
        return result;
    }

    /** Convenience: show and return the result in one call. */
    public static Category show(Window owner, Category existing) {
        CategoryDialog dialog = new CategoryDialog(owner, existing);
        dialog.setVisible(true);
        return dialog.getResult();
    }
}
