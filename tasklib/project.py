from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from tasklib.task import Task


@dataclass
class Project:
    name: str
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        self.tasks.append(task)

    def get_open_tasks(self):
        return [t for t in self.tasks if t.status == "open"]

    def get_closed_tasks(self):
        return [t for t in self.tasks if t.status == "closed"]

    def __str__(self):
        return f"Project({self.name}, {len(self.tasks)} tasks)"
