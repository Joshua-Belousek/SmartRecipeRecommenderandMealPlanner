#######################################################################################
##                              Testing output function                              ##
#######################################################################################

import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import output

class TestOutputFunctions(unittest.TestCase):

    def setUp(self):
        # Sample meal plan and shopping list for testing
        self.meal_plan = {
            "Monday": {"Pasta": {}, "Salad": {}},
            "Tuesday": {"Rice": {}}
        }
        self.shopping_list = {
            "tomato": 3,
            "garlic": 1,
            "lettuce": 1,
            "rice": 1
        }
        self.output_file = "test_output.txt"

    def tearDown(self):
        # Clean up by removing the output file if it exists
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_output(self):
        # Call the function to write the meal plan and shopping list to the file
        output.output_meal_plan_Shopping_list(self.output_file, self.meal_plan, self.shopping_list)
        
        # Ensure the file was created
        self.assertTrue(os.path.exists(self.output_file))
        
        # Open the file and read its content
        with open(self.output_file, "r") as file:
            content = file.read()

        # Check if Meal Plan and Shopping List are written correctly
        self.assertIn("Meal Plan:", content)
        self.assertIn("Monday:", content)
        self.assertIn("Pasta", content)
        self.assertIn("Tuesday:", content)
        self.assertIn("Rice", content)
        self.assertIn("Shopping List:", content)
        self.assertIn("tomato", content)
        self.assertIn("3", content)

if __name__ == '__main__':
    unittest.main()
