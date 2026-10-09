package com.shopflow.frontend.ui;

import com.shopflow.common.model.Category;
import com.shopflow.common.model.Product;
import com.shopflow.frontend.AppContext;
import com.shopflow.frontend.api.ProductApi;
import com.shopflow.frontend.ui.components.MoneyRenderer;
import com.shopflow.frontend.ui.components.ToolbarFactory;
import com.shopflow.frontend.ui.table.ProductTableModel;
import com.shopflow.frontend.util.AsyncTask;
import com.shopflow.frontend.util.Dialogs;

import javax.swing.JCheckBox;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.ListSelectionModel;
import javax.swing.SwingUtilities;
import javax.swing.table.DefaultTableCellRenderer;
import java.awt.BorderLayout;
import java.awt.Component;
import java.util.List;
import java.util.function.Supplier;

/**
 * Product list with search, low-stock filter, create/edit/delete and
 * quick stock adjustment.
 */
public class ProductPanel extends JPanel {

    private static final long serialVersionUID = 1L;

    private final AppContext context;
    private final StatusBar statusBar;
    private final ProductTableModel model = new ProductTableModel();
    private final JTable table = new JTable(model);
    private final JCheckBox lowStockOnly = new JCheckBox("Low stock only");
    private String search = "";

    public ProductPanel(AppContext context, StatusBar statusBar) {
        super(new BorderLayout());
        this.context = context;
        this.statusBar = statusBar;
        Theme.styleTable(table);
        table.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
        MoneyRenderer.installOn(table);
        table.setDefaultRenderer(String.class, new LowStockRenderer());
        lowStockOnly.addActionListener(event -> refresh());

        JPanel toolbar = ToolbarFactory.create(term -> {
            search = term;
            refresh();
        },
                ToolbarFactory.primary("New", this::create),
                ToolbarFactory.button("Edit", this::edit),
                ToolbarFactory.button("Adjust stock", this::adjustStock),
                ToolbarFactory.danger("Delete", this::delete),
                ToolbarFactory.button("Refresh", this::refresh));
        toolbar.add(lowStockOnly);
        add(toolbar, BorderLayout.NORTH);
        add(new JScrollPane(table), BorderLayout.CENTER);
    }

    public void refresh() {
        statusBar.setBusy(true);
        AsyncTask.run(() -> context.products().list(search, "", lowStockOnly.isSelected()), rows -> {
            model.setRows(rows);
            statusBar.info(rows.size() + " products");
        }, error -> Dialogs.error(this, "Products", error), () -> statusBar.setBusy(false));
    }

    private Product selected() {
        int viewRow = table.getSelectedRow();
        if (viewRow < 0) {
            Dialogs.warn(this, "Select a product first");
            return null;
        }
        return model.productAt(table.convertRowIndexToModel(viewRow));
    }

    private void withCategories(java.util.function.Consumer<List<Category>> then) {
        statusBar.setBusy(true);
        AsyncTask.run(context.categories()::list, categories -> {
            if (categories.isEmpty()) {
                Dialogs.warn(this, "Create a category before adding products");
                return;
            }
            then.accept(categories);
        }, error -> Dialogs.error(this, "Categories", error), () -> statusBar.setBusy(false));
    }

    private void create() {
        withCategories(categories -> {
            Product draft = ProductDialog.show(SwingUtilities.getWindowAncestor(this), null, categories);
            if (draft != null) {
                submit(() -> context.products().create(draft), "Product created");
            }
        });
    }

    private void edit() {
        Product product = selected();
        if (product == null) {
            return;
        }
        withCategories(categories -> {
            Product edited = ProductDialog.show(SwingUtilities.getWindowAncestor(this), product, categories);
            if (edited != null) {
                submit(() -> context.products().update(edited), "Product updated");
            }
        });
    }

    private void adjustStock() {
        Product product = selected();
        if (product == null) {
            return;
        }
        String input = Dialogs.prompt(this, "Adjust stock",
                product.getName() + " has " + product.getStock() + " units. Enter a change (e.g. 5 or -2):", "0");
        if (input == null) {
            return;
        }
        int delta;
        try {
            delta = Integer.parseInt(input.trim());
        } catch (NumberFormatException e) {
            Dialogs.error(this, "Enter a whole number");
            return;
        }
        if (delta != 0) {
            submit(() -> context.products().adjustStock(product.getId(), delta), "Stock adjusted");
        }
    }

    private void delete() {
        Product product = selected();
        if (product == null || !Dialogs.confirmDelete(this, "product \"" + product.getName() + "\"")) {
            return;
        }
        statusBar.setBusy(true);
        AsyncTask.runVoid(() -> context.products().delete(product.getId()), () -> {
            statusBar.setBusy(false);
            statusBar.success("Product deleted");
            refresh();
        }, error -> {
            statusBar.setBusy(false);
            Dialogs.error(this, "Delete product", error);
        });
    }

    private void submit(Supplier<ProductApi.Row> call, String successMessage) {
        statusBar.setBusy(true);
        AsyncTask.run(call, saved -> {
            statusBar.success(successMessage + ": " + saved.product().getName());
            refresh();
        }, error -> Dialogs.error(this, "Save product", error), () -> statusBar.setBusy(false));
    }

    /** Highlights rows whose product is low on stock. */
    private class LowStockRenderer extends DefaultTableCellRenderer {
        private static final long serialVersionUID = 1L;

        @Override
        public Component getTableCellRendererComponent(JTable tbl, Object value, boolean isSelected,
                                                       boolean hasFocus, int row, int column) {
            Component component = super.getTableCellRendererComponent(tbl, value, isSelected, hasFocus, row, column);
            Product product = model.productAt(tbl.convertRowIndexToModel(row));
            if (!isSelected) {
                component.setBackground(product.isLowStock() ? Theme.LOW_STOCK_BG : tbl.getBackground());
            }
            return component;
        }
    }
}
