from tasklib import Task, Project


def test_create_project():
    p = Project(name="Demo")
    assert p.name == "Demo"
    assert len(p.tasks) == 0


def test_add_task_to_project():
    p = Project(name="Demo")
    t = Task(title="Setup CI")
    p.add_task(t)
    assert len(p.tasks) == 1


def test_get_open_tasks():
    p = Project(name="Demo")
    t1 = Task(title="Open task")
    t2 = Task(title="Closed task")
    t2.close()
    p.add_task(t1)
    p.add_task(t2)
    assert len(p.get_open_tasks()) == 1
    assert len(p.get_closed_tasks()) == 1
