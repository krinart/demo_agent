from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4


@dataclass
class Task:
    title: str
    description: str = ""
    status: str = "open"
    created_at: datetime = field(default_factory=datetime.now)
    task_id: str = field(default_factory=lambda: uuid4().hex[:8])

    def close(self):
        self.status = "closed"

    def reopen(self):
        self.status = "open"

    def __str__(self):
        return f"[{self.status.upper()}] {self.title}"
