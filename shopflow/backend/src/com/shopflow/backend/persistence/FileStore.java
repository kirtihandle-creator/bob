package com.shopflow.backend.persistence;

import com.shopflow.backend.repository.InMemoryRepository;
import com.shopflow.common.json.Json;
import com.shopflow.common.model.Identifiable;

import java.io.IOException;
import java.io.UncheckedIOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardCopyOption;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 * Persists each repository to {@code <dataDir>/<name>.json}. Writes are
 * atomic (temp file then move) so a crash mid-write never corrupts data.
 * The same files are read by the Python report script, so the format
 * must stay a plain JSON array of entity objects.
 */
public class FileStore {

    private static final Logger LOG = Logger.getLogger(FileStore.class.getName());

    private final Path dataDir;

    public FileStore(Path dataDir) {
        this.dataDir = dataDir;
    }

    public Path getDataDir() {
        return dataDir;
    }

    public void ensureDirectory() throws IOException {
        Files.createDirectories(dataDir);
    }

    public Path fileFor(String name) {
        return dataDir.resolve(name + ".json");
    }

    /** Loads the repository from disk and wires it to save on every change. */
    public <T extends Identifiable> void attach(InMemoryRepository<T> repository) {
        List<T> loaded = load(repository);
        repository.loadAll(loaded);
        repository.setChangeListener(this::save);
        LOG.info(() -> "Loaded " + loaded.size() + " " + repository.getName());
    }

    @SuppressWarnings("unchecked")
    public <T extends Identifiable> List<T> load(InMemoryRepository<T> repository) {
        Path file = fileFor(repository.getName());
        List<T> entities = new ArrayList<>();
        if (!Files.exists(file)) {
            return entities;
        }
        try {
            String text = Files.readString(file, StandardCharsets.UTF_8);
            for (Object element : Json.array(text)) {
                if (element instanceof Map<?, ?> map) {
                    entities.add(repository.fromJson((Map<String, Object>) map));
                }
            }
        } catch (IOException | RuntimeException e) {
            LOG.log(Level.WARNING, "Could not read " + file + "; starting empty", e);
        }
        return entities;
    }

    /**
     * Writes the repository to disk.
     *
     * @throws UncheckedIOException when the data could not be written; the caller
     *                              must not report the mutation as saved
     */
    public synchronized <T extends Identifiable> void save(InMemoryRepository<T> repository) {
        Path file = fileFor(repository.getName());
        Path temp = dataDir.resolve(repository.getName() + ".json.tmp");
        try {
            ensureDirectory();
            Files.writeString(temp, Json.prettify(repository.toJsonList()), StandardCharsets.UTF_8);
            Files.move(temp, file, StandardCopyOption.REPLACE_EXISTING, StandardCopyOption.ATOMIC_MOVE);
        } catch (IOException e) {
            LOG.log(Level.SEVERE, "Failed to persist " + repository.getName(), e);
            try {
                Files.deleteIfExists(temp);
            } catch (IOException cleanup) {
                LOG.log(Level.WARNING, "Could not remove temp file " + temp, cleanup);
            }
            throw new UncheckedIOException("Failed to persist " + repository.getName(), e);
        }
    }

    public void saveAll(List<InMemoryRepository<?>> repositories) {
        for (InMemoryRepository<?> repository : repositories) {
            save(repository);
        }
    }
}
