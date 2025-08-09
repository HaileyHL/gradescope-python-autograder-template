#!/usr/bin/env python3
import argparse
import os
import sys
from pathlib import Path
import unittest

from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner

RESULTS_PATH = "/autograder/results/results.json"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--assignment", required=True)
    parser.add_argument("--solution-dir", required=True)
    args = parser.parse_args()

    solution_dir = Path(args.solution_dir).resolve()
    assign_dir = solution_dir.parent

    # Make assignment dir and solution dir importable for tests like:
    #   from solution.solution import Foo   OR   from solution import Foo
    sys.path.insert(0, str(assign_dir))
    sys.path.insert(0, str(solution_dir))
    os.environ["PYTHONPATH"] = os.pathsep.join(sys.path)

    # Discover tests in the assignment folder
    suite = unittest.defaultTestLoader.discover(start_dir=str(assign_dir), pattern="test_*.py")

    # Ensure results directory exists
    Path(RESULTS_PATH).parent.mkdir(parents=True, exist_ok=True)

    with open(RESULTS_PATH, "w") as f:
        JSONTestRunner(visibility="visible", stream=f).run(suite)

if __name__ == "__main__":
    main()
