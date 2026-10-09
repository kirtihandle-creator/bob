package com.shopflow.frontend.ui;

import com.shopflow.common.model.Category;
import com.shopflow.frontend.AppContext;
import com.shopflow.frontend.api.CategoryApi;
import com.shopflow.frontend.ui.components.ToolbarFactory;
import com.shopflow.frontend.ui.table.CategoryTableModel;
import com.shopflow.frontend.util.AsyncTask;
import com.shopflow.frontend.util.Dialogs;

import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.SwingUtilities;
import java.awt.BorderLayout;

/**
 * List, create, edit and delete categories.
 */
public class CategoryPanel extends JPanel {

    private static final long serialVersionUID = 1L;

    private final AppContext context;
    private final StatusBar statusBar;
    private final CategoryTableModel model = new CategoryTableModel();
    private final JTable table = new JTable(model);

    public CategoryPanel(AppContext context, StatusBar statusBar) {
        super(new BorderLayout());
        this.context = context;
        this.statusBar = statusBar;
        Theme.styleTable(table);
        table.setSelectionMode(javax.swing.ListSelectionModel.SINGLE_SELECTION);

        JPanel toolbar = ToolbarFactory.create(null,
                ToolbarFactory.primary("New", this::create),
                ToolbarFactory.button("Edit", this::edit),
                ToolbarFactory.danger("Delete", this::delete),
                ToolbarFactory.button("Refresh", this::refresh));
        add(toolbar, BorderLayout.NORTH);
        add(new JScrollPane(table), BorderLayout.CENTER);
    }

    public void refresh() {
        statusBar.setBusy(true);
        AsyncTask.run(context.categories()::listRows, rows -> {
            model.setRows(rows);
            statusBar.info(rows.size() + " categories");
        }, error -> Dialogs.error(this, "Categories", error), () -> statusBar.setBusy(false));
    }

    private CategoryApi.Row selected() {
        int viewRow = table.getSelectedRow();
        if (viewRow < 0) {
            Dialogs.warn(this, "Select a category first");
            return null;
        }
        return model.rowAt(table.convertRowIndexToModel(viewRow));
    }

    private void create() {
        Category draft = CategoryDialog.show(SwingUtilities.getWindowAncestor(this), null);
        if (draft == null) {
            return;
        }
        submit(() -> context.categories().create(draft), "Category created");
    }

    private void edit() {
        CategoryApi.Row row = selected();
        if (row == null) {
            return;
        }
        Category edited = CategoryDialog.show(SwingUtilities.getWindowAncestor(this), row.category());
        if (edited == null) {
            return;
        }
        submit(() -> context.categories().update(edited), "Category updated");
    }

    private void delete() {
        CategoryApi.Row row = selected();
        if (row == null) {
            return;
        }
        if (row.productCount() > 0) {
            Dialogs.warn(this, "This category still has " + row.productCount() + " product(s)");
            return;
        }
        if (!Dialogs.confirmDelete(this, "category \"" + row.category().getName() + "\"")) {
            return;
        }
        statusBar.setBusy(true);
        AsyncTask.runVoid(() -> context.categories().delete(row.category().getId()), () -> {
            statusBar.setBusy(false);
            statusBar.success("Category deleted");
            refresh();
        }, error -> {
            statusBar.setBusy(false);
            Dialogs.error(this, "Delete category", error);
        });
    }

    private void submit(java.util.function.Supplier<Category> call, String successMessage) {
        statusBar.setBusy(true);
        AsyncTask.run(call, saved -> {
            statusBar.success(successMessage + ": " + saved.getName());
            refresh();
        }, error -> Dialogs.error(this, "Save category", error), () -> statusBar.setBusy(false));
    }
}
