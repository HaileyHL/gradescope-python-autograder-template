import unittest

from gradescope_utils.autograder_utils.decorators import weight, visibility

try:
    from solution.dining_hall_menus import dining_hall_menus
except Exception as e:
    raise Exception(f'Couldnt import your function dining_hall_menus from files. Please double check your file name and function name.')



def assert_equal_with_message(testcase, test_name, expected, actual):
    try:
        testcase.assertEqual(actual, expected)
    except AssertionError:
        print(f"--- Failed {test_name} ---")
        print(f"Expected Output:{expected}")
        print(f"Actual Output:{actual}")
        raise

# Tests for dining_hall_menus
class test_dining_hall_menus(unittest.TestCase):
    # 40 points in total
    @weight(5)
    def test_dining_hall_menus_1(self):
        """ #name(Test normal case 1) #score(4) """
        stu = dining_hall_menus(['pizza', 'spaghetti', 'salad', 'fries'], ['burgers', 'sushi', 'fries', 'pizza'])
        expected_list = ['spaghetti', 'salad', 'burgers', 'sushi']
        assert_equal_with_message(self, "Test normal case 1", sorted(expected_list), sorted(stu))

    @weight(5)
    def test_dining_hall_menus_2(self):
        """ #name(Test normal case 2) #score(4) """
        stu = dining_hall_menus(['pizza'], ['PIZZA'])
        expected_list = ['pizza', 'PIZZA']
        assert_equal_with_message(self, "Test normal case 1", sorted(expected_list), sorted(stu))

    @weight(5)
    def test_dining_hall_menus_3(self):
        """ #name(Test normal case 3) #score(3) """
        stu = dining_hall_menus(['sushi'], ['fries'])
        expected_list = ['sushi', 'fries']
        assert_equal_with_message(self, "Test normal case 1", sorted(expected_list), sorted(stu))

    @weight(5)
    def test_dining_hall_menus_4(self):
        """ #name(Test normal case 4) #score(3) """
        stu = dining_hall_menus(['fried rice', 'noodles', 'chicken'], ['chicken fried rice', 'noodles'])
        expected_list = ['fried rice', 'chicken', 'chicken fried rice']
        assert_equal_with_message(self, "Test normal case 1", sorted(expected_list), sorted(stu))

    @weight(4)
    def test_dining_hall_menus_5(self):
        """ #name(Test duplicate case 5) #score(4) """
        stu = dining_hall_menus(['pizza', 'salad', 'salad'], ['pizza'])
        expected_list = ['salad']
        assert_equal_with_message(self, "Test normal case 1", sorted(expected_list), sorted(stu))

    @weight(4)
    def test_dining_hall_menus_6(self):
        """ #name(Test duplicate case 6) #score(3) """
        stu = dining_hall_menus(['pasta', 'pasta', 'PASTA'], ['pasta'])
        expected_list = ['PASTA']
        assert_equal_with_message(self, "Test normal case 1", sorted(expected_list), sorted(stu))

    @weight(3)
    def test_dining_hall_menus_7(self):
        """ #name(Test both empty 7) #score(2)"""
        stu = dining_hall_menus([], [])
        expected_list = []
        assert_equal_with_message(self, "Test normal case 1", expected_list, stu)

    @weight(3)
    def test_dining_hall_menus_8(self):
        """ #name(Test empty case 8) #score(2) """
        stu = dining_hall_menus([], ['fries', 'fries'])
        expected_list = ['fries']
        assert_equal_with_message(self, "Test normal case 1", sorted(expected_list), sorted(stu))

    @weight(3)
    def test_dining_hall_menus_9(self):
        """ #name(Test same menus case 9) #score(2) """
        stu = dining_hall_menus(['sushi', 'sushi'], ['sushi', 'sushi'])
        expected_list = []
        assert_equal_with_message(self, "Test normal case 1", expected_list, stu)

    @weight(3)
    def test_dining_hall_menus_10(self):
        """ #name(Test empty string case 10) #score(2) """
        stu = dining_hall_menus(['burgers'], [''])
        expected_list = ['burgers', '']
        assert_equal_with_message(self, "Test normal case 1", sorted(expected_list), sorted(stu))

if __name__ == '__main__':
    unittest.main()
