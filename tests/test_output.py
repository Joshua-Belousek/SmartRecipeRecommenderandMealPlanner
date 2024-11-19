#######################################################################################
##                              Testing output function                              ##
#######################################################################################

import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import output

# class TestOutputFunctions(unittest.TestCase):

#     def setUp(self):
#         # Sample meal plan and shopping list for testing
#         self.meal_plan = {
#             "Monday": {"Pasta": {}, "Salad": {}},
#             "Tuesday": {"Rice": {}}
#         }
#         self.shopping_list = {
#             "tomato": 3,
#             "garlic": 1,
#             "lettuce": 1,
#             "rice": 1
#         }
#         self.output_file = "test_output.txt"

#     def tearDown(self):
#         # Clean up by removing the output file if it exists
#         if os.path.exists(self.output_file):
#             os.remove(self.output_file)

#     def test_output(self):
#         # Call the function to write the meal plan and shopping list to the file
#         output.output_meal_plan_Shopping_list(self.output_file, self.meal_plan, self.shopping_list)
        
#         # Ensure the file was created
#         self.assertTrue(os.path.exists(self.output_file))
        
#         # Open the file and read its content
#         with open(self.output_file, "r") as file:
#             content = file.read()

#         # Check if Meal Plan and Shopping List are written correctly
#         self.assertIn("Meal Plan:", content)
#         self.assertIn("Monday:", content)
#         self.assertIn("Pasta", content)
#         self.assertIn("Tuesday:", content)
#         self.assertIn("Rice", content)
#         self.assertIn("Shopping List:", content)
#         self.assertIn("tomato", content)
#         self.assertIn("3", content)

# if __name__ == '__main__':
#     unittest.main()



class TestOutputFunctions(unittest.TestCase):

    def setUp(self):
        # Sample data for testing
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
        self.nutritional_analysis = {
            "total": {"calories": 2500, "protein": 150, "carbs": 300, "fat": 70, "fiber": 30},
            "daily": {
                "Monday": {"calories": 1250, "protein": 75, "carbs": 150, "fat": 35, "fiber": 15},
                "Tuesday": {"calories": 1250, "protein": 75, "carbs": 150, "fat": 35, "fiber": 15}
            },
            "per_meal": {
                "Pasta": {"calories": 600, "protein": 20, "carbs": 80, "fat": 10, "fiber": 5},
                "Salad": {"calories": 150, "protein": 5, "carbs": 20, "fat": 5, "fiber": 2},
                "Rice": {"calories": 500, "protein": 15, "carbs": 60, "fat": 10, "fiber": 3}
            },
            "comparison": {
                "calories": {"goal": 2000, "actual": 1250, "difference": -750},
                "protein": {"goal": 100, "actual": 75, "difference": -25},
                "carbs": {"goal": 250, "actual": 150, "difference": -100},
                "fat": {"goal": 80, "actual": 35, "difference": -45},
                "fiber": {"goal": 40, "actual": 15, "difference": -25}
            }
        }
        self.output_file = "test_output.txt"

    def tearDown(self):
        # Clean up by removing the output file if it exists
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_output_meal_plan_and_analysis(self):
        # Call the function to write the meal plan, shopping list, and nutritional analysis to the file
        output.output_meal_plan_and_analysis(self.output_file, self.meal_plan, self.shopping_list, self.nutritional_analysis)

        # Ensure the file was created
        self.assertTrue(os.path.exists(self.output_file))

        # Open the file and read its content
        with open(self.output_file, "r") as file:
            content = file.read()

        # Check if Meal Plan is written correctly
        self.assertIn("Meal Plan:", content)
        self.assertIn("Monday:", content)
        self.assertIn("Pasta", content)
        self.assertIn("Tuesday:", content)
        self.assertIn("Rice", content)

        # Check if Shopping List is written correctly
        self.assertIn("Shopping List:", content)
        self.assertIn("tomato", content)
        self.assertIn("3", content)
        self.assertIn("lettuce", content)

        # Check if Nutritional Analysis is written correctly
        self.assertIn("Nutritional Analysis:", content)
        self.assertIn("Total for the week:", content)
        self.assertIn("Calories: 2500", content)
        self.assertIn("Daily Breakdown:", content)
        self.assertIn("Monday:", content)
        self.assertIn("Calories: 1250", content)
        self.assertIn("Comparison to Goals:", content)
        self.assertIn("Calories:", content)
        self.assertIn("Goal: 2000", content)
        self.assertIn("Difference: -750", content)

if __name__ == "__main__":
    unittest.main()