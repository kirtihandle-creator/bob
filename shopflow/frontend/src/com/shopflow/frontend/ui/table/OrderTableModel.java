package com.shopflow.frontend.ui.table;

import com.shopflow.common.model.Order;
import com.shopflow.common.util.Dates;

import javax.swing.table.AbstractTableModel;
import java.util.ArrayList;
import java.util.List;

/**
 * Table model for the order list.
 */
public class OrderTableModel extends AbstractTableModel {

    private static final long serialVersionUID = 1L;
    private static final String[] COLUMNS = {"Order", "Customer", "Items", "Total", "Status", "Created"};

    private final List<Order> orders = new ArrayList<>();

    public void setOrders(List<Order> newOrders) {
        orders.clear();
        orders.addAll(newOrders);
        fireTableDataChanged();
    }

    public Order orderAt(int modelIndex) {
        return orders.get(modelIndex);
    }

    public void replace(Order updated) {
        for (int i = 0; i < orders.size(); i++) {
            if (orders.get(i).getId().equals(updated.getId())) {
                orders.set(i, updated);
                fireTableRowsUpdated(i, i);
                return;
            }
        }
        orders.add(0, updated);
        fireTableRowsInserted(0, 0);
    }

    @Override
    public int getRowCount() {
        return orders.size();
    }

    @Override
    public int getColumnCount() {
        return COLUMNS.length;
    }

    @Override
    public String getColumnName(int column) {
        return COLUMNS[column];
    }

    @Override
    public Class<?> getColumnClass(int column) {
        return switch (column) {
            case 2 -> Integer.class;
            case 3 -> Double.class;
            default -> String.class;
        };
    }

    @Override
    public Object getValueAt(int rowIndex, int columnIndex) {
        Order order = orders.get(rowIndex);
        return switch (columnIndex) {
            case 0 -> order.getId();
            case 1 -> order.getCustomerName();
            case 2 -> order.getItemCount();
            case 3 -> order.getTotal();
            case 4 -> order.getStatus().getLabel();
            case 5 -> Dates.formatDateTime(order.getCreatedAt());
            default -> "";
        };
    }
}
