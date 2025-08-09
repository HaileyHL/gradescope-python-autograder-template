import argparse
import unittest

from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('.')

    # 1. Run tests and show on stdout (for debugging)
    unittest.TextTestRunner(stream=sys.stdout, verbosity=2).run(suite)

    with open('/autograder/results/results.json', 'w') as f:
        JSONTestRunner(visibility='visible', stream=f).run(suite)
