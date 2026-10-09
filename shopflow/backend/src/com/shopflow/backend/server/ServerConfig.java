package com.shopflow.backend.server;

import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * Runtime configuration for the backend, read from system properties
 * and environment variables with sensible defaults. Example:
 * {@code java -Dshopflow.port=9090 -Dshopflow.data=./mydata ...}
 */
public class ServerConfig {

    public static final int DEFAULT_PORT = 8080;
    public static final String DEFAULT_DATA_DIR = "data";
    public static final String DEFAULT_PYTHON = "python";
    public static final long DEFAULT_TOKEN_TTL_MS = 8L * 60 * 60 * 1000;

    private final int port;
    private final Path dataDir;
    private final long tokenTtlMillis;
    private final boolean seedOnEmpty;
    private final int threadPoolSize;
    private final String pythonCommand;
    private final Path reportScript;
    private final String bootstrapAdminUser;
    private final String bootstrapAdminPassword;

    public ServerConfig(int port, Path dataDir, long tokenTtlMillis, boolean seedOnEmpty,
                        int threadPoolSize, String pythonCommand, Path reportScript,
                        String bootstrapAdminUser, String bootstrapAdminPassword) {
        this.port = port;
        this.dataDir = dataDir;
        this.tokenTtlMillis = tokenTtlMillis;
        this.seedOnEmpty = seedOnEmpty;
        this.threadPoolSize = threadPoolSize;
        this.pythonCommand = pythonCommand;
        this.reportScript = reportScript;
        this.bootstrapAdminUser = bootstrapAdminUser;
        this.bootstrapAdminPassword = bootstrapAdminPassword;
    }

    public static ServerConfig fromEnvironment() {
        int port = intSetting("shopflow.port", "SHOPFLOW_PORT", DEFAULT_PORT);
        String dir = stringSetting("shopflow.data", "SHOPFLOW_DATA", DEFAULT_DATA_DIR);
        long ttl = longSetting("shopflow.tokenTtl", "SHOPFLOW_TOKEN_TTL", DEFAULT_TOKEN_TTL_MS);
        boolean seed = !"false".equalsIgnoreCase(stringSetting("shopflow.seed", "SHOPFLOW_SEED", "true"));
        int threads = intSetting("shopflow.threads", "SHOPFLOW_THREADS", 8);
        String python = stringSetting("shopflow.python", "SHOPFLOW_PYTHON", DEFAULT_PYTHON);
        String script = stringSetting("shopflow.reportScript", "SHOPFLOW_REPORT_SCRIPT",
                "backend/src/com/shopflow/backend/service/report_service.py");
        String adminUser = stringSetting("shopflow.adminUser", "SHOPFLOW_ADMIN_USER", "admin");
        String adminPassword = stringSetting("shopflow.adminPassword", "SHOPFLOW_ADMIN_PASSWORD", "");
        return new ServerConfig(port, Paths.get(dir).toAbsolutePath(), ttl, seed, threads,
                python, Paths.get(script).toAbsolutePath(), adminUser, adminPassword);
    }

    private static String stringSetting(String property, String env, String fallback) {
        String value = System.getProperty(property);
        if (value == null || value.isBlank()) {
            value = System.getenv(env);
        }
        return value == null || value.isBlank() ? fallback : value.trim();
    }

    private static int intSetting(String property, String env, int fallback) {
        try {
            return Integer.parseInt(stringSetting(property, env, String.valueOf(fallback)));
        } catch (NumberFormatException e) {
            return fallback;
        }
    }

    private static long longSetting(String property, String env, long fallback) {
        try {
            return Long.parseLong(stringSetting(property, env, String.valueOf(fallback)));
        } catch (NumberFormatException e) {
            return fallback;
        }
    }

    public int getPort() {
        return port;
    }

    public Path getDataDir() {
        return dataDir;
    }

    public long getTokenTtlMillis() {
        return tokenTtlMillis;
    }

    public boolean isSeedOnEmpty() {
        return seedOnEmpty;
    }

    public int getThreadPoolSize() {
        return threadPoolSize;
    }

    public String getPythonCommand() {
        return pythonCommand;
    }

    public Path getReportScript() {
        return reportScript;
    }

    public String getBootstrapAdminUser() {
        return bootstrapAdminUser;
    }

    /** Only used to create the first administrator; never persisted. */
    public String getBootstrapAdminPassword() {
        return bootstrapAdminPassword;
    }

    public boolean hasBootstrapAdminPassword() {
        return bootstrapAdminPassword != null && !bootstrapAdminPassword.isBlank();
    }

    @Override
    public String toString() {
        return "ServerConfig{port=" + port + ", dataDir=" + dataDir
                + ", tokenTtlMillis=" + tokenTtlMillis + ", seedOnEmpty=" + seedOnEmpty
                + ", threads=" + threadPoolSize + ", python=" + pythonCommand
                + ", reportScript=" + reportScript
                + ", bootstrapAdminUser=" + bootstrapAdminUser
                + ", bootstrapAdminPassword=" + (hasBootstrapAdminPassword() ? "<set>" : "<unset>") + "}";
    }
}
