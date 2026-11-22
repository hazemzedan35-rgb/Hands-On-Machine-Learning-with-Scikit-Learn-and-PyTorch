#!/usr/bin/env python3
"""Simple, standard-library CLI for an honest book-long learning journal.

Commands:
    python scripts/journey.py new --chapter 2 --title "Working with Real Data"
    python scripts/journey.py mark --day 3 --status notes
    python scripts/journey.py chapter --chapter 1 --status complete
    python scripts/journey.py refresh
"""

import argparse
from datetime import date
import json
from pathlib import Path
import re
import sys
import unicodedata
import uuid

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "docs" / "progress.json"


def read_data():
    return json.loads(DATA_FILE.read_text(encoding="utf-8"))


def save_data(data):
    DATA_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def slugify(value):
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii").lower()
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", value)).strip("-") or "new-topic"


def chapter_by_number(data, number):
    for chapter in data["chapters"]:
        if chapter["number"] == number:
            return chapter
    raise ValueError(f"Unknown chapter {number}; use 1 through 19")


def replace_region(path, tag, content):
    text = path.read_text(encoding="utf-8")
    start = f"<!-- {tag}:START -->"
    end = f"<!-- {tag}:END -->"
    if text.count(start) != 1 or text.count(end) != 1:
        raise ValueError(f"Missing or duplicate markers in {path}: {start}, {end}")
    before, after_start = text.split(start, 1)
    _, after = after_start.split(end, 1)
    path.write_text(before + start + "\n" + content.rstrip() + "\n" + end + after, encoding="utf-8")


def chapter_status(data, number):
    if number in data["completed_chapters"]:
        return "✅ Complete"
    relevant = [day for day in data["days"] if day["chapter"] == number]
    if any(day["status"] in ("notes", "complete") for day in relevant):
        return "📝 In progress"
    if relevant:
        return "🗓️ Planned day"
    return "⏳ Not started"


def day_status(day):
    return {"draft":"🗓️ Draft", "notes":"📝 Notes written", "complete":"✅ Complete"}[day["status"]]


def refresh(data):
    lines = ["| Chapter | Topic | Status | Logged sessions |", "| --- | --- | --- | ---: |"]
    for chapter in data["chapters"]:
        n = chapter["number"]
        count = sum(day["chapter"] == n for day in data["days"])
        lines.append(f"| {n:02d} | [{chapter['title']}](chapters/{chapter['folder']}/README.md) | {chapter_status(data, n)} | {count} |")
    replace_region(ROOT / "README.md", "CHAPTERS", "\n".join(lines))
    roadmap = ["## Part I — The Fundamentals of Machine Learning (Chapters 1–8)", ""]
    for chapter in data["chapters"]:
        n = chapter["number"]
        if n == 9:
            roadmap += ["", "## Part II — Neural Networks and Deep Learning (Chapters 9–19)", ""]
        completed = "x" if n in data["completed_chapters"] else " "
        roadmap.append(f"- [{completed}] **Chapter {n:02d}:** [{chapter['title']}](../chapters/{chapter['folder']}/README.md)")
    replace_region(ROOT / "docs" / "ROADMAP.md", "ROADMAP", "\n".join(roadmap))

    lines = ["| Day | Chapter | Topic | Progress |", "| --- | --- | --- | --- |"]
    for day in sorted(data["days"], key=lambda d: d["number"]):
        n = day["number"]
        lines.append(f"| {n:02d} | {day['chapter']:02d} | [" + day["title"] + f"](days/{day['folder']}/README.md) | {day_status(day)} |")
    replace_region(ROOT / "README.md", "DAYS", "\n".join(lines))

    lines = ["| Day | Date | Chapter | Status | Practice |", "| --- | --- | --- | --- | --- |"]
    for day in sorted(data["days"], key=lambda d: d["number"]):
        practice = {"starter":"🧪 Starter lab prepared", "not-started":"—", "in-progress":"🧪 In progress", "complete":"✅ Done"}.get(day["practice"], "—")
        lines.append(f"| {day['number']:02d} | {day['date'] or '—'} | {day['chapter']:02d} | {day_status(day)} | {practice} |")
    replace_region(ROOT / "docs" / "LEARNING-LOG.md", "LOG", "\n".join(lines))

    for chapter in data["chapters"]:
        sessions = [d for d in data["days"] if d["chapter"] == chapter["number"]]
        lines = [f"- [Day {day['number']:02d} — {day['title']}](../../days/{day['folder']}/README.md) ({day_status(day)})" for day in sorted(sessions, key=lambda d:d["number"])]
        replace_region(ROOT / "chapters" / chapter["folder"] / "README.md", "DAYS", "\n".join(lines) if lines else "No study days linked yet.")


