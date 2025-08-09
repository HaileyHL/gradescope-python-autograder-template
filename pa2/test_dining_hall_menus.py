import unittest

from gradescope_utils.autograder_utils.decorators import weight, visibility



# Tests for dining_hall_menus
try:
    from solution.dining_hall_menus import dining_hall_menus
except Exception as e:
    raise Exception(f'Couldnt import your function dining_hall_menus from files. Please double check your file name and function name.') from None

class test_dining_hall_menus(unittest.TestCase):

    def assert_equal_with_message(self, test_name, expected, actual):
        try:
            self.assertEqual(actual, expected)
        except AssertionError:
            print(f"--- Failed {test_name} ---")
            print(f"Expected Output:{expected}")
            print(f"Actual Output:{actual}")
            raise


    # 40 points in total
    @weight(5)
    def test_dining_hall_menus_1(self):
        stu = dining_hall_menus(['pizza', 'spaghetti', 'salad', 'fries'], ['burgers', 'sushi', 'fries', 'pizza'])
        expected_list = ['spaghetti', 'salad', 'burgers', 'sushi']
        self.assert_equal_with_message("Test normal case 1", sorted(expected_list), sorted(stu))

    @weight(5)
    def test_dining_hall_menus_2(self):
        stu = dining_hall_menus(['pizza'], ['PIZZA'])
        expected_list = ['pizza', 'PIZZA']
        self.assert_equal_with_message("Test normal case 2", sorted(expected_list), sorted(stu))

    @weight(5)
    def test_dining_hall_menus_3(self):
        stu = dining_hall_menus(['sushi'], ['fries'])
        expected_list = ['sushi', 'fries']
        self.assert_equal_with_message("Test normal case 3", sorted(expected_list), sorted(stu))

    @weight(5)
    def test_dining_hall_menus_4(self):
        stu = dining_hall_menus(['fried rice', 'noodles', 'chicken'], ['chicken fried rice', 'noodles'])
        expected_list = ['fried rice', 'chicken', 'chicken fried rice']
        self.assert_equal_with_message("Test normal case 4", sorted(expected_list), sorted(stu))

    @weight(4)
    def test_dining_hall_menus_5(self):
        stu = dining_hall_menus(['pizza', 'salad', 'salad'], ['pizza'])
        expected_list = ['salad']
        self.assert_equal_with_message("Test duplicate case 5", sorted(expected_list), sorted(stu))

    @weight(4)
    def test_dining_hall_menus_6(self):
        stu = dining_hall_menus(['pasta', 'pasta', 'PASTA'], ['pasta'])
        expected_list = ['PASTA']
        self.assert_equal_with_message("Test duplicate case 6", sorted(expected_list), sorted(stu))

    @weight(3)
    def test_dining_hall_menus_7(self):
        stu = dining_hall_menus([], [])
        expected_list = []
        self.assert_equal_with_message("Test both empty 7", expected_list, stu)

    @weight(3)
    def test_dining_hall_menus_8(self):
        stu = dining_hall_menus([], ['fries', 'fries'])
        expected_list = ['fries']
        self.assert_equal_with_message("Test empty case 8", sorted(expected_list), sorted(stu))

    @weight(3)
    def test_dining_hall_menus_9(self):
        stu = dining_hall_menus(['sushi', 'sushi'], ['sushi', 'sushi'])
        expected_list = []
        self.assert_equal_with_message("Test same menus case 9", expected_list, stu)

    @weight(3)
    def test_dining_hall_menus_10(self):
        stu = dining_hall_menus(['burgers'], [''])
        expected_list = ['burgers', '']
        self.assert_equal_with_message("Test empty string case 10", sorted(expected_list), sorted(stu))

if __name__ == '__main__':
    unittest.main()
