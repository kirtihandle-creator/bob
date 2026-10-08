"""Validated task storage backed by SQLite."""

from datetime import date
from pathlib import Path
import sqlite3


class TaskStore:
    def __init__(self, path: str | Path):
        if str(path) != ":memory:":
            Path(path).parent.mkdir(parents=True, exist_ok=True)
        self.connection = sqlite3.connect(path)
        self.connection.row_factory = sqlite3.Row
        self.connection.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                notes TEXT NOT NULL DEFAULT '',
                priority TEXT NOT NULL CHECK(priority IN ('Low', 'Normal', 'High')),
                due_date TEXT NOT NULL DEFAULT '',
                completed INTEGER NOT NULL DEFAULT 0,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.connection.commit()

    def save(self, title, notes="", priority="Normal", due_date="", task_id=None):
        title, due_date = title.strip(), due_date.strip()
        if not title:
            raise ValueError("Please enter a task title.")
        if priority not in ("Low", "Normal", "High"):
            raise ValueError("Choose Low, Normal, or High priority.")
        if due_date:
            try:
                parsed = date.fromisoformat(due_date)
                if parsed.isoformat() != due_date:
                    raise ValueError
            except ValueError:
                raise ValueError("Use YYYY-MM-DD for the due date, or leave it empty.") from None
        with self.connection:
            values = (title, notes.strip(), priority, due_date)
            if task_id is None:
                cursor = self.connection.execute(
                    "INSERT INTO tasks (title, notes, priority, due_date) VALUES (?, ?, ?, ?)",
                    values,
                )
                return cursor.lastrowid
            self.connection.execute(
                "UPDATE tasks SET title=?, notes=?, priority=?, due_date=? WHERE id=?",
                (*values, task_id),
            )
            return task_id

    def list_tasks(self, search="", status="All"):
        conditions, values = [], []
        if search.strip():
            conditions.append("(instr(lower(title), lower(?)) > 0 OR instr(lower(notes), lower(?)) > 0)")
            values.extend([search.strip()] * 2)
        if status in ("Active", "Completed"):
            conditions.append("completed=?")
            values.append(int(status == "Completed"))
        where = " WHERE " + " AND ".join(conditions) if conditions else ""
        return self.connection.execute(
            "SELECT * FROM tasks" + where + " ORDER BY completed, "
            "CASE priority WHEN 'High' THEN 0 WHEN 'Normal' THEN 1 ELSE 2 END, "
            "CASE WHEN due_date='' THEN 1 ELSE 0 END, due_date, id DESC",
            values,
        ).fetchall()

    def toggle(self, task_id):
        with self.connection:
            self.connection.execute("UPDATE tasks SET completed=1-completed WHERE id=?", (task_id,))

    def delete(self, task_id):
        with self.connection:
            self.connection.execute("DELETE FROM tasks WHERE id=?", (task_id,))

    def close(self):
        self.connection.close()
