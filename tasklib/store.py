from __future__ import annotations

import json
from pathlib import Path
from typing import Optional

from tasklib.task import Task


class TaskStore:
    def __init__(self, path: str = "tasks.json"):
        self.path = Path(path)
        self._tasks: dict[str, Task] = {}

    def add(self, task: Task):
        self._tasks[task.task_id] = task

    def get(self, task_id: str) -> Optional[Task]:
        return self._tasks.get(task_id)

    def all(self) -> list[Task]:
        return list(self._tasks.values())

    def save(self):
        data = {}
        for tid, task in self._tasks.items():
            data[tid] = {
                "title": task.title,
                "description": task.description,
                "status": task.status,
                "created_at": task.created_at.isoformat(),
            }
        self.path.write_text(json.dumps(data, indent=2))

    def load(self):
        if not self.path.exists():
            return
        data = json.loads(self.path.read_text())
        for tid, info in data.items():
            task = Task(
                title=info["title"],
                description=info["description"],
                status=info["status"],
                task_id=tid,
            )
            self._tasks[tid] = task
