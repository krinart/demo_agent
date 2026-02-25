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


def test_filter_tasks_by_status():
    p = Project(name="Demo")
    p.add_task(Task(title="A"))
    p.add_task(Task(title="B"))
    t3 = Task(title="C")
    t3.close()
    p.add_task(t3)
    assert len(p.filter_tasks(status="open")) == 2
    assert len(p.filter_tasks(status="closed")) == 1


def test_filter_tasks_by_predicate():
    p = Project(name="Demo")
    p.add_task(Task(title="Important bug"))
    p.add_task(Task(title="Minor tweak"))
    result = p.filter_tasks(predicate=lambda t: "bug" in t.title.lower())
    assert len(result) == 1
    assert result[0].title == "Important bug"


def test_empty_project_name_raises():
    import pytest
    with pytest.raises(ValueError, match="cannot be empty"):
        Project(name="")


def test_whitespace_project_name_raises():
    import pytest
    with pytest.raises(ValueError, match="cannot be empty"):
        Project(name="   ")


def test_project_name_stripped():
    p = Project(name="  My Project  ")
    assert p.name == "My Project"


def test_summary():
    p = Project(name="Demo")
    p.add_task(Task(title="Open task"))
    t2 = Task(title="Done task")
    t2.close()
    p.add_task(t2)
    assert p.summary() == "Project(Demo, 1 open / 2 total)"
    assert str(p) == p.summary()
