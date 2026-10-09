package com.shopflow.frontend.ui.table;

import com.shopflow.common.model.Category;
import com.shopflow.frontend.api.CategoryApi;

import javax.swing.table.AbstractTableModel;
import java.util.ArrayList;
import java.util.List;

/**
 * Table model for categories with their product counts.
 */
public class CategoryTableModel extends AbstractTableModel {

    private static final long serialVersionUID = 1L;
    private static final String[] COLUMNS = {"Name", "Description", "Products"};

    private final List<CategoryApi.Row> rows = new ArrayList<>();

    public void setRows(List<CategoryApi.Row> newRows) {
        rows.clear();
        rows.addAll(newRows);
        fireTableDataChanged();
    }

    public CategoryApi.Row rowAt(int modelIndex) {
        return rows.get(modelIndex);
    }

    public Category categoryAt(int modelIndex) {
        return rows.get(modelIndex).category();
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
        return column == 2 ? Integer.class : String.class;
    }

    @Override
    public Object getValueAt(int rowIndex, int columnIndex) {
        CategoryApi.Row row = rows.get(rowIndex);
        return switch (columnIndex) {
            case 0 -> row.category().getName();
            case 1 -> row.category().getDescription();
            case 2 -> row.productCount();
            default -> "";
        };
    }
}
