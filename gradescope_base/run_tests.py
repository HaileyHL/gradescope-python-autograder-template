#!/usr/bin/env python3
import argparse
import os
import sys
from pathlib import Path
import unittest

from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--assignment", help="assignment folder name (e.g., assignment0)")
    parser.add_argument("--solution-dir", help="absolute path to the student's solution folder")
    args = parser.parse_args()

    # Resolve directories
    if args.solution_dir:
        solution_dir = Path(args.solution_dir).resolve()
        assign_dir = solution_dir.parent
    else:
        # Backward‑compatible defaults: discover from CWD
        assign_dir = Path(".").resolve()
        # Try the common case where a 'solution' package exists next to tests
        solution_dir = assign_dir / "solution"

    # Make both the assignment folder and the solution package importable
    sys.path.insert(0, str(assign_dir))
    if solution_dir.exists():
        sys.path.insert(0, str(solution_dir))

    # Discover tests in the assignment folder (test_*.py)
    suite = unittest.defaultTestLoader.discover(start_dir=str(assign_dir), pattern="test_*.py")

    results_path = "/autograder/results/results.json"
    os.makedirs(Path(results_path).parent, exist_ok=True)
    with open(results_path, "w") as f:
        JSONTestRunner(visibility="visible", stream=f).run(suite)


if __name__ == "__main__":
    main()
