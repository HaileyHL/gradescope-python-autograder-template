import unittest

from gradescope_utils.autograder_utils.decorators import weight, visibility

try:
    from solution.validate_email import validate_email
except Exception as e:
    raise Exception(f'Couldnt import your function validate_email from files. Please double check your file name and function name.') from None


# Tests for validate_email
class test_validate_email(unittest.TestCase):

    def run_validate_email(self, inputs):
        try:
            stu = validate_email(inputs[0], inputs[1])
            return stu
        except Exception as e:
            print(f"Encountered with the parameters {inputs}.")
            print(f"ERROR: {e}")
            print("Please double check your implementation.")

    def assert_equal_with_message(self, test_name, inputs, expected, actual):
        try:
            self.assertEqual(actual, expected)
        except AssertionError:
            print(f"--- Failed {test_name} ---")
            print(f"Inputs:{inputs}")
            print(f"Expected Output:{expected}")
            print(f"Actual Output:{actual}")

    # 32 points in total
    @weight(4)
    def test_validate_email1(self):
        inputs = ("abc@gmail.com", "gmail.com")
        stu = self.run_validate_email(inputs)
        expected = True
        self.assert_equal_with_message("Test valid email 1", ("abc@gmail.com", "gmail.com"),expected, stu)

    @weight(4)
    def test_validate_email2(self):
        try:
            stu = validate_email("abcgmail.com", "gmail.com")
        except Exception:
            print(f"ERROR: {e}\nThis was encountered with the parameters{("abcgmail.com", "gmail.com")}.\nPlease double check your implementation.")
        expected = False
        self.assert_equal_with_message("Test invalid email 2",("abcgmail.com", "gmail.com"), expected, stu)

    @weight(3)
    def test_validate_email3(self):
        try:
            stu = validate_email("abc@@gmail.com", "gmail.com")
        except Exception:
            print(f"ERROR: {e}\nThis was encountered with the parameters{("abc@@gmail.com", "gmail.com")}.\nPlease double check your implementation.")
        expected = False
        self.assert_equal_with_message("Test invalid email 3", ("abc@@gmail.com", "gmail.com"), expected, stu)

    @weight(3)
    def test_validate_email4(self):
        try:
            stu = validate_email("abc@:^).com", ":^).com")
        except Exception:
            print(f"ERROR: {e}\nThis was encountered with the parameters{("abc@:^).com", ":^).com")}.\nPlease double check your implementation.")
        expected = True
        self.assert_equal_with_message("Test weird suffix", ("abc@:^).com", ":^).com"), expected, stu)

    @weight(3)
    def test_validate_email5(self):
        try:
            stu = validate_email("       abc@gmail.com", "gmail.com")
        except Exception:
            print(f"ERROR: {e}\nThis was encountered with the parameters{("       abc@gmail.com", "gmail.com")}.\nPlease double check your implementation.")
        expected = True
        self.assert_equal_with_message("Test leading spaces 5", ("       abc@gmail.com", "gmail.com"), expected, stu)

    @weight(3)
    def test_validate_email6(self):
        try:
            stu = validate_email("abc@gmail.com       ", "gmail.com")
        except Exception:
            print(f"ERROR: {e}\nThis was encountered with the parameters{("abc@gmail.com       ", "gmail.com")}.\nPlease double check your implementation.")
        expected = True
        self.assert_equal_with_message("Test trailing spaces", ("abc@gmail.com       ", "gmail.com"), expected, stu)

    @weight(3)
    def test_validate_email7(self):
        try:
            stu = validate_email("       abc@gmail.com       ", "gmail.com")
        except Exception:
            print(f"ERROR: {e}\nThis was encountered with the parameters{("       abc@gmail.com       ", "gmail.com")}.\nPlease double check your implementation.")
        expected = True
        self.assert_equal_with_message("Test both spaces 7",("       abc@gmail.com       ", "gmail.com"), expected, stu)

    @weight(3)
    def test_validate_email8(self):
        try:
            stu = validate_email("ab c@gmail.com", "gmail.com")
        except Exception:
            print(f"ERROR: {e}\nThis was encountered with the parameters{("ab c@gmail.com", "gmail.com")}.\nPlease double check your implementation.")
        expected = False
        self.assert_equal_with_message("Test spaces in the middle 8", ("ab c@gmail.com", "gmail.com"), expected, stu)

    @weight(3)
    def test_validate_email9(self):
        try:
            stu = validate_email("abc@g mail.com", "gmail.com")
        except Exception:
            print(f"ERROR: {e}\nThis was encountered with the parameters{("abc@g mail.com", "gmail.com")}.\nPlease double check your implementation.")
        expected = False
        self.assert_equal_with_message("Test spaces in the middle 9", ("abc@g mail.com", "gmail.com"), expected, stu)

    @weight(3)
    def test_validate_email10(self):
        try:
            stu = validate_email("abc@gmail.com", "ucsd.edu")
        except Exception:
            print(f"ERROR: {e}\nThis was encountered with the parameters{("abc@gmail.com", "ucsd.edu")}.\nPlease double check your implementation.")
        expected = False
        self.assert_equal_with_message("Test wrong suffix 10", ("abc@gmail.com", "ucsd.edu"), expected, stu)

if __name__ == '__main__':
    unittest.main()
