"""The task log: one line per outcome, in plain words, for Irfan.

Tasks live in ops/progress/tasks.jsonl, one JSON object per line. Anything only
Irfan can do (buy, pay, create an account, type a password, approve wording) is
recorded with "irfan" as the owner, so it shows under "Needs you".

Usage (run from the project folder):
    python ops/progress/task.py add foundation leader "Write the product note"
    python ops/progress/task.py add foundation irfan "Choose the site name"
    python ops/progress/task.py done 3 "Product note written: PRODUCT.md"
    python ops/progress/task.py drop 4 "No longer needed: decided against it"
    python ops/progress/task.py list                 # open tasks
    python ops/progress/task.py list --all           # everything
    python ops/progress/task.py list --owner developer
    python ops/progress/task.py needs-you            # open tasks owned by Irfan

Edit STREAMS below when the work changes shape.
"""

import argparse
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

SITE_TZ = timezone(timedelta(hours=5, minutes=30), "IST")

LOG = Path(__file__).resolve().parent / "tasks.jsonl"

# Work streams. Keep the list short; add one only when its work exists.
STREAMS = [
    "foundation",  # project folder, rules, team method, tools
    "product",     # product note, decisions, halal definitions
    "design",      # mock-ups and the stylesheet
    "recipes",     # the recipe database
    "planner",     # weekly plans, shopping list, sharing
    "ramadan",     # suhoor and iftar plans, fasting times
    "checker",     # the "is this halal?" ingredient checker
    "finder",      # restaurant data, listings, city pages
    "accounts",    # sign-in, saved items, premium switch
    "policies",    # terms, privacy, halal labelling and other policies
    "server",      # hosting, domain, email, backups, security
    "search",      # titles, markup, sitemaps, indexing
]

OWNERS = ["irfan", "leader", "developer", "tester"]


def now_text() -> str:
    return datetime.now(SITE_TZ).strftime("%Y-%m-%d %H:%M IST")


def load() -> list[dict]:
    if not LOG.exists():
        return []
    tasks = []
    for line in LOG.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            tasks.append(json.loads(line))
    return tasks


def save(tasks: list[dict]) -> None:
    lines = [json.dumps(task, ensure_ascii=False) for task in tasks]
    LOG.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")


def find(tasks: list[dict], task_id: int) -> dict:
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise SystemExit(f"No task with number {task_id}.")


def show(tasks: list[dict]) -> None:
    if not tasks:
        print("Nothing here.")
        return
    for task in tasks:
        line = f"{task['id']:>3}  [{task['status']}]  {task['stream']}  {task['owner']}: {task['text']}"
        if task.get("outcome"):
            line += f"  ->  {task['outcome']}"
        print(line)


def main() -> int:
    parser = argparse.ArgumentParser(description="The task log.")
    sub = parser.add_subparsers(dest="command", required=True)

    add = sub.add_parser("add", help="add a task")
    add.add_argument("stream", choices=STREAMS)
    add.add_argument("owner", choices=OWNERS)
    add.add_argument("text")

    for name in ("done", "drop"):
        close = sub.add_parser(name, help=f"mark a task {name}")
        close.add_argument("id", type=int)
        close.add_argument("outcome", help="what happened, in plain words")

    listing = sub.add_parser("list", help="show tasks")
    listing.add_argument("--all", action="store_true")
    listing.add_argument("--owner", choices=OWNERS)
    listing.add_argument("--stream", choices=STREAMS)

    sub.add_parser("needs-you", help="open tasks only Irfan can do")

    args = parser.parse_args()
    tasks = load()

    if args.command == "add":
        next_id = max((t["id"] for t in tasks), default=0) + 1
        tasks.append({
            "id": next_id,
            "stream": args.stream,
            "owner": args.owner,
            "text": args.text.strip(),
            "status": "open",
            "opened": now_text(),
        })
        save(tasks)
        print(f"Task {next_id} added.")
    elif args.command in ("done", "drop"):
        task = find(tasks, args.id)
        task["status"] = "done" if args.command == "done" else "dropped"
        task["outcome"] = args.outcome.strip()
        task["closed"] = now_text()
        save(tasks)
        print(f"Task {args.id} marked {task['status']}.")
    elif args.command == "list":
        chosen = tasks if args.all else [t for t in tasks if t["status"] == "open"]
        if args.owner:
            chosen = [t for t in chosen if t["owner"] == args.owner]
        if args.stream:
            chosen = [t for t in chosen if t["stream"] == args.stream]
        show(chosen)
    elif args.command == "needs-you":
        show([t for t in tasks if t["status"] == "open" and t["owner"] == "irfan"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
