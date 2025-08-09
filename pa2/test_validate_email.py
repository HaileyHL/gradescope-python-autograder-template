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
            print(f"Error calling function with the parameters {inputs}.")
            print("Please double check your implementation.")
            print(f"--- DETAILED ERROR MESSAGE ---")
            raise

    def assert_equal_with_message(self, test_name, inputs, expected, actual):
        try:
            self.assertEqual(actual, expected)
        except AssertionError:
            print(f"--- Failed {test_name} ---")
            print(f"Parameters:{inputs}")
            print(f"Expected Output:{expected}")
            print(f"Actual Output:{actual}")
            print(f"--- DETAILED ERROR MESSAGE ---")
            raise

    # 32 points in total
    @weight(4)
    def test_validate_email1(self):
        inputs = ("abc@gmail.com", "gmail.com")
        stu = self.run_validate_email(inputs)
        expected = True
        self.assert_equal_with_message("Test valid email 1", inputs,expected, stu)

    @weight(4)
    def test_validate_email2(self):
        inputs = ("abcgmail.com", "gmail.com")
        stu = self.run_validate_email(inputs)
        expected = False
        self.assert_equal_with_message("Test invalid email 2",inputs, expected, stu)

    @weight(3)
    def test_validate_email3(self):
        inputs = ("abc@@gmail.com", "gmail.com")
        stu = self.run_validate_email(inputs)
        expected = False
        self.assert_equal_with_message("Test invalid email 3", inputs, expected, stu)

    @weight(3)
    def test_validate_email4(self):
        inputs = ("abc@:^).com", ":^).com")
        stu = self.run_validate_email(inputs)
        expected = True
        self.assert_equal_with_message("Test weird suffix", inputs, expected, stu)

    @weight(3)
    def test_validate_email5(self):
        inputs = ("       abc@gmail.com", "gmail.com")
        stu = self.run_validate_email(inputs)
        expected = True
        self.assert_equal_with_message("Test leading spaces 5", inputs, expected, stu)

    @weight(3)
    def test_validate_email6(self):
        inputs = ("abc@gmail.com       ", "gmail.com")
        stu = self.run_validate_email(inputs)
        expected = True
        self.assert_equal_with_message("Test trailing spaces", inputs, expected, stu)

    @weight(3)
    def test_validate_email7(self):
        inputs = ("       abc@gmail.com       ", "gmail.com")
        stu = self.run_validate_email(inputs)
        expected = True
        self.assert_equal_with_message("Test both spaces 7", inputs, expected, stu)

    @weight(3)
    def test_validate_email8(self):
        inputs = ("ab c@gmail.com", "gmail.com")
        stu = self.run_validate_email(inputs)
        expected = False
        self.assert_equal_with_message("Test spaces in the middle 8", inputs, expected, stu)

    @weight(3)
    def test_validate_email9(self):
        inputs = ("abc@g mail.com", "gmail.com")
        stu = self.run_validate_email(inputs)
        expected = False
        self.assert_equal_with_message("Test spaces in the middle 9", inputs, expected, stu)

    @weight(3)
    def test_validate_email10(self):
        inputs = ("abc@gmail.com", "ucsd.edu")
        stu = self.run_validate_email(inputs)
        expected = False
        self.assert_equal_with_message("Test wrong suffix 10", inputs, expected, stu)

if __name__ == '__main__':
    unittest.main()
