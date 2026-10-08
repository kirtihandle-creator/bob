import tempfile
import unittest
from pathlib import Path

from task_manager.storage import TaskStore


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


if __name__ == "__main__":
    unittest.main()
