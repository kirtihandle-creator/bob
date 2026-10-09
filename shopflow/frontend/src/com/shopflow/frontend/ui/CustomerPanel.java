package com.shopflow.frontend.ui;

import com.shopflow.common.model.Customer;
import com.shopflow.common.model.Order;
import com.shopflow.common.util.Dates;
import com.shopflow.common.util.Money;
import com.shopflow.frontend.AppContext;
import com.shopflow.frontend.api.CustomerApi;
import com.shopflow.frontend.ui.components.MoneyRenderer;
import com.shopflow.frontend.ui.components.ToolbarFactory;
import com.shopflow.frontend.ui.table.CustomerTableModel;
import com.shopflow.frontend.util.AsyncTask;
import com.shopflow.frontend.util.Dialogs;

import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.ListSelectionModel;
import javax.swing.SwingUtilities;
import java.awt.BorderLayout;
import java.util.List;
import java.util.function.Supplier;

/**
 * Customer list with search, create/edit/delete and order history.
 */
public class CustomerPanel extends JPanel {

    private static final long serialVersionUID = 1L;

    private final AppContext context;
    private final StatusBar statusBar;
    private final CustomerTableModel model = new CustomerTableModel();
    private final JTable table = new JTable(model);
    private String search = "";

    public CustomerPanel(AppContext context, StatusBar statusBar) {
        super(new BorderLayout());
        this.context = context;
        this.statusBar = statusBar;
        Theme.styleTable(table);
        table.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
        MoneyRenderer.installOn(table);

        JPanel toolbar = ToolbarFactory.create(term -> {
            search = term;
            refresh();
        },
                ToolbarFactory.primary("New", this::create),
                ToolbarFactory.button("Edit", this::edit),
                ToolbarFactory.button("Order history", this::history),
                ToolbarFactory.danger("Delete", this::delete),
                ToolbarFactory.button("Refresh", this::refresh));
        add(toolbar, BorderLayout.NORTH);
        add(new JScrollPane(table), BorderLayout.CENTER);
    }

    public void refresh() {
        statusBar.setBusy(true);
        AsyncTask.run(() -> context.customers().list(search), rows -> {
            model.setRows(rows);
            statusBar.info(rows.size() + " customers");
        }, error -> Dialogs.error(this, "Customers", error), () -> statusBar.setBusy(false));
    }

    private CustomerApi.Row selected() {
        int viewRow = table.getSelectedRow();
        if (viewRow < 0) {
            Dialogs.warn(this, "Select a customer first");
            return null;
        }
        return model.rowAt(table.convertRowIndexToModel(viewRow));
    }

    private void create() {
        Customer draft = CustomerDialog.show(SwingUtilities.getWindowAncestor(this), null);
        if (draft != null) {
            submit(() -> context.customers().create(draft), "Customer created");
        }
    }

    private void edit() {
        CustomerApi.Row row = selected();
        if (row == null) {
            return;
        }
        Customer edited = CustomerDialog.show(SwingUtilities.getWindowAncestor(this), row.customer());
        if (edited != null) {
            submit(() -> context.customers().update(edited), "Customer updated");
        }
    }

    private void history() {
        CustomerApi.Row row = selected();
        if (row == null) {
            return;
        }
        statusBar.setBusy(true);
        AsyncTask.run(() -> context.customers().orders(row.customer().getId()),
                orders -> showHistory(row.customer(), orders),
                error -> Dialogs.error(this, "Order history", error),
                () -> statusBar.setBusy(false));
    }

    private void showHistory(Customer customer, List<Order> orders) {
        if (orders.isEmpty()) {
            Dialogs.info(this, customer.getName() + " has not placed any orders yet.");
            return;
        }
        StringBuilder text = new StringBuilder("Orders for " + customer.getName() + ":\n\n");
        for (Order order : orders) {
            text.append(Dates.formatDate(order.getCreatedAt()))
                    .append("  ").append(order.getStatus().getLabel())
                    .append("  ").append(order.getItemCount()).append(" item(s)")
                    .append("  ").append(Money.format(order.getTotal()))
                    .append('\n');
        }
        Dialogs.info(this, text.toString());
    }

    private void delete() {
        CustomerApi.Row row = selected();
        if (row == null || !Dialogs.confirmDelete(this, "customer \"" + row.customer().getName() + "\"")) {
            return;
        }
        statusBar.setBusy(true);
        AsyncTask.runVoid(() -> context.customers().delete(row.customer().getId()), () -> {
            statusBar.setBusy(false);
            statusBar.success("Customer deleted");
            refresh();
        }, error -> {
            statusBar.setBusy(false);
            Dialogs.error(this, "Delete customer", error);
        });
    }

    private void submit(Supplier<CustomerApi.Row> call, String successMessage) {
        statusBar.setBusy(true);
        AsyncTask.run(call, saved -> {
            statusBar.success(successMessage + ": " + saved.customer().getName());
            refresh();
        }, error -> Dialogs.error(this, "Save customer", error), () -> statusBar.setBusy(false));
    }
}
