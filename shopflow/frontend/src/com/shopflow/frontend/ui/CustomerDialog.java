package com.shopflow.frontend.ui;

import com.shopflow.common.model.Customer;
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
 * Create/edit dialog for a customer.
 */
public class CustomerDialog extends JDialog {

    private static final long serialVersionUID = 1L;

    private final JTextField name = new JTextField(24);
    private final JTextField email = new JTextField(24);
    private final JTextField phone = new JTextField(24);
    private final JTextArea address = new JTextArea(3, 24);
    private final Customer original;
    private Customer result;

    public CustomerDialog(Window owner, Customer existing) {
        super(owner, existing == null ? "New customer" : "Edit customer", ModalityType.APPLICATION_MODAL);
        this.original = existing;
        if (existing != null) {
            name.setText(existing.getName());
            email.setText(existing.getEmail());
            phone.setText(existing.getPhone());
            address.setText(existing.getAddress());
        }
        buildUi();
        pack();
        setLocationRelativeTo(owner);
    }

    private void buildUi() {
        JPanel root = new JPanel(new BorderLayout());
        root.add(new FormBuilder()
                .add("Name", name)
                .add("Email", email)
                .add("Phone", phone)
                .addTextArea("Address", address)
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
                .maxLength(name.getText(), 80, "Name")
                .require(email.getText(), "Email")
                .email(email.getText().trim(), "Email")
                .maxLength(phone.getText(), 30, "Phone")
                .maxLength(address.getText(), 200, "Address");
        if (!validation.isValid()) {
            Dialogs.error(this, validation.getMessage());
            return;
        }
        result = new Customer(original == null ? null : original.getId(),
                name.getText().trim(), email.getText().trim().toLowerCase(),
                phone.getText().trim(), address.getText().trim());
        if (original != null) {
            result.setCreatedAt(original.getCreatedAt());
        }
        dispose();
    }

    public Customer getResult() {
        return result;
    }

    public static Customer show(Window owner, Customer existing) {
        CustomerDialog dialog = new CustomerDialog(owner, existing);
        dialog.setVisible(true);
        return dialog.getResult();
    }
}
