import unittest

from gradescope_utils.autograder_utils.decorators import weight, visibility

try:
    from solution.count_exact_match import count_exact_match
except Exception:
    raise Exception(f'Couldnt import your function validate_email from files. Please double check your file name and function name.') from None


class test_count_exact_match(unittest.TestCase):
    def assert_equal_with_message(self, test_name, expected, actual):
        try:
            self.assertEqual(actual, expected)
        except AssertionError:
            print(f"--- Failed {test_name} ---")
            print(f"Expected Output:{expected}")
            print(f"Actual Output:{actual}")
            print(f"\n--- DETAILED ERROR MESSAGE ---")
            raise

    # 28 points in total
    @weight(6)
    def test_1(self):
        stu = count_exact_match("severussnape", "alanrickman")
        self.assert_equal_with_message("Test count_exact_match 1: severussnape, alanrickman", 2, stu)

    @weight(6)
    def test_2(self):
        stu = count_exact_match("snackaverage", "stackoverflow")
        self.assert_equal_with_message("Test count_exact_match 2: snackaverage, stackoverflow", 7, stu)

    @weight(3)
    def test_3(self):
        stu = count_exact_match("ABCDE", "ABCDE")
        self.assert_equal_with_message("Test count_exact_match 3: ABCDE, ABCDE", 5, stu)

    @weight(4)
    def test_4(self):
        stu = count_exact_match("  ABCDE  ", "ABCDE")
        self.assert_equal_with_message("Test count_exact_match 4:   ABCDE  (with spaces), ABCDE", 0, stu)

    @weight(3)
    def test_5(self):
        stu = count_exact_match("", "alonglongstring")
        self.assert_equal_with_message("Test count_exact_match 5: empty string, alonglongstring", 0, stu)

    @weight(3)
    def test_6(self):
        stu = count_exact_match("", "")
        self.assert_equal_with_message("Test count_exact_match 6: two empty strings", 0, stu)

    @weight(3)
    def test_7(self):
        stu = count_exact_match("racecar", "RACECAR")
        self.assert_equal_with_message("Test count_exact_match 7: racecar, RACECAR", 0, stu)


if __name__ == '__main__':
    unittest.main()
