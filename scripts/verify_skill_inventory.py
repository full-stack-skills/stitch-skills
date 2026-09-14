#!/usr/bin/env python3
import argparse
import pathlib
import re
import sys


def skill_name(skill_file: pathlib.Path) -> str:
    text = skill_file.read_text(encoding="utf-8")
    match = re.search(r"(?m)^name:\s*[\"']?([^\n\"']+)", text)
    if match is None:
        raise ValueError(f"missing name: {skill_file}")
    return match.group(1).strip()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True)
    parser.add_argument("--expected-count", required=True, type=int)
    args = parser.parse_args()
    root = pathlib.Path(args.root)
    entries = sorted(path for path in root.iterdir() if path.is_dir())
    errors = []
    for entry in entries:
        skill_file = entry / "SKILL.md"
        if not skill_file.is_file():
            errors.append(f"missing SKILL.md: {entry.name}")
            continue
        if skill_name(skill_file) != entry.name:
            errors.append(f"name mismatch: {entry.name}")
    if len(entries) != args.expected_count:
        errors.append(f"expected {args.expected_count}, found {len(entries)}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"validated {len(entries)} skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
