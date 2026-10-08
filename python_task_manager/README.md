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

## Built-in workflows

The `task_manager/workflows` directory contains exactly **115 Python files of 100
nonblank lines each** (11,500 lines total). The original ten project categories
cover ten phases, from discovery to retrospective. Event, podcast, and gardening
projects each add planning, design, implementation, validation, and delivery workflows. Each module
provides twelve task templates, `build_tasks(start_date=None)`, and `summary()`.
The code includes template data; these are reusable modules within one application.

List the available workflows or import one into your task database:

```powershell
python main.py --list-workflows
python main.py --import-workflow python_app_planning --start-date 2026-10-08
python main.py
```

Imports exit without opening the desktop interface. The start date defaults to
today, with two tasks per day over six days. Each import adds a fresh set of tasks;
importing the same workflow again creates duplicates. Use `--database` to select
a different database for an import. Workflow commands do not require Tkinter.

## Tests

```powershell
python -m unittest discover -s tests -v
```

## Project structure

- `main.py`: application entry point and database option.
- `task_manager/app.py`: desktop interface and actions.
- `task_manager/storage.py`: validation and SQLite persistence.
- `tests/test_storage.py`: lifecycle, validation, search, and persistence tests.
- `task_manager/workflows/`: 115 reusable workflow modules, each exactly 100 lines.

This is a local, single-user application. A desktop display is required to run the
interface. On Linux, Tkinter may require your distribution's `python3-tk` package.
