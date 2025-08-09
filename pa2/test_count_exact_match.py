import unittest

from gradescope_utils.autograder_utils.decorators import weight, visibility

try:
    from solution.count_exact_match import count_exact_match
except Exception as e:
    raise Exception(f'Couldnt import your function count_exact_match from files. Please double check your file name and function name.')


def assert_equal_with_message(testcase, test_name, expected, actual):
    try:
        testcase.assertEqual(actual, expected)
    except AssertionError:
        print(f"--- Failed {test_name} ---")
        print(f"Expected Output:{expected}")
        print(f"Actual Output:{actual}")
        raise


# Tests for count_exact_match
class test_count_exact_match(unittest.TestCase):
    # 30 points in total
    @weight(6)
    def test_count_exact_match_1(self):
        stu = count_exact_match("severussnape", "alanrickman")
        assert_equal_with_message(self, "Test count_exact_match 1", 2, stu)

    @weight(6)
    def test_count_exact_match_2(self):
        stu = count_exact_match("snackaverage", "stackoverflow")
        assert_equal_with_message(self, "Test count_exact_match 2", 7, stu)

    @weight(3)
    def test_count_exact_match_3(self):
        stu = count_exact_match("ABCDE", "ABCDE")
        assert_equal_with_message(self, "Test count_exact_match 3", 5, stu)

    @weight(4)
    def test_count_exact_match_4(self):
        stu = count_exact_match("  ABCDE  ", "ABCDE")
        assert_equal_with_message(self, "Test count_exact_match 4", 0, stu)

    @weight(3)
    def test_count_exact_match_5(self):
        stu = count_exact_match("", "alonglongstring")
        assert_equal_with_message(self, "Test count_exact_match 5", 0, stu)

    @weight(3)
    def test_count_exact_match_6(self):
        stu = count_exact_match("", "")
        assert_equal_with_message(self, "Test count_exact_match 6", 0, stu)

    @weight(3)
    def test_count_exact_match_7(self):
        stu = count_exact_match("racecar", "RACECAR")
        assert_equal_with_message(self, "Test count_exact_match 7", 0, stu)


if __name__ == '__main__':
    unittest.main()
