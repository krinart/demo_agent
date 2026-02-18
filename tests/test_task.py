from tasklib import Task


def test_create_task():
    t = Task(title="Write docs")
    assert t.title == "Write docs"
    assert t.status == "open"


def test_close_task():
    t = Task(title="Fix bug")
    t.close()
    assert t.status == "closed"


def test_reopen_task():
    t = Task(title="Fix bug")
    t.close()
    t.reopen()
    assert t.status == "open"


def test_invalid_status_raises():
    import pytest
    with pytest.raises(ValueError, match="Invalid status"):
        Task(title="Bad", status="unknown")


def test_start_task():
    t = Task(title="Work item")
    t.start()
    assert t.status == "in_progress"
