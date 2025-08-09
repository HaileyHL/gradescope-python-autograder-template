import unittest

from gradescope_utils.autograder_utils.decorators import weight, visibility

try:
    from solution.validate_email import validate_email
except Exception as e:
    raise Exception(f'Couldnt import your function validate_email from files. Please double check your file name and function name.')



def assert_equal_with_message(testcase, test_name, expected, actual):
    try:
        testcase.assertEqual(actual, expected)
    except AssertionError:
        print(f"--- Failed {test_name} ---")
        print(f"Expected Output:{expected}")
        print(f"Actual Output:{actual}")
        raise

# Tests for validate_email
class test_validate_email(unittest.TestCase):
    # 40 points in total
    @weight(3)
    def test_validate_email1(self):
        """ #name(Test valid email 1) #score(4)"""
        stu = validate_email("abc@gmail.com", "gmail.com")
        expected = True
        assert_equal_with_message(self, "Test valid email 1", expected, stu)

    @weight(3)
    def test_validate_email2(self):
        """ #name(Test invalid email 2) #score(4)"""
        stu = validate_email("abcgmail.com", "gmail.com")
        expected = False
        assert_equal_with_message(self, "Test valid email 1", expected, stu)

    @weight(3)
    def test_validate_email3(self):
        """ #name(Test invalid email 3) #score(4)"""
        stu = validate_email("abc@@gmail.com", "gmail.com")
        expected = False
        assert_equal_with_message(self, "Test valid email 1", expected, stu)

    @weight(3)
    def test_validate_email4(self):
        """ #name(Test weird suffix 4) #score(3)"""
        stu = validate_email("abc@:^).com", ":^).com")
        expected = True
        assert_equal_with_message(self, "Test valid email 1", expected, stu)

    @weight(3)
    def test_validate_email5(self):
        """ #name(Test leading spaces 5) #score(3)"""
        stu = validate_email("       abc@gmail.com", "gmail.com")
        expected = True
        assert_equal_with_message(self, "Test valid email 1", expected, stu)

    @weight(3)
    def test_validate_email6(self):
        """ #name(Test trailing spaces 6) #score(3)"""
        stu = validate_email("abc@gmail.com       ", "gmail.com")
        expected = True
        assert_equal_with_message(self, "Test valid email 1", expected, stu)

    @weight(3)
    def test_validate_email7(self):
        """ #name(Test both spaces 7) #score(3)"""
        stu = validate_email("       abc@gmail.com       ", "gmail.com")
        expected = True
        assert_equal_with_message(self, "Test valid email 1", expected, stu)

    @weight(2)
    def test_validate_email8(self):
        """ #name(Test spaces in the middle 8) #score(2)"""
        stu = validate_email("ab c@gmail.com", "gmail.com")
        expected = False
        assert_equal_with_message(self, "Test valid email 1", expected, stu)

    @weight(2)
    def test_validate_email9(self):
        """ #name(Test spaces in the middle 9) #score(2)"""
        stu = validate_email("abc@g mail.com", "gmail.com")
        expected = False
        assert_equal_with_message(self, "Test valid email 1", expected, stu)

    @weight(2)
    def test_validate_email10(self):
        """ #name(Test wrong suffix 10) #score(3)"""
        stu = validate_email("abc@gmail.com", "ucsd.edu")
        expected = False
        assert_equal_with_message(self, "Test valid email 1", expected, stu)

if __name__ == '__main__':
    unittest.main()
