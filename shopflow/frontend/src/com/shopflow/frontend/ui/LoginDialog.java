package com.shopflow.frontend.ui;

import com.shopflow.frontend.AppContext;
import com.shopflow.frontend.api.ApiException;
import com.shopflow.frontend.ui.components.FormBuilder;
import com.shopflow.frontend.util.AsyncTask;

import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JPasswordField;
import javax.swing.JTextField;
import java.awt.BorderLayout;
import java.awt.FlowLayout;

/**
 * Modal sign-in dialog. Closes itself on success; {@link #wasSuccessful()}
 * tells the caller whether a session was established.
 */
public class LoginDialog extends JDialog {

    private static final long serialVersionUID = 1L;

    private final AppContext context;
    private final JTextField username = new JTextField(18);
    private final JPasswordField password = new JPasswordField(18);
    private final JLabel status = Theme.muted(" ");
    private final JButton signIn = Theme.primaryButton("Sign in");
    private boolean successful;

    public LoginDialog(JFrame owner, AppContext context) {
        super(owner, "Sign in to ShopFlow", true);
        this.context = context;
        setDefaultCloseOperation(DISPOSE_ON_CLOSE);
        buildUi();
        pack();
        setResizable(false);
        setLocationRelativeTo(owner);
    }

    private void buildUi() {
        JPanel root = new JPanel(new BorderLayout(0, Theme.GAP));
        root.setBorder(Theme.padding());

        JPanel header = new JPanel(new BorderLayout());
        header.add(Theme.title("ShopFlow"), BorderLayout.NORTH);
        header.add(Theme.muted("Backend: " + context.client().getBaseUrl()), BorderLayout.SOUTH);
        root.add(header, BorderLayout.NORTH);

        JPanel form = new FormBuilder()
                .add("Username", username)
                .add("Password", password)
                .build();
        root.add(form, BorderLayout.CENTER);

        JPanel footer = new JPanel(new BorderLayout());
        footer.add(status, BorderLayout.NORTH);
        JPanel buttons = new JPanel(new FlowLayout(FlowLayout.RIGHT, Theme.GAP, 0));
        JButton cancel = new JButton("Quit");
        cancel.addActionListener(event -> dispose());
        buttons.add(cancel);
        buttons.add(signIn);
        footer.add(buttons, BorderLayout.SOUTH);
        root.add(footer, BorderLayout.SOUTH);

        signIn.addActionListener(event -> attemptLogin());
        password.addActionListener(event -> attemptLogin());
        username.addActionListener(event -> password.requestFocusInWindow());
        getRootPane().setDefaultButton(signIn);
        setContentPane(root);
    }

    private void attemptLogin() {
        String user = username.getText().trim();
        String pass = new String(password.getPassword());
        if (user.isEmpty() || pass.isEmpty()) {
            showStatus("Enter both username and password", true);
            return;
        }
        setBusy(true);
        showStatus("Signing in...", false);
        AsyncTask.run(
                () -> context.auth().login(user, pass),
                loggedIn -> {
                    successful = true;
                    dispose();
                },
                error -> {
                    String message = error instanceof ApiException api && api.isUnauthorized()
                            ? "Invalid username or password"
                            : error instanceof ApiException api ? api.userMessage() : String.valueOf(error);
                    showStatus(message, true);
                    password.selectAll();
                    password.requestFocusInWindow();
                },
                () -> setBusy(false));
    }

    private void setBusy(boolean busy) {
        signIn.setEnabled(!busy);
        username.setEnabled(!busy);
        password.setEnabled(!busy);
    }

    private void showStatus(String text, boolean isError) {
        status.setText(text);
        status.setForeground(isError ? Theme.DANGER : Theme.MUTED);
        pack();
    }

    public boolean wasSuccessful() {
        return successful;
    }
}
