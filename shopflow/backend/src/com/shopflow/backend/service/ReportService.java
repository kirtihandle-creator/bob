package com.shopflow.backend.service;

import com.shopflow.backend.persistence.FileStore;
import com.shopflow.backend.server.ApiException;
import com.shopflow.backend.server.ServerConfig;
import com.shopflow.common.json.Json;

import java.io.IOException;
import java.io.InputStream;
import java.io.UncheckedIOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.util.List;
import java.util.Map;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.TimeoutException;
import java.util.logging.Logger;

/**
 * Produces dashboard statistics by delegating to the Python script
 * {@code report_service.py} that lives alongside the Java services.
 *
 * The Java backend does not compute reports itself: it flushes the
 * repositories to disk, runs the Python interpreter against the data
 * directory, and parses the JSON the script prints. If Python is not
 * installed or the script is missing, the reports endpoint fails and the
 * desktop dashboard cannot load.
 */
public class ReportService {

    private static final Logger LOG = Logger.getLogger(ReportService.class.getName());
    private static final long TIMEOUT_SECONDS = 20;
    /** Dedicated daemon threads for draining script output, kept off the common pool. */
    private static final ExecutorService DRAIN_POOL = Executors.newCachedThreadPool(runnable -> {
        Thread thread = new Thread(runnable, "report-drain");
        thread.setDaemon(true);
        return thread;
    });

    private final ServerConfig config;
    private final FileStore fileStore;
    private volatile Map<String, Object> lastReport;
    private volatile long lastRunAt;

    public ReportService(ServerConfig config, FileStore fileStore) {
        this.config = config;
        this.fileStore = fileStore;
    }

    public Map<String, Object> summary() {
        if (!Files.exists(config.getReportScript())) {
            throw new ApiException(503, "Report script not found: " + config.getReportScript());
        }
        List<String> command = List.of(
                config.getPythonCommand(),
                config.getReportScript().toString(),
                fileStore.getDataDir().toString());
        ProcessBuilder builder = new ProcessBuilder(command);
        builder.redirectErrorStream(false);
        try {
            Process process = builder.start();
            // Drain both streams on background threads so the timeout below is enforced
            // even when the script hangs while still holding its pipes open.
            CompletableFuture<String> stdoutFuture = drain(process.getInputStream());
            CompletableFuture<String> stderrFuture = drain(process.getErrorStream());
            if (!process.waitFor(TIMEOUT_SECONDS, TimeUnit.SECONDS)) {
                process.destroyForcibly();
                throw new ApiException(504, "Report script timed out after " + TIMEOUT_SECONDS + "s");
            }
            String stdout = stdoutFuture.get(TIMEOUT_SECONDS, TimeUnit.SECONDS);
            String stderr = stderrFuture.get(TIMEOUT_SECONDS, TimeUnit.SECONDS);
            if (process.exitValue() != 0) {
                LOG.warning(() -> "report_service.py failed: " + stderr);
                throw new ApiException(502, "Report script failed: " + firstLine(stderr));
            }
            Map<String, Object> report = Json.object(stdout);
            report.put("generatedBy", "python:" + config.getReportScript().getFileName());
            report.put("generatedAt", System.currentTimeMillis());
            lastReport = report;
            lastRunAt = System.currentTimeMillis();
            return report;
        } catch (IOException e) {
            throw new ApiException(503, "Could not run Python (" + config.getPythonCommand() + "): "
                    + e.getMessage(), e);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            throw ApiException.internal("Interrupted while running report script", e);
        } catch (ExecutionException | TimeoutException e) {
            throw new ApiException(502, "Could not read report script output: " + e.getMessage(), e);
        } catch (RuntimeException e) {
            if (e instanceof ApiException api) {
                throw api;
            }
            throw new ApiException(502, "Report script returned invalid JSON: " + e.getMessage(), e);
        }
    }

    /** Last successful report, or null if none has been generated yet. */
    public Map<String, Object> cached() {
        return lastReport;
    }

    public long lastRunAt() {
        return lastRunAt;
    }

    public Map<String, Object> health() {
        boolean scriptPresent = Files.exists(config.getReportScript());
        return Json.map(
                "python", config.getPythonCommand(),
                "script", config.getReportScript().toString(),
                "scriptPresent", scriptPresent,
                "lastRunAt", lastRunAt);
    }

    private static CompletableFuture<String> drain(InputStream stream) {
        return CompletableFuture.supplyAsync(() -> {
            try (InputStream in = stream) {
                return new String(in.readAllBytes(), StandardCharsets.UTF_8);
            } catch (IOException e) {
                throw new UncheckedIOException(e);
            }
        }, DRAIN_POOL);
    }

    private static String firstLine(String text) {
        if (text == null || text.isBlank()) {
            return "unknown error";
        }
        String[] lines = text.strip().split("\\R");
        return lines[lines.length - 1];
    }
}
