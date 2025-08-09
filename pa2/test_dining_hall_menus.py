import unittest

from gradescope_utils.autograder_utils.decorators import weight, visibility

# Tests for dining_hall_menus
try:
    from solution.dining_hall_menus import dining_hall_menus
except Exception as e:
    raise Exception(f'Couldnt import your function dining_hall_menus from files. Please double check your file name and function name.') from None

class test_dining_hall_menus(unittest.TestCase):

    def run_dining_hall_menus(self, inputs):
        try:
            stu = dining_hall_menus(inputs[0], inputs[1])
            return stu
        except Exception as e:
            print(f"Error calling function with the parameters {inputs}.")
            print("Please double check your implementation.")
            print(f"\n--- DETAILED ERROR MESSAGE ---")
            raise

    def assert_equal_with_message(self, test_name, inputs, expected, actual):
        try:
            self.assertEqual(actual, expected)
        except AssertionError:
            print(f"--- Failed {test_name} ---")
            print(f"Parameters:{inputs}")
            print(f"Expected Output:{expected}")
            print(f"Actual Output:{actual}")
            print(f"\n--- DETAILED ERROR MESSAGE ---")
            raise


    # 40 points in total
    @weight(5)
    def test_1(self):
        inputs = (['pizza', 'spaghetti', 'salad', 'fries'], ['burgers', 'sushi', 'fries', 'pizza'])
        stu = self.run_dining_hall_menus(inputs)
        expected_list = ['spaghetti', 'salad', 'burgers', 'sushi']
        self.assert_equal_with_message("Test normal case 1", inputs,
                                       sorted(expected_list), sorted(stu))

    @weight(5)
    def test_2(self):
        inputs = (['pizza'], ['PIZZA'])
        stu = self.run_dining_hall_menus(inputs)
        expected_list = ['pizza', 'PIZZA']
        self.assert_equal_with_message("Test normal case 2", inputs, sorted(expected_list), sorted(stu))

    @weight(5)
    def test_3(self):
        inputs = (['sushi'], ['fries'])
        stu = self.run_dining_hall_menus(inputs)
        expected_list = ['sushi', 'fries']
        self.assert_equal_with_message("Test normal case 3", inputs, sorted(expected_list), sorted(stu))

    @weight(5)
    def test_4(self):
        inputs = (['fried rice', 'noodles', 'chicken'], ['chicken fried rice', 'noodles'])
        stu = self.run_dining_hall_menus(inputs)
        expected_list = ['fried rice', 'chicken', 'chicken fried rice']
        self.assert_equal_with_message("Test normal case 4", inputs, sorted(expected_list), sorted(stu))

    @weight(4)
    def test_5(self):
        inputs = (['pizza', 'salad', 'salad'], ['pizza'])
        stu = self.run_dining_hall_menus(inputs)
        expected_list = ['salad']
        self.assert_equal_with_message("Test duplicate case 5", inputs, sorted(expected_list), sorted(stu))

    @weight(4)
    def test_6(self):
        inputs = (['pasta', 'pasta', 'PASTA'], ['pasta'])
        stu = self.run_dining_hall_menus(inputs)
        expected_list = ['PASTA']
        self.assert_equal_with_message("Test duplicate case 6", inputs,sorted(expected_list), sorted(stu))

    @weight(3)
    def test_7(self):
        inputs = ([], [])
        stu = self.run_dining_hall_menus(inputs)
        expected_list = []
        self.assert_equal_with_message("Test both empty 7",inputs, expected_list, stu)

    @weight(3)
    def test_8(self):
        inputs = ([], ['fries', 'fries'])
        stu = self.run_dining_hall_menus(inputs)
        expected_list = ['fries']
        self.assert_equal_with_message("Test empty case 8", inputs, sorted(expected_list), sorted(stu))

    @weight(3)
    def test_9(self):
        inputs = (['sushi', 'sushi'], ['sushi', 'sushi'])
        stu = self.run_dining_hall_menus(inputs)
        expected_list = []
        self.assert_equal_with_message("Test same menus case 9", inputs, expected_list, stu)

    @weight(3)
    def test_10(self):
        inputs = (['burgers'], [''])
        stu = self.run_dining_hall_menus(inputs)
        expected_list = ['burgers', '']
        self.assert_equal_with_message("Test empty string case 10", inputs, sorted(expected_list), sorted(stu))

if __name__ == '__main__':
    unittest.main()
