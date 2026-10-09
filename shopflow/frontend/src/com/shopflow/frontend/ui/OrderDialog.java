package com.shopflow.frontend.ui;

import com.shopflow.common.model.Customer;
import com.shopflow.common.model.Product;
import com.shopflow.common.util.Money;
import com.shopflow.frontend.api.OrderApi;
import com.shopflow.frontend.ui.components.FormBuilder;
import com.shopflow.frontend.util.Dialogs;

import javax.swing.DefaultComboBoxModel;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JDialog;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JSpinner;
import javax.swing.JTable;
import javax.swing.JTextArea;
import javax.swing.SpinnerNumberModel;
import javax.swing.table.DefaultTableModel;
import java.awt.BorderLayout;
import java.awt.FlowLayout;
import java.awt.Window;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/**
 * Dialog for composing a new order: choose a customer, add product lines,
 * review the running total and submit.
 */
public class OrderDialog extends JDialog {

    private static final long serialVersionUID = 1L;

    /** What the caller receives when the user confirms. */
    public record Draft(String customerId, String notes, List<OrderApi.NewLine> lines) {
    }

    private final JComboBox<Customer> customer = new JComboBox<>();
    private final JComboBox<Product> product = new JComboBox<>();
    private final JSpinner quantity = new JSpinner(new SpinnerNumberModel(1, 1, 10_000, 1));
    private final JTextArea notes = new JTextArea(2, 24);
    private final DefaultTableModel linesModel = new DefaultTableModel(
            new Object[]{"Product", "Qty", "Unit price", "Line total"}, 0) {
        private static final long serialVersionUID = 1L;

        @Override
        public boolean isCellEditable(int row, int column) {
            return false;
        }
    };
    private final JTable linesTable = new JTable(linesModel);
    private final JLabel total = Theme.heading("Total: " + Money.format(0));
    private final Map<String, Integer> quantities = new LinkedHashMap<>();
    private final Map<String, Product> productsById = new LinkedHashMap<>();
    private Draft result;

    public OrderDialog(Window owner, List<Customer> customers, List<Product> products) {
        super(owner, "New order", ModalityType.APPLICATION_MODAL);
        customer.setModel(new DefaultComboBoxModel<>(customers.toArray(new Customer[0])));
        List<Product> inStock = new ArrayList<>();
        for (Product candidate : products) {
            if (candidate.getStock() > 0) {
                inStock.add(candidate);
                productsById.put(candidate.getId(), candidate);
            }
        }
        product.setModel(new DefaultComboBoxModel<>(inStock.toArray(new Product[0])));
        buildUi();
        setSize(640, 480);
        setLocationRelativeTo(owner);
    }

    private void buildUi() {
        JPanel lineEntry = new JPanel(new FlowLayout(FlowLayout.LEFT, Theme.GAP, 0));
        lineEntry.add(product);
        lineEntry.add(new JLabel("Qty"));
        lineEntry.add(quantity);
        JButton addLine = new JButton("Add line");
        addLine.addActionListener(event -> addLine());
        lineEntry.add(addLine);
        JButton removeLine = new JButton("Remove selected");
        removeLine.addActionListener(event -> removeSelectedLine());
        lineEntry.add(removeLine);

        JPanel top = new FormBuilder()
                .add("Customer", customer)
                .add("Add product", lineEntry)
                .addTextArea("Notes", notes)
                .build();

        JPanel root = new JPanel(new BorderLayout(0, Theme.GAP));
        root.add(top, BorderLayout.NORTH);
        Theme.styleTable(linesTable);
        linesTable.setAutoCreateRowSorter(false);
        root.add(new JScrollPane(linesTable), BorderLayout.CENTER);

        JPanel footer = new JPanel(new BorderLayout());
        footer.setBorder(Theme.padding(0, Theme.PAD, Theme.PAD, Theme.PAD));
        footer.add(total, BorderLayout.WEST);
        JPanel buttons = new JPanel(new FlowLayout(FlowLayout.RIGHT, Theme.GAP, 0));
        JButton cancel = new JButton("Cancel");
        cancel.addActionListener(event -> dispose());
        JButton place = Theme.primaryButton("Place order");
        place.addActionListener(event -> placeOrder());
        buttons.add(cancel);
        buttons.add(place);
        footer.add(buttons, BorderLayout.EAST);
        root.add(footer, BorderLayout.SOUTH);
        setContentPane(root);
    }

    private void addLine() {
        Product selected = (Product) product.getSelectedItem();
        if (selected == null) {
            Dialogs.warn(this, "No products in stock to add");
            return;
        }
        int qty = (Integer) quantity.getValue();
        int combined = quantities.getOrDefault(selected.getId(), 0) + qty;
        if (combined > selected.getStock()) {
            Dialogs.warn(this, "Only " + selected.getStock() + " of " + selected.getName() + " in stock");
            return;
        }
        quantities.put(selected.getId(), combined);
        rebuildLines();
    }

    private void removeSelectedLine() {
        int row = linesTable.getSelectedRow();
        if (row < 0) {
            return;
        }
        String productId = new ArrayList<>(quantities.keySet()).get(row);
        quantities.remove(productId);
        rebuildLines();
    }

    private void rebuildLines() {
        linesModel.setRowCount(0);
        double sum = 0;
        for (Map.Entry<String, Integer> entry : quantities.entrySet()) {
            Product item = productsById.get(entry.getKey());
            double lineTotal = Money.multiply(item.getPrice(), entry.getValue());
            sum += lineTotal;
            linesModel.addRow(new Object[]{item.getName(), entry.getValue(),
                    Money.format(item.getPrice()), Money.format(lineTotal)});
        }
        total.setText("Total: " + Money.format(sum));
    }

    private void placeOrder() {
        Customer selected = (Customer) customer.getSelectedItem();
        if (selected == null) {
            Dialogs.error(this, "Choose a customer");
            return;
        }
        if (quantities.isEmpty()) {
            Dialogs.error(this, "Add at least one product line");
            return;
        }
        List<OrderApi.NewLine> lines = new ArrayList<>();
        for (Map.Entry<String, Integer> entry : quantities.entrySet()) {
            lines.add(new OrderApi.NewLine(entry.getKey(), entry.getValue()));
        }
        result = new Draft(selected.getId(), notes.getText().trim(), lines);
        dispose();
    }

    public Draft getResult() {
        return result;
    }

    public static Draft show(Window owner, List<Customer> customers, List<Product> products) {
        OrderDialog dialog = new OrderDialog(owner, customers, products);
        dialog.setVisible(true);
        return dialog.getResult();
    }
}
