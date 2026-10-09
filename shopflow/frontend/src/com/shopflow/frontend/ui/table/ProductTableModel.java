package com.shopflow.frontend.ui.table;

import com.shopflow.common.model.Product;
import com.shopflow.common.util.Money;
import com.shopflow.frontend.api.ProductApi;

import javax.swing.table.AbstractTableModel;
import java.util.ArrayList;
import java.util.List;

/**
 * Table model for the product list, backed by enriched rows from the API.
 */
public class ProductTableModel extends AbstractTableModel {

    private static final long serialVersionUID = 1L;
    private static final String[] COLUMNS = {"SKU", "Name", "Category", "Price", "Stock", "Status"};

    private final List<ProductApi.Row> rows = new ArrayList<>();

    public void setRows(List<ProductApi.Row> newRows) {
        rows.clear();
        rows.addAll(newRows);
        fireTableDataChanged();
    }

    public ProductApi.Row rowAt(int modelIndex) {
        return rows.get(modelIndex);
    }

    public Product productAt(int modelIndex) {
        return rows.get(modelIndex).product();
    }

    public List<ProductApi.Row> getRows() {
        return List.copyOf(rows);
    }

    public int indexOf(String productId) {
        for (int i = 0; i < rows.size(); i++) {
            if (rows.get(i).product().getId().equals(productId)) {
                return i;
            }
        }
        return -1;
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
            case 3 -> Double.class;
            case 4 -> Integer.class;
            default -> String.class;
        };
    }

    @Override
    public Object getValueAt(int rowIndex, int columnIndex) {
        ProductApi.Row row = rows.get(rowIndex);
        Product product = row.product();
        return switch (columnIndex) {
            case 0 -> product.getSku();
            case 1 -> product.getName();
            case 2 -> row.categoryName();
            case 3 -> product.getPrice();
            case 4 -> product.getStock();
            case 5 -> product.isLowStock() ? "Low stock" : "In stock";
            default -> "";
        };
    }

    /** Display helper used by the renderer for the price column. */
    public static String formatPrice(Object value) {
        return value instanceof Number number ? Money.format(number.doubleValue()) : "";
    }
}
