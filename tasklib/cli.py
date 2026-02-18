from __future__ import annotations

import argparse

from tasklib import Task, TaskStore


def main():
    parser = argparse.ArgumentParser(description="Task management CLI")
    sub = parser.add_subparsers(dest="command")

    add_p = sub.add_parser("add", help="Add a new task")
    add_p.add_argument("title")
    add_p.add_argument("--desc", default="")

    sub.add_parser("list", help="List all tasks")

    args = parser.parse_args()
    store = TaskStore()
    store.load()

    if args.command == "add":
        t = Task(title=args.title, description=args.desc)
        store.add(t)
        store.save()
        print(f"Created: {t}")
    elif args.command == "list":
        for t in store.all():
            print(t)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
