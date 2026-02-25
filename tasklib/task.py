from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4


VALID_STATUSES = {"open", "closed", "in_progress"}


@dataclass
class Task:
    title: str
    description: str = ""
    status: str = "open"
    created_at: datetime = field(default_factory=datetime.now)
    task_id: str = field(default_factory=lambda: uuid4().hex[:8])

    def __post_init__(self):
        if self.status not in VALID_STATUSES:
            raise ValueError(
                f"Invalid status '{self.status}'. Must be one of: {VALID_STATUSES}"
            )

    def close(self):
        self.status = "closed"

    def reopen(self):
        self.status = "open"

    def start(self):
        self.status = "in_progress"

    def __str__(self):
        return f"[{self.status.upper()}] {self.title}"
