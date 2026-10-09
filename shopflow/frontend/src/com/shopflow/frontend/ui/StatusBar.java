package com.shopflow.frontend.ui;

import com.shopflow.frontend.session.Session;

import javax.swing.BorderFactory;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JProgressBar;
import javax.swing.Timer;
import java.awt.BorderLayout;
import java.awt.Color;

/**
 * Bottom bar of the main window showing the last message, a busy
 * indicator and who is signed in.
 */
public class StatusBar extends JPanel {

    private static final long serialVersionUID = 1L;
    private static final int CLEAR_AFTER_MS = 6000;

    private final JLabel message = new JLabel(" ");
    private final JLabel user = new JLabel();
    private final JProgressBar busy = new JProgressBar();
    private final Timer clearTimer;
    private int busyCount;

    public StatusBar(Session session) {
        super(new BorderLayout(Theme.GAP, 0));
        setBorder(BorderFactory.createCompoundBorder(
                BorderFactory.createMatteBorder(1, 0, 0, 0, Theme.BORDER),
                Theme.padding(4, Theme.PAD, 4, Theme.PAD)));
        busy.setIndeterminate(true);
        busy.setVisible(false);
        busy.setPreferredSize(new java.awt.Dimension(90, 12));

        JPanel right = new JPanel(new BorderLayout(Theme.GAP, 0));
        right.setOpaque(false);
        right.add(busy, BorderLayout.WEST);
        right.add(user, BorderLayout.EAST);

        add(message, BorderLayout.CENTER);
        add(right, BorderLayout.EAST);

        clearTimer = new Timer(CLEAR_AFTER_MS, event -> message.setText(" "));
        clearTimer.setRepeats(false);

        session.addListener(this::onSessionChanged);
        onSessionChanged(session);
    }

    private void onSessionChanged(Session session) {
        if (session.isLoggedIn()) {
            user.setText(session.displayName() + " (" + session.getUser().getRole() + ")");
            user.setForeground(Theme.MUTED);
        } else {
            user.setText("Not signed in");
            user.setForeground(Theme.MUTED);
        }
    }

    public void info(String text) {
        show(text, Theme.MUTED);
    }

    public void success(String text) {
        show(text, Theme.SUCCESS);
    }

    public void error(String text) {
        show(text, Theme.DANGER);
    }

    private void show(String text, Color color) {
        message.setText(text);
        message.setForeground(color);
        clearTimer.restart();
    }

    /** Call once per started background task and once when it finishes. */
    public void setBusy(boolean isBusy) {
        busyCount = Math.max(0, busyCount + (isBusy ? 1 : -1));
        busy.setVisible(busyCount > 0);
    }
}
