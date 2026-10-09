package com.shopflow.frontend.ui.table;

import com.shopflow.common.model.Customer;
import com.shopflow.common.util.Dates;
import com.shopflow.frontend.api.CustomerApi;

import javax.swing.table.AbstractTableModel;
import java.util.ArrayList;
import java.util.List;

/**
 * Table model for customers with order statistics.
 */
public class CustomerTableModel extends AbstractTableModel {

    private static final long serialVersionUID = 1L;
    private static final String[] COLUMNS = {"Name", "Email", "Phone", "Orders", "Lifetime value", "Since"};

    private final List<CustomerApi.Row> rows = new ArrayList<>();

    public void setRows(List<CustomerApi.Row> newRows) {
        rows.clear();
        rows.addAll(newRows);
        fireTableDataChanged();
    }

    public CustomerApi.Row rowAt(int modelIndex) {
        return rows.get(modelIndex);
    }

    public Customer customerAt(int modelIndex) {
        return rows.get(modelIndex).customer();
    }

    @Override
    public int getRowCount() {
        return rows.size();
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
            case 3 -> Integer.class;
            case 4 -> Double.class;
            default -> String.class;
        };
    }

    @Override
    public Object getValueAt(int rowIndex, int columnIndex) {
        CustomerApi.Row row = rows.get(rowIndex);
        Customer customer = row.customer();
        return switch (columnIndex) {
            case 0 -> customer.getName();
            case 1 -> customer.getEmail();
            case 2 -> customer.getPhone();
            case 3 -> row.orderCount();
            case 4 -> row.lifetimeValue();
            case 5 -> Dates.formatDate(customer.getCreatedAt());
            default -> "";
        };
    }
}
