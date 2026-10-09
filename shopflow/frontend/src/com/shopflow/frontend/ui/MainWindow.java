package com.shopflow.frontend.ui;

import com.shopflow.frontend.AppContext;
import com.shopflow.frontend.util.AsyncTask;
import com.shopflow.frontend.util.Dialogs;

import javax.swing.JFrame;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JPasswordField;
import javax.swing.JTabbedPane;
import javax.swing.SwingUtilities;
import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

/**
 * Main application window: a tab per screen, a menu bar and a status bar.
 * Each tab refreshes itself when it becomes visible.
 */
public class MainWindow extends JFrame {

    private static final long serialVersionUID = 1L;

    private final AppContext context;
    private final StatusBar statusBar;
    private final JTabbedPane tabs = new JTabbedPane();
    private final DashboardPanel dashboard;
    private final ProductPanel products;
    private final CategoryPanel categories;
    private final CustomerPanel customers;
    private final OrderPanel orders;

    public MainWindow(AppContext context) {
        super("ShopFlow");
        this.context = context;
        this.statusBar = new StatusBar(context.session());
        this.dashboard = new DashboardPanel(context, statusBar);
        this.products = new ProductPanel(context, statusBar);
        this.categories = new CategoryPanel(context, statusBar);
        this.customers = new CustomerPanel(context, statusBar);
        this.orders = new OrderPanel(context, statusBar);

        tabs.addTab("Dashboard", dashboard);
        tabs.addTab("Products", products);
        tabs.addTab("Categories", categories);
        tabs.addTab("Customers", customers);
        tabs.addTab("Orders", orders);
        tabs.addChangeListener(event -> refreshCurrentTab());

        setJMenuBar(buildMenu());
        setLayout(new BorderLayout());
        add(tabs, BorderLayout.CENTER);
        add(statusBar, BorderLayout.SOUTH);
        setDefaultCloseOperation(DO_NOTHING_ON_CLOSE);
        addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent event) {
                quit();
            }
        });
        setMinimumSize(new Dimension(900, 600));
        setSize(1100, 700);
        setLocationRelativeTo(null);
    }

    private JMenuBar buildMenu() {
        JMenuBar bar = new JMenuBar();

        JMenu file = new JMenu("File");
        JMenuItem refresh = new JMenuItem("Refresh current tab");
        refresh.addActionListener(event -> refreshCurrentTab());
        JMenuItem quit = new JMenuItem("Quit");
        quit.addActionListener(event -> quit());
        file.add(refresh);
        file.addSeparator();
        file.add(quit);

        JMenu account = new JMenu("Account");
        JMenuItem password = new JMenuItem("Change password...");
        password.addActionListener(event -> changePassword());
        JMenuItem signOut = new JMenuItem("Sign out");
        signOut.addActionListener(event -> signOut());
        account.add(password);
        account.addSeparator();
        account.add(signOut);

        JMenu help = new JMenu("Help");
        JMenuItem about = new JMenuItem("About");
        about.addActionListener(event -> Dialogs.info(this,
                "ShopFlow desktop client\nBackend: " + context.client().getBaseUrl()
                        + "\nSigned in as " + context.session().displayName()));
        help.add(about);

        bar.add(file);
        bar.add(account);
        bar.add(help);
        return bar;
    }

    /** Loads the first tab; call after the window is shown. */
    public void start() {
        refreshCurrentTab();
    }

    private void refreshCurrentTab() {
        switch (tabs.getSelectedIndex()) {
            case 0 -> dashboard.refresh();
            case 1 -> products.refresh();
            case 2 -> categories.refresh();
            case 3 -> customers.refresh();
            case 4 -> orders.refresh();
            default -> { }
        }
    }

    private void changePassword() {
        JPasswordField current = new JPasswordField(18);
        JPasswordField fresh = new JPasswordField(18);
        Object[] form = {"Current password", current, "New password", fresh};
        int choice = javax.swing.JOptionPane.showConfirmDialog(this, form, "Change password",
                javax.swing.JOptionPane.OK_CANCEL_OPTION, javax.swing.JOptionPane.PLAIN_MESSAGE);
        if (choice != javax.swing.JOptionPane.OK_OPTION) {
            return;
        }
        String currentText = new String(current.getPassword());
        String freshText = new String(fresh.getPassword());
        statusBar.setBusy(true);
        AsyncTask.runVoid(() -> context.auth().changePassword(currentText, freshText), () -> {
            statusBar.setBusy(false);
            statusBar.success("Password changed");
        }, error -> {
            statusBar.setBusy(false);
            Dialogs.error(this, "Change password", error);
        });
    }

    private void signOut() {
        context.auth().logout();
        dispose();
        SwingUtilities.invokeLater(() -> com.shopflow.frontend.Main.showLoginThenMain(context));
    }

    private void quit() {
        context.auth().logout();
        dispose();
        System.exit(0);
    }
}
