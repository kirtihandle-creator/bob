import tempfile
import unittest
from pathlib import Path

from task_manager.storage import TaskStore
from main import import_workflow, load_workflow, workflow_names


class TaskStoreTests(unittest.TestCase):
    def setUp(self):
        self.store = TaskStore(":memory:")
        self.addCleanup(self.store.close)

    def test_task_lifecycle(self):
        task_id = self.store.save("  Buy groceries  ", priority="High")
        self.assertEqual(self.store.list_tasks()[0]["title"], "Buy groceries")
        self.store.save("Buy vegetables", "At the market", "Low", "2026-12-01", task_id)
        self.store.toggle(task_id)
        self.assertEqual(len(self.store.list_tasks(status="Completed")), 1)
        self.assertEqual(self.store.list_tasks(status="Active"), [])
        self.store.toggle(task_id)
        self.assertEqual(self.store.list_tasks()[0]["completed"], 0)
        self.store.delete(task_id)
        self.assertEqual(self.store.list_tasks(), [])

    def test_validation(self):
        for kwargs in ({"title": " "}, {"title": "Task", "priority": "Urgent"},
                       {"title": "Task", "due_date": "2026-02-30"},
                       {"title": "Task", "due_date": "20261201"}):
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                self.store.save(**kwargs)
        self.assertEqual(self.store.list_tasks(), [])

    def test_search_filter_and_order(self):
        self.store.save("Read", "Python guide", "Low")
        self.store.save("Study PYTHON", priority="High")
        self.store.save("100% done", priority="Normal")
        self.assertEqual([t["title"] for t in self.store.list_tasks("python")], ["Study PYTHON", "Read"])
        self.assertEqual(len(self.store.list_tasks("%")), 1)
        self.assertEqual(self.store.list_tasks("' OR 1=1 --"), [])

    def test_persistence(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nested" / "tasks.db"
            first = TaskStore(path)
            first.save("Remember me")
            first.close()
            second = TaskStore(path)
            try:
                self.assertEqual(second.list_tasks()[0]["title"], "Remember me")
            finally:
                second.close()


class WorkflowTests(unittest.TestCase):
    def test_all_workflows_and_exact_file_sizes(self):
        names = workflow_names()
        self.assertEqual(len(names), 100)
        store = TaskStore(":memory:")
        self.addCleanup(store.close)
        for name in names:
            with self.subTest(workflow=name):
                module = load_workflow(name)
                lines = Path(module.__file__).read_text(encoding="utf-8").splitlines()
                self.assertEqual(len(lines), 100)
                self.assertTrue(all(line.strip() for line in lines))
                tasks = module.build_tasks("2026-12-29")
                self.assertEqual(len(tasks), 12)
                self.assertEqual(tasks[0]["due_date"], "2026-12-29")
                self.assertEqual(tasks[-1]["due_date"], "2027-01-03")
                self.assertEqual(module.summary()["id"], name)
                self.assertEqual(module.summary()["high_priority_tasks"], 3)
                tasks[0]["title"] = "Changed copy"
                self.assertNotEqual(module.build_tasks()[0]["title"], "Changed copy")
                for task in module.build_tasks("2026-12-29"):
                    store.save(**task)
        self.assertEqual(len(store.list_tasks()), 1200)

    def test_import_persists_tasks(self):
        with tempfile.TemporaryDirectory() as directory:
            database = Path(directory) / "tasks.db"
            self.assertEqual(import_workflow(database, "python_app_planning", "2026-10-08"), 12)
            store = TaskStore(database)
            try:
                self.assertEqual(len(store.list_tasks()), 12)
                self.assertTrue(all(task["title"].startswith("Python application:")
                                    for task in store.list_tasks()))
            finally:
                store.close()

    def test_invalid_import_does_not_create_database(self):
        with tempfile.TemporaryDirectory() as directory:
            database = Path(directory) / "tasks.db"
            for name, start in (("missing", None), ("python_app_planning", "2026-02-30")):
                with self.subTest(name=name, start=start), self.assertRaises(ValueError):
                    import_workflow(database, name, start)
                self.assertFalse(database.exists())


if __name__ == "__main__":
    unittest.main()
