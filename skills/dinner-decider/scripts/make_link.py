#!/usr/bin/env python3
"""Build a shareable "What's For Dinner" voting link with tonight's ideas preloaded.

Usage:
  python3 make_link.py "Chicken stir fry" "Leftover chili mac"          # adds to the standard menu
  python3 make_link.py --only "Chicken stir fry" "Breakfast burritos"   # vote on just these
"""
import argparse
import base64
import datetime
import json

BASE_URL = "https://kalston96.github.io/dinner/"


def build_link(ideas, only=False):
    state = {
        "v": 1,
        "d": datetime.date.today().isoformat(),
        "c": [{"id": f"c{i}", "n": name.strip()} for i, name in enumerate(ideas) if name.strip()],
        "a": None,
        "b": None,
        "f": None,
    }
    if only:
        state["o"] = True
    raw = json.dumps(state, separators=(",", ":"), ensure_ascii=False).encode()
    return BASE_URL + "#" + base64.urlsafe_b64encode(raw).decode().rstrip("=")


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("ideas", nargs="*", help="Dinner ideas to add for tonight")
    p.add_argument("--only", action="store_true", help="Vote on only these ideas, not the standard menu")
    args = p.parse_args()
    if args.only and not args.ideas:
        p.error("--only needs at least one idea")
    print(build_link(args.ideas, args.only))