def new_day(args, data):
    chapter = chapter_by_number(data, args.chapter)
    if len(args.title) > 120 or not args.title.strip():
        raise ValueError("Use a nonempty title, up to 120 characters")
    day_num = max([d["number"] for d in data["days"]], default=0) + 1
    folder = f"day-{day_num:02d}-{slugify(args.title)}"
    dest = ROOT / "days" / folder
    if dest.exists():
        raise FileExistsError(f"Folder already exists: {dest}")
    study_date = args.date or date.today().isoformat()
    date.fromisoformat(study_date)  # Fail cleanly if invalid date

    note = (ROOT / "templates" / "DAY-TEMPLATE.md").read_text(encoding="utf-8")
    practice = (ROOT / "templates" / "EXERCISES-TEMPLATE.md").read_text(encoding="utf-8")
    replacements = {"day":day_num,"title":args.title.strip(),"date":study_date,"chapter":args.chapter,"chapter_title":chapter["title"],"chapter_folder":chapter["folder"]}
    note = note.format(**replacements)
    practice = practice.format(**replacements)
    dest.mkdir(parents=True)
    (dest / "README.md").write_text(note,encoding="utf-8")
    (dest / "exercises.md").write_text(practice,encoding="utf-8")
    if args.notebook:
        notebook = {
            "cells":[
                {"cell_type":"markdown", "metadata":{}, "id":uuid.uuid4().hex[:8],"source":[f"# Day {day_num:02d} — {args.title}\n", "\n", "Add your own explanation and hypotheses.\n"]},
                {"cell_type":"code", "metadata":{}, "id":uuid.uuid4().hex[:8], "execution_count":None, "outputs":[], "source":["# Write your experiment here\n"]}
            ],
            "metadata":{"kernelspec":{"display_name":"Python 3","language":"python","name":"python3"},"language_info":{"name":"python"}},
            "nbformat":4,"nbformat_minor":5
        }
        (dest / f"day_{day_num:02d}_experiment.ipynb").write_text(json.dumps(notebook,indent=1,ensure_ascii=False)+"\n",encoding="utf-8")
    data["days"].append({"number":day_num,"chapter":args.chapter,"title":args.title.strip(),"folder":folder,"date":study_date,"status":"draft","practice":"not-started"})
    save_data(data)
    refresh(data)
    print(f"Created Day {day_num:02d} → days/{folder}/")
    print("Next: write your notes; mark progress; git add . && git commit -m '...' && git push")


def mark_day(args, data):
    selected = next((d for d in data["days"] if d["number"] == args.day),None)
    if selected is None:
        raise ValueError(f"Day {args.day} was not found")
    selected["status"] = args.status
    if args.practice:
        selected["practice"] = args.practice
    save_data(data)
    refresh(data)
    print(f"Day {args.day:02d}: {args.status}")


def mark_chapter(args, data):
    chapter_by_number(data,args.chapter)
    comp = set(data["completed_chapters"])
    if args.status == "complete":
        comp.add(args.chapter)
    else:
        comp.discard(args.chapter)
    data["completed_chapters"] = sorted(comp)
    save_data(data)
    refresh(data)
    print(f"Chapter {args.chapter:02d}: {args.status}")


def main():
    parser = argparse.ArgumentParser(description="Maintain my book-long ML learning journey")
    subs = parser.add_subparsers(dest="command",required=True)
    new = subs.add_parser("new",help="Create a new study-day folder")
    new.add_argument("--chapter",type=int,required=True,help="1..19")
    new.add_argument("--title",required=True,help="Today's topic")
    new.add_argument("--date",default=None,help="YYYY-MM-DD; defaults to today")
    new.add_argument("--notebook",action="store_true",help="Create an empty notebook")
    mark = subs.add_parser("mark",help="Update the status of a recorded day")
    mark.add_argument("--day",type=int,required=True)
    mark.add_argument("--status",required=True,choices=("draft","notes","complete"))
    mark.add_argument("--practice",choices=("not-started","starter","in-progress","complete"))
    ch = subs.add_parser("chapter",help="Update an entire chapter's completion")
    ch.add_argument("--chapter",type=int,required=True)
    ch.add_argument("--status",required=True,choices=("in-progress","complete"))
    subs.add_parser("refresh",help="Rebuild the README and chapter links")
    args=parser.parse_args()
    try:
        data=read_data()
        if args.command=="new": new_day(args,data)
        elif args.command=="mark": mark_day(args,data)
        elif args.command=="chapter": mark_chapter(args,data)
        else:
            refresh(data)
            print("Updated README and chapter/session links")
    except (ValueError, FileExistsError, KeyError) as exc:
        parser.exit(2,f"Error: {exc}\n")


if __name__=="__main__":
    main()
