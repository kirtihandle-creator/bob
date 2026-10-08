"""Tkinter desktop interface."""

import tkinter as tk
from tkinter import messagebox, ttk

from .storage import TaskStore


class TaskManager(tk.Tk):
    def __init__(self, database):
        super().__init__()
        self.title("Everyday Tasks")
        self.geometry("1000x650")
        self.minsize(780, 520)
        self.store = TaskStore(database)
        self.editing_id = None
        self.rows = {}
        self.protocol("WM_DELETE_WINDOW", self.close)
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("TFrame", background="#f3f5f9")
        style.configure("TLabel", background="#f3f5f9", font=("Segoe UI", 10))
        style.configure("Title.TLabel", font=("Segoe UI", 24, "bold"))
        style.configure("TButton", padding=(12, 7))
        style.configure("Treeview", rowheight=32, font=("Segoe UI", 10))
        style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))

        page = ttk.Frame(self, padding=24)
        page.pack(fill="both", expand=True)
        ttk.Label(page, text="Everyday Tasks", style="Title.TLabel").pack(anchor="w")
        ttk.Label(page, text="Plan your day. Keep track of what matters.").pack(anchor="w", pady=(0, 18))
        controls = ttk.Frame(page)
        controls.pack(fill="x", pady=(0, 12))
        ttk.Label(controls, text="Search").pack(side="left", padx=(0, 8))
        self.search = tk.StringVar()
        ttk.Entry(controls, textvariable=self.search, width=35).pack(side="left")
        self.status = tk.StringVar(value="All")
        ttk.Combobox(controls, textvariable=self.status, values=("All", "Active", "Completed"),
                     state="readonly", width=12).pack(side="left", padx=10)
        ttk.Button(controls, text="New task", command=self.new).pack(side="right")

        content = ttk.Frame(page)
        content.pack(fill="both", expand=True)
        content.columnconfigure(0, weight=1)
        content.rowconfigure(0, weight=1)
        table = ttk.Frame(content)
        table.grid(row=0, column=0, sticky="nsew", padx=(0, 20))
        self.tree = ttk.Treeview(table, columns=("title", "priority", "due", "status"),
                                 show="headings", selectmode="browse")
        for column, label, width in (("title", "Task", 220), ("priority", "Priority", 75),
                                     ("due", "Due date", 100), ("status", "Status", 90)):
            self.tree.heading(column, text=label)
            self.tree.column(column, width=width, minwidth=60)
        scrollbar = ttk.Scrollbar(table, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.tree.pack(fill="both", expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.select)
        self.tree.tag_configure("done", foreground="#6b7280")

        form = ttk.Frame(content, width=250)
        form.grid(row=0, column=1, sticky="ns")
        self.heading = tk.StringVar(value="New task")
        ttk.Label(form, textvariable=self.heading, font=("Segoe UI", 14, "bold")).pack(anchor="w", pady=(0, 12))
        self.title_value = tk.StringVar()
        self.priority = tk.StringVar(value="Normal")
        self.due = tk.StringVar()
        ttk.Label(form, text="Title *").pack(anchor="w")
        self.title_entry = ttk.Entry(form, textvariable=self.title_value, width=28)
        self.title_entry.pack(fill="x", pady=(4, 12))
        ttk.Label(form, text="Priority").pack(anchor="w")
        ttk.Combobox(form, textvariable=self.priority, values=("Low", "Normal", "High"),
                     state="readonly").pack(fill="x", pady=(4, 12))
        ttk.Label(form, text="Due date (YYYY-MM-DD)").pack(anchor="w")
        ttk.Entry(form, textvariable=self.due).pack(fill="x", pady=(4, 12))
        ttk.Label(form, text="Notes").pack(anchor="w")
        self.notes = tk.Text(form, height=6, width=28, wrap="word", font=("Segoe UI", 10), undo=True)
        self.notes.pack(fill="both", expand=True, pady=(4, 12))
        ttk.Button(form, text="Save task", command=self.save).pack(fill="x")
        self.toggle_button = ttk.Button(form, text="Mark completed / active", command=self.toggle, state="disabled")
        self.toggle_button.pack(fill="x", pady=6)
        self.delete_button = ttk.Button(form, text="Delete task", command=self.delete, state="disabled")
        self.delete_button.pack(fill="x")
        self.summary = tk.StringVar()
        ttk.Label(page, textvariable=self.summary).pack(anchor="w", pady=(14, 0))
        self.search.trace_add("write", lambda *_: self.refresh())
        self.status.trace_add("write", lambda *_: self.refresh())
        self.bind("<Control-n>", lambda _: self.new())
        self.bind("<Control-s>", lambda _: self.save())
        self.refresh()

    def refresh(self):
        selected = self.editing_id
        self.tree.delete(*self.tree.get_children())
        tasks = self.store.list_tasks(self.search.get(), self.status.get())
        self.rows = {task["id"]: task for task in tasks}
        for task in tasks:
            self.tree.insert("", "end", iid=str(task["id"]), values=(task["title"], task["priority"],
                             task["due_date"] or "—", "Completed" if task["completed"] else "Active"),
                             tags=("done",) if task["completed"] else ())
        if selected in self.rows:
            self.tree.selection_set(str(selected))
        elif selected is not None:
            self.new()
        all_tasks = self.store.list_tasks()
        completed = sum(task["completed"] for task in all_tasks)
        self.summary.set(f"{len(all_tasks) - completed} active  •  {completed} completed  •  {len(tasks)} shown"
                         if all_tasks else "No tasks yet. Add your first task using the form.")

    def new(self):
        self.editing_id = None
        self.tree.selection_remove(*self.tree.selection())
        self.heading.set("New task")
        self.title_value.set("")
        self.priority.set("Normal")
        self.due.set("")
        self.notes.delete("1.0", "end")
        self.toggle_button.configure(state="disabled")
        self.delete_button.configure(state="disabled")
        self.title_entry.focus_set()

    def select(self, _event=None):
        selection = self.tree.selection()
        if not selection:
            return
        task = self.rows[int(selection[0])]
        self.editing_id = task["id"]
        self.heading.set("Edit task")
        self.title_value.set(task["title"])
        self.priority.set(task["priority"])
        self.due.set(task["due_date"])
        self.notes.delete("1.0", "end")
        self.notes.insert("1.0", task["notes"])
        self.toggle_button.configure(state="normal")
        self.delete_button.configure(state="normal")

    def save(self):
        try:
            self.store.save(self.title_value.get(), self.notes.get("1.0", "end-1c"),
                            self.priority.get(), self.due.get(), self.editing_id)
        except ValueError as error:
            messagebox.showerror("Check your task", str(error), parent=self)
            return
        self.new()
        self.refresh()

    def toggle(self):
        if self.editing_id is not None:
            self.store.toggle(self.editing_id)
            self.refresh()

    def delete(self):
        if self.editing_id is not None and messagebox.askyesno(
                "Delete task", "Permanently delete this task?", parent=self):
            self.store.delete(self.editing_id)
            self.new()
            self.refresh()

    def close(self):
        self.store.close()
        self.destroy()
