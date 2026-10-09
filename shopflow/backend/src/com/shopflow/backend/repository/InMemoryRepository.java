package com.shopflow.backend.repository;

import com.shopflow.backend.util.IdGenerator;
import com.shopflow.common.model.Identifiable;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.concurrent.ConcurrentHashMap;
import java.util.function.Consumer;
import java.util.function.Predicate;

/**
 * Thread-safe in-memory store for one entity type. A change listener can
 * be attached so that a persistence layer is notified after every write.
 */
public abstract class InMemoryRepository<T extends Identifiable> {

    private final Map<String, T> store = new ConcurrentHashMap<>();
    private final String idPrefix;
    private Consumer<InMemoryRepository<T>> changeListener = repo -> { };

    protected InMemoryRepository(String idPrefix) {
        this.idPrefix = idPrefix;
    }

    /** Short name used for the persistence file, e.g. "products". */
    public abstract String getName();

    /** Rebuilds an entity from its JSON map, used when loading from disk. */
    public abstract T fromJson(Map<String, Object> map);

    public void setChangeListener(Consumer<InMemoryRepository<T>> listener) {
        this.changeListener = listener == null ? repo -> { } : listener;
    }

    public List<T> findAll() {
        List<T> all = new ArrayList<>(store.values());
        all.sort(Comparator.comparing(Identifiable::getId));
        return all;
    }

    public List<T> findWhere(Predicate<T> predicate) {
        List<T> matches = new ArrayList<>();
        for (T entity : store.values()) {
            if (predicate.test(entity)) {
                matches.add(entity);
            }
        }
        matches.sort(Comparator.comparing(Identifiable::getId));
        return matches;
    }

    public Optional<T> findFirst(Predicate<T> predicate) {
        return store.values().stream().filter(predicate).findFirst();
    }

    public Optional<T> findById(String id) {
        return id == null ? Optional.empty() : Optional.ofNullable(store.get(id));
    }

    public boolean exists(String id) {
        return id != null && store.containsKey(id);
    }

    /**
     * Stores the entity and notifies the change listener. If the listener
     * fails (for example the disk write fails) the in-memory change is rolled
     * back so memory and disk never disagree, and the failure is rethrown.
     */
    public T save(T entity) {
        boolean isNew = entity.getId() == null || entity.getId().isBlank();
        if (isNew) {
            entity.setId(IdGenerator.next(idPrefix));
        }
        T previous = store.put(entity.getId(), entity);
        try {
            changeListener.accept(this);
        } catch (RuntimeException e) {
            if (previous == null) {
                store.remove(entity.getId());
                if (isNew) {
                    entity.setId(null);
                }
            } else {
                store.put(entity.getId(), previous);
            }
            throw e;
        }
        return entity;
    }

    public boolean delete(String id) {
        if (id == null) {
            return false;
        }
        T removed = store.remove(id);
        if (removed == null) {
            return false;
        }
        try {
            changeListener.accept(this);
        } catch (RuntimeException e) {
            store.put(id, removed);
            throw e;
        }
        return true;
    }

    public int count() {
        return store.size();
    }

    public boolean isEmpty() {
        return store.isEmpty();
    }

    /** Replaces the full content without firing the change listener. */
    public void loadAll(List<T> entities) {
        store.clear();
        for (T entity : entities) {
            if (entity.getId() != null) {
                store.put(entity.getId(), entity);
                IdGenerator.bumpPast(entity.getId());
            }
        }
    }

    public List<Object> toJsonList() {
        List<Object> list = new ArrayList<>();
        for (T entity : findAll()) {
            list.add(entity.toJson());
        }
        return list;
    }
}
