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
