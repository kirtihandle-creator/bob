package com.shopflow.frontend;

import com.shopflow.frontend.ui.LoginDialog;
import com.shopflow.frontend.ui.MainWindow;
import com.shopflow.frontend.ui.Theme;

import javax.swing.SwingUtilities;

/**
 * Desktop client entry point.
 *
 * <pre>
 * java -cp out/common;out/frontend com.shopflow.frontend.Main --url=http://localhost:8080
 * </pre>
 */
public final class Main {

    private Main() {
    }

    public static void main(String[] args) {
        String baseUrl = AppContext.resolveBaseUrl(args);
        AppContext context = new AppContext(baseUrl);
        Theme.install();
        SwingUtilities.invokeLater(() -> showLoginThenMain(context));
    }

    /**
     * Shows the sign-in dialog and, on success, the main window.
     * Quitting the dialog exits the application.
     */
    public static void showLoginThenMain(AppContext context) {
        LoginDialog login = new LoginDialog(null, context);
        login.setVisible(true);
        if (!login.wasSuccessful()) {
            System.exit(0);
            return;
        }
        MainWindow window = new MainWindow(context);
        window.setVisible(true);
        window.start();
    }
}
