package com.shopflow.frontend.ui;

import com.shopflow.common.model.Category;
import com.shopflow.common.model.Product;
import com.shopflow.common.util.Money;
import com.shopflow.common.util.Validation;
import com.shopflow.frontend.ui.components.FormBuilder;
import com.shopflow.frontend.util.Dialogs;

import javax.swing.DefaultComboBoxModel;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JDialog;
import javax.swing.JPanel;
import javax.swing.JSpinner;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.SpinnerNumberModel;
import java.awt.BorderLayout;
import java.awt.FlowLayout;
import java.awt.Window;
import java.util.List;

/**
 * Create/edit dialog for a product.
 */
public class ProductDialog extends JDialog {

    private static final long serialVersionUID = 1L;

    private final JTextField name = new JTextField(24);
    private final JTextField sku = new JTextField(24);
    private final JComboBox<Category> category = new JComboBox<>();
    private final JTextField price = new JTextField(24);
    private final JSpinner stock = new JSpinner(new SpinnerNumberModel(0, 0, 1_000_000, 1));
    private final JTextArea description = new JTextArea(3, 24);
    private final Product original;
    private Product result;

    public ProductDialog(Window owner, Product existing, List<Category> categories) {
        super(owner, existing == null ? "New product" : "Edit product", ModalityType.APPLICATION_MODAL);
        this.original = existing;
        category.setModel(new DefaultComboBoxModel<>(categories.toArray(new Category[0])));
        if (existing != null) {
            name.setText(existing.getName());
            sku.setText(existing.getSku());
            price.setText(Money.plain(existing.getPrice()));
            stock.setValue(existing.getStock());
            description.setText(existing.getDescription());
            selectCategory(categories, existing.getCategoryId());
        } else {
            price.setText("0.00");
        }
        buildUi();
        pack();
        setLocationRelativeTo(owner);
    }

    private void selectCategory(List<Category> categories, String categoryId) {
        for (Category candidate : categories) {
            if (candidate.getId().equals(categoryId)) {
                category.setSelectedItem(candidate);
                return;
            }
        }
    }

    private void buildUi() {
        JPanel root = new JPanel(new BorderLayout());
        root.add(new FormBuilder()
                .add("Name", name)
                .add("SKU", sku)
                .add("Category", category)
                .add("Price", price)
                .add("Stock", stock)
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
        double parsedPrice;
        try {
            parsedPrice = Money.parse(price.getText());
        } catch (NumberFormatException e) {
            Dialogs.error(this, "Price must be a number");
            return;
        }
        Category selected = (Category) category.getSelectedItem();
        String normalizedSku = sku.getText().trim().toUpperCase();
        Validation validation = Validation.begin()
                .require(name.getText(), "Name")
                .maxLength(name.getText(), 80, "Name")
                .require(normalizedSku, "SKU")
                .sku(normalizedSku, "SKU")
                .check(selected != null, "Choose a category")
                .nonNegative(parsedPrice, "Price");
        if (!validation.isValid()) {
            Dialogs.error(this, validation.getMessage());
            return;
        }
        result = new Product(original == null ? null : original.getId(),
                name.getText().trim(), normalizedSku, selected.getId(),
                description.getText().trim(), parsedPrice, (Integer) stock.getValue());
        dispose();
    }

    public Product getResult() {
        return result;
    }

    public static Product show(Window owner, Product existing, List<Category> categories) {
        ProductDialog dialog = new ProductDialog(owner, existing, categories);
        dialog.setVisible(true);
        return dialog.getResult();
    }
}
