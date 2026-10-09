package com.shopflow.frontend.ui;

import com.shopflow.common.model.Customer;
import com.shopflow.common.model.Order;
import com.shopflow.common.model.OrderItem;
import com.shopflow.common.model.OrderStatus;
import com.shopflow.common.model.Product;
import com.shopflow.common.util.Dates;
import com.shopflow.common.util.Money;
import com.shopflow.frontend.AppContext;
import com.shopflow.frontend.ui.components.MoneyRenderer;
import com.shopflow.frontend.ui.components.ToolbarFactory;
import com.shopflow.frontend.ui.table.OrderTableModel;
import com.shopflow.frontend.util.AsyncTask;
import com.shopflow.frontend.util.Dialogs;

import javax.swing.JComboBox;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.ListSelectionModel;
import javax.swing.SwingUtilities;
import java.awt.BorderLayout;
import java.util.List;
import java.util.Set;

/**
 * Order list with status filter, order creation, status transitions,
 * detail view and (for administrators) deletion.
 */
public class OrderPanel extends JPanel {

    private static final long serialVersionUID = 1L;
    private static final String ALL = "All statuses";

    private final AppContext context;
    private final StatusBar statusBar;
    private final OrderTableModel model = new OrderTableModel();
    private final JTable table = new JTable(model);
    private final JComboBox<Object> statusFilter = new JComboBox<>();

    public OrderPanel(AppContext context, StatusBar statusBar) {
        super(new BorderLayout());
        this.context = context;
        this.statusBar = statusBar;
        Theme.styleTable(table);
        table.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
        MoneyRenderer.installOn(table);

        statusFilter.addItem(ALL);
        for (OrderStatus status : OrderStatus.values()) {
            statusFilter.addItem(status);
        }
        statusFilter.addActionListener(event -> refresh());

        JPanel toolbar = ToolbarFactory.create(null,
                ToolbarFactory.primary("New order", this::create),
                ToolbarFactory.button("Details", this::details),
                ToolbarFactory.button("Change status", this::changeStatus),
                ToolbarFactory.danger("Delete", this::delete),
                ToolbarFactory.button("Refresh", this::refresh));
        toolbar.add(statusFilter);
        add(toolbar, BorderLayout.NORTH);
        add(new JScrollPane(table), BorderLayout.CENTER);
    }

    public void refresh() {
        Object selected = statusFilter.getSelectedItem();
        OrderStatus status = selected instanceof OrderStatus value ? value : null;
        statusBar.setBusy(true);
        AsyncTask.run(() -> context.orders().list(status), orders -> {
            model.setOrders(orders);
            statusBar.info(orders.size() + " orders");
        }, error -> Dialogs.error(this, "Orders", error), () -> statusBar.setBusy(false));
    }

    private Order selected() {
        int viewRow = table.getSelectedRow();
        if (viewRow < 0) {
            Dialogs.warn(this, "Select an order first");
            return null;
        }
        return model.orderAt(table.convertRowIndexToModel(viewRow));
    }

    private void create() {
        statusBar.setBusy(true);
        AsyncTask.run(() -> {
            List<Customer> customers = context.customers().listAll();
            List<Product> products = context.products().listAll();
            return new Object[]{customers, products};
        }, loaded -> {
            @SuppressWarnings("unchecked") List<Customer> customers = (List<Customer>) loaded[0];
            @SuppressWarnings("unchecked") List<Product> products = (List<Product>) loaded[1];
            if (customers.isEmpty() || products.isEmpty()) {
                Dialogs.warn(this, "You need at least one customer and one product first");
                return;
            }
            OrderDialog.Draft draft = OrderDialog.show(SwingUtilities.getWindowAncestor(this), customers, products);
            if (draft != null) {
                place(draft);
            }
        }, error -> Dialogs.error(this, "New order", error), () -> statusBar.setBusy(false));
    }

    private void place(OrderDialog.Draft draft) {
        statusBar.setBusy(true);
        AsyncTask.run(() -> context.orders().create(draft.customerId(), draft.notes(), draft.lines()), order -> {
            statusBar.success("Order " + order.getId() + " placed for " + Money.format(order.getTotal()));
            refresh();
        }, error -> Dialogs.error(this, "Place order", error), () -> statusBar.setBusy(false));
    }

    private void details() {
        Order order = selected();
        if (order == null) {
            return;
        }
        StringBuilder text = new StringBuilder();
        text.append("Order ").append(order.getId()).append('\n')
                .append("Customer: ").append(order.getCustomerName()).append('\n')
                .append("Status: ").append(order.getStatus().getLabel()).append('\n')
                .append("Created: ").append(Dates.formatDateTime(order.getCreatedAt())).append('\n');
        if (!order.getNotes().isBlank()) {
            text.append("Notes: ").append(order.getNotes()).append('\n');
        }
        text.append('\n');
        for (OrderItem item : order.getItems()) {
            text.append(item.getQuantity()).append(" x ").append(item.getProductName())
                    .append(" @ ").append(Money.format(item.getUnitPrice()))
                    .append(" = ").append(Money.format(item.getLineTotal())).append('\n');
        }
        text.append("\nTotal: ").append(Money.format(order.getTotal()));
        Dialogs.info(this, text.toString());
    }

    private void changeStatus() {
        Order order = selected();
        if (order == null) {
            return;
        }
        Set<OrderStatus> allowed = order.getStatus().allowedTransitions();
        if (allowed.isEmpty()) {
            Dialogs.info(this, "Order is " + order.getStatus().getLabel() + " and cannot change further");
            return;
        }
        Object choice = javax.swing.JOptionPane.showInputDialog(this,
                "Move order " + order.getId() + " from " + order.getStatus().getLabel() + " to:",
                "Change status", javax.swing.JOptionPane.QUESTION_MESSAGE, null,
                allowed.toArray(), allowed.iterator().next());
        if (!(choice instanceof OrderStatus target)) {
            return;
        }
        statusBar.setBusy(true);
        AsyncTask.run(() -> context.orders().changeStatus(order.getId(), target), updated -> {
            model.replace(updated);
            statusBar.success("Order now " + updated.getStatus().getLabel());
        }, error -> Dialogs.error(this, "Change status", error), () -> statusBar.setBusy(false));
    }

    private void delete() {
        Order order = selected();
        if (order == null) {
            return;
        }
        if (!context.session().isAdmin()) {
            Dialogs.warn(this, "Only administrators can delete orders");
            return;
        }
        if (!Dialogs.confirmDelete(this, "order " + order.getId())) {
            return;
        }
        statusBar.setBusy(true);
        AsyncTask.runVoid(() -> context.orders().delete(order.getId()), () -> {
            statusBar.setBusy(false);
            statusBar.success("Order deleted");
            refresh();
        }, error -> {
            statusBar.setBusy(false);
            Dialogs.error(this, "Delete order", error);
        });
    }
}
