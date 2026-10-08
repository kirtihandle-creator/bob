# Everyday Tasks

A desktop task manager written entirely in Python, using Tkinter for the interface
and SQLite for persistent storage. No pip dependencies or online services are required.

## Run

Requires Python 3.10 or newer with Tkinter (included with the standard Windows Python installer).
From this project directory:

```powershell
python main.py
```

Create tasks with a title, notes, priority, and optional due date in `YYYY-MM-DD`
format. Select a task to edit, complete, reopen, or delete it. Search matches titles
and notes; the status filter shows all, active, or completed tasks. Tasks are sorted
by completion, priority, then due date. Click **Save task** to persist edits before
selecting another task or changing filters; edits are not autosaved.

Keyboard shortcuts: **Ctrl+N** creates a new task; **Ctrl+S** saves the form.

Your data is saved locally in `data/tasks.db`. To back it up, close the app and copy
that file. You may choose another location:

```powershell
python main.py --database "E:\my-tasks.db"
```

## Check

```powershell
python -m unittest discover -s tests -v
```

## Project structure

- `main.py`: application entry point and database option.
- `task_manager/app.py`: desktop interface and actions.
- `task_manager/storage.py`: validation and SQLite persistence.
- `tests/test_storage.py`: lifecycle, validation, search, and persistence tests.

This is a local, single-user application. A desktop display is required to run the
interface. On Linux, Tkinter may require your distribution's `python3-tk` package.
