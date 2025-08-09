import unittest

from gradescope_utils.autograder_utils.decorators import weight, visibility

try:
    from solution.validate_email import validate_email
except Exception as e:
    raise Exception(f'Couldnt import your function validate_email from files. Please double check your file name and function name.') from None


# Tests for validate_email
class test_validate_email(unittest.TestCase):

    def assert_equal_with_message(self, test_name, inputs, expected, actual):
        try:
            self.assertEqual(actual, expected)
        except AssertionError:
            print(f"--- Failed {test_name} ---")
            print(f"Inputs:{inputs}")
            raise

    # 32 points in total
    @weight(4)
    def test_validate_email1(self):
        stu = validate_email("abc@gmail.com", "gmail.com")
        expected = True
        self.assert_equal_with_message("Test valid email 1", ("abc@gmail.com", "gmail.com"),expected, stu)

    @weight(4)
    def test_validate_email2(self):
        stu = validate_email("abcgmail.com", "gmail.com")
        expected = False
        self.assert_equal_with_message("Test invalid email 2",("abcgmail.com", "gmail.com"), expected, stu)

    @weight(3)
    def test_validate_email3(self):
        stu = validate_email("abc@@gmail.com", "gmail.com")
        expected = False
        self.assert_equal_with_message("Test invalid email 3", ("abc@@gmail.com", "gmail.com"), expected, stu)

    @weight(3)
    def test_validate_email4(self):
        stu = validate_email("abc@:^).com", ":^).com")
        expected = True
        self.assert_equal_with_message("Test weird suffix", ("abc@:^).com", ":^).com"), expected, stu)

    @weight(3)
    def test_validate_email5(self):
        stu = validate_email("       abc@gmail.com", "gmail.com")
        expected = True
        self.assert_equal_with_message("Test leading spaces 5", ("       abc@gmail.com", "gmail.com"), expected, stu)

    @weight(3)
    def test_validate_email6(self):
        stu = validate_email("abc@gmail.com       ", "gmail.com")
        expected = True
        self.assert_equal_with_message("Test trailing spaces", ("abc@gmail.com       ", "gmail.com"), expected, stu)

    @weight(3)
    def test_validate_email7(self):
        stu = validate_email("       abc@gmail.com       ", "gmail.com")
        expected = True
        self.assert_equal_with_message("Test both spaces 7",("       abc@gmail.com       ", "gmail.com"), expected, stu)

    @weight(3)
    def test_validate_email8(self):
        stu = validate_email("ab c@gmail.com", "gmail.com")
        expected = False
        self.assert_equal_with_message("Test spaces in the middle 8", ("ab c@gmail.com", "gmail.com"), expected, stu)

    @weight(3)
    def test_validate_email9(self):
        stu = validate_email("abc@g mail.com", "gmail.com")
        expected = False
        self.assert_equal_with_message("Test spaces in the middle 9", ("abc@g mail.com", "gmail.com"), expected, stu)

    @weight(3)
    def test_validate_email10(self):
        stu = validate_email("abc@gmail.com", "ucsd.edu")
        expected = False
        self.assert_equal_with_message("Test wrong suffix 10", ("abc@gmail.com", "ucsd.edu"), expected, stu)

if __name__ == '__main__':
    unittest.main()
