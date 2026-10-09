package com.shopflow.frontend.util;

import com.shopflow.frontend.api.ApiException;

import javax.swing.SwingUtilities;
import javax.swing.SwingWorker;
import java.util.concurrent.ExecutionException;
import java.util.function.Consumer;
import java.util.function.Supplier;

/**
 * Runs a blocking API call off the Swing thread and delivers the result
 * or error back on it. Usage:
 *
 * <pre>
 * AsyncTask.run(() -> api.list(), rows -> table.setRows(rows), this::showError);
 * </pre>
 */
public final class AsyncTask<T> extends SwingWorker<T, Void> {

    private final Supplier<T> work;
    private final Consumer<T> onSuccess;
    private final Consumer<Throwable> onError;
    private final Runnable onFinally;

    private AsyncTask(Supplier<T> work, Consumer<T> onSuccess, Consumer<Throwable> onError, Runnable onFinally) {
        this.work = work;
        this.onSuccess = onSuccess;
        this.onError = onError;
        this.onFinally = onFinally;
    }

    public static <T> AsyncTask<T> run(Supplier<T> work, Consumer<T> onSuccess, Consumer<Throwable> onError) {
        return run(work, onSuccess, onError, () -> { });
    }

    public static <T> AsyncTask<T> run(Supplier<T> work, Consumer<T> onSuccess,
                                       Consumer<Throwable> onError, Runnable onFinally) {
        AsyncTask<T> task = new AsyncTask<>(work, onSuccess, onError, onFinally);
        task.execute();
        return task;
    }

    /** Variant for calls that return nothing. */
    public static AsyncTask<Void> runVoid(Runnable work, Runnable onSuccess, Consumer<Throwable> onError) {
        return run(() -> {
            work.run();
            return null;
        }, ignored -> onSuccess.run(), onError);
    }

    @Override
    protected T doInBackground() {
        return work.get();
    }

    @Override
    protected void done() {
        try {
            T result = get();
            onSuccess.accept(result);
        } catch (ExecutionException e) {
            onError.accept(unwrap(e.getCause()));
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            onError.accept(e);
        } catch (RuntimeException e) {
            onError.accept(e);
        } finally {
            onFinally.run();
        }
    }

    private static Throwable unwrap(Throwable cause) {
        return cause == null ? new ApiException(0, "Unknown error") : cause;
    }

    /** Ensures a runnable executes on the Swing event thread. */
    public static void onUi(Runnable runnable) {
        if (SwingUtilities.isEventDispatchThread()) {
            runnable.run();
        } else {
            SwingUtilities.invokeLater(runnable);
        }
    }
}
