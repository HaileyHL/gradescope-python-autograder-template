import unittest

from gradescope_utils.autograder_utils.decorators import weight, visibility

try:
    from solution.count_exact_match import count_exact_match
except Exception:
    raise Exception(f'Couldnt import your function validate_email from files. Please double check your file name and function name.') from None


class test_count_exact_match(unittest.TestCase):

    def run_count_exact_match(self, inputs):
        try:
            stu = count_exact_match(inputs[0], inputs[1])
            return stu
        except Exception as e:
            print(f"Error calling function with the parameters {inputs}.")
            print("Please double check your implementation.")
            print(f"\n--- DETAILED ERROR MESSAGE ---")
            raise


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
        inputs = ("severussnape", "alanrickman")
        stu = self.run_count_exact_match(inputs)
        self.assert_equal_with_message("Test count_exact_match 1: severussnape, alanrickman", 2, stu)

    @weight(6)
    def test_2(self):
        inputs = ("snackaverage", "stackoverflow")
        stu = self.run_count_exact_match(inputs)
        self.assert_equal_with_message("Test count_exact_match 2: snackaverage, stackoverflow", 7, stu)

    @weight(3)
    def test_3(self):
        inputs = ("ABCDE", "ABCDE")
        stu = self.run_count_exact_match(inputs)
        self.assert_equal_with_message("Test count_exact_match 3: ABCDE, ABCDE", 5, stu)

    @weight(4)
    def test_4(self):
        inputs = ("  ABCDE  ", "ABCDE")
        stu = self.run_count_exact_match(inputs)
        self.assert_equal_with_message("Test count_exact_match 4:   ABCDE  (with spaces), ABCDE", 0, stu)

    @weight(3)
    def test_5(self):
        inputs = ("", "alonglongstring")
        stu = self.run_count_exact_match(inputs)
        self.assert_equal_with_message("Test count_exact_match 5: empty string, alonglongstring", 0, stu)

    @weight(3)
    def test_6(self):
        inputs = ("", "")
        stu = self.run_count_exact_match(inputs)
        self.assert_equal_with_message("Test count_exact_match 6: two empty strings", 0, stu)

    @weight(3)
    def test_7(self):
        inputs = ("racecar", "RACECAR")
        stu = self.run_count_exact_match(inputs)
        self.assert_equal_with_message("Test count_exact_match 7: racecar, RACECAR", 0, stu)


if __name__ == '__main__':
    unittest.main()
