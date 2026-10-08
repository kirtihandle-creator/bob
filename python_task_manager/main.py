"""Run with: python main.py"""

import argparse
from importlib import import_module
from pathlib import Path

from task_manager.storage import TaskStore


def workflow_names():
    folder = Path(__file__).parent / "task_manager" / "workflows"
    return sorted(path.stem for path in folder.glob("*.py"))


def load_workflow(name):
    if name not in workflow_names():
        raise ValueError(f"Unknown workflow: {name}")
    return import_module(f"task_manager.workflows.{name}")


def import_workflow(database, name, start_date=None):
    tasks = load_workflow(name).build_tasks(start_date)
    store = TaskStore(database)
    try:
        with store.connection:
            store.connection.executemany(
                "INSERT INTO tasks (title, notes, priority, due_date) VALUES (?, ?, ?, ?)",
                [(t["title"], t["notes"], t["priority"], t["due_date"]) for t in tasks],
            )
    finally:
        store.close()
    return len(tasks)


def main():
    parser = argparse.ArgumentParser(description="Everyday Tasks: a Python desktop task manager")
    parser.add_argument("--database", type=Path, default=Path(__file__).parent / "data" / "tasks.db",
                        help="SQLite database location")
    actions = parser.add_mutually_exclusive_group()
    actions.add_argument("--list-workflows", action="store_true", help="List the 100 built-in workflows")
    actions.add_argument("--import-workflow", metavar="NAME", help="Add a workflow's tasks and exit")
    parser.add_argument("--start-date", help="Workflow start date as YYYY-MM-DD (defaults to today)")
    args = parser.parse_args()
    if args.start_date and not args.import_workflow:
        parser.error("--start-date requires --import-workflow")
    if args.list_workflows:
        for name in workflow_names():
            workflow = load_workflow(name)
            print(f"{name}: {workflow.NAME}")
        return
    if args.import_workflow:
        try:
            count = import_workflow(args.database, args.import_workflow, args.start_date)
        except (ValueError, OverflowError) as error:
            parser.error(str(error))
        print(f"Imported {count} tasks from {args.import_workflow}.")
        return
    from task_manager.app import TaskManager
    TaskManager(args.database).mainloop()



if __name__ == "__main__":
    main()


import React from "react";

function App() {
  return (
    <div>
      <h1>Hello, React!</h1>
      <p>This is a simple TSX component.</p>
      <button onClick={() => alert("Button clicked!")}>
        Click Me
      </button>
    </div>
  );
}
import React, { useState } from "react";

export default function App() {
  const [count, setCount] = useState(0);

  return (
    <main
      style={{
        minHeight: "100vh",
        display: "grid",
        placeItems: "center",
        background: "#0f172a",
        color: "white",
        fontFamily: "system-ui, sans-serif",
      }}
    >
      <div style={{ textAlign: "center" }}>
        <h1>My React App</h1>

        <p>Count: {count}</p>

        <button
          onClick={() => setCount((value) => value + 1)}
          style={{
            padding: "10px 18px",
            border: 0,
            borderRadius: 8,
            background: "#3b82f6",
            color: "white",
            cursor: "pointer",
            fontSize: 16,
          }}
        >
          Click me
        </button>
      </div>
    </main>
  );
}