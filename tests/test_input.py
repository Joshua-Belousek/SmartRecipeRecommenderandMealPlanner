#######################################################################################
##                              Testing input functions                              ##
#######################################################################################

import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import inputs 

class TestInputFunctions(unittest.TestCase):
    def test_read_ingredients_csv(self):
        # Sample CSV content
        ingredients = inputs.read_ingredients_csv("data/ingredients.csv")
        self.assertGreater(len(ingredients), 0)             # check if there are ingredients
        self.assertEqual(ingredients[0]["name"], "chicken") # check if the first element is chciken (which it is)

    def test_read_json(self):
        preferences = inputs.read_Json("data/preferences.json")
        self.assertEqual(preferences["diet"], "non-vegetarian")  # check if the diet is vegan 
        self.assertGreater(preferences["nutritional_goals"]["calories"], 500) # check if the calories greater than 500

if __name__ == '__main__':
    unittest.main()
