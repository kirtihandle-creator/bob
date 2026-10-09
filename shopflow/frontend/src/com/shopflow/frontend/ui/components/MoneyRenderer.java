package com.shopflow.frontend.ui.components;

import com.shopflow.common.util.Money;

import javax.swing.JTable;
import javax.swing.SwingConstants;
import javax.swing.table.DefaultTableCellRenderer;
import java.awt.Component;

/**
 * Right-aligned currency renderer for {@code Double} table columns.
 */
public class MoneyRenderer extends DefaultTableCellRenderer {

    private static final long serialVersionUID = 1L;

    public MoneyRenderer() {
        setHorizontalAlignment(SwingConstants.RIGHT);
    }

    @Override
    public Component getTableCellRendererComponent(JTable table, Object value, boolean isSelected,
                                                   boolean hasFocus, int row, int column) {
        String text = value instanceof Number number ? Money.format(number.doubleValue()) : "";
        return super.getTableCellRendererComponent(table, text, isSelected, hasFocus, row, column);
    }

    /** Installs this renderer on every Double column of the table. */
    public static void installOn(JTable table) {
        table.setDefaultRenderer(Double.class, new MoneyRenderer());
    }
}
