"""Run with: python main.py"""

import argparse
from pathlib import Path

from task_manager.app import TaskManager


def main():
    parser = argparse.ArgumentParser(description="Everyday Tasks: a Python desktop task manager")
    parser.add_argument("--database", type=Path, default=Path(__file__).parent / "data" / "tasks.db",
                        help="SQLite database location")
    args = parser.parse_args()
    TaskManager(args.database).mainloop()


if __name__ == "__main__":
    main()
