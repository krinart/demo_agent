from tasklib import Task, TaskStore


def test_store_add_and_get():
    store = TaskStore()
    t = Task(title="Test task", task_id="abc123")
    store.add(t)
    assert store.get("abc123") is t


def test_store_all():
    store = TaskStore()
    store.add(Task(title="A"))
    store.add(Task(title="B"))
    assert len(store.all()) == 2
