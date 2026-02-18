from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, List, Optional

from tasklib.task import Task


@dataclass
class Project:
    name: str
    tasks: list[Task] = field(default_factory=list)

    def __post_init__(self):
        if not self.name or not self.name.strip():
            raise ValueError("Project name cannot be empty")
        self.name = self.name.strip()

    def add_task(self, task: Task):
        self.tasks.append(task)

    def filter_tasks(
        self,
        status: Optional[str] = None,
        predicate: Optional[Callable[[Task], bool]] = None,
    ) -> list[Task]:
        """Filter tasks by status and/or custom predicate."""
        results = self.tasks
        if status is not None:
            results = [t for t in results if t.status == status]
        if predicate is not None:
            results = [t for t in results if predicate(t)]
        return results

    def get_open_tasks(self):
        return self.filter_tasks(status="open")

    def get_closed_tasks(self):
        return self.filter_tasks(status="closed")

    def summary(self) -> str:
        """Return a summary including open task count."""
        open_count = len(self.filter_tasks(status="open"))
        return f"Project({self.name}, {open_count} open / {len(self.tasks)} total)"

    def __str__(self):
        return self.summary()
