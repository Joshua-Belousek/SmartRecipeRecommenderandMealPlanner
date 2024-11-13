import unittest
import sys
import os 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from unittest.mock import patch, mock_open
import json
from algorithms import recommend_recpies, meets_daily_nutritional_goals, create_meal_plan, generate_shopping_list, nutritional_analysis


class TestRecommendRecipes(unittest.TestCase):
    # Test recommend_recpies function
    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps({
        "recipe1": {
            "diet": "Vegetarian",
            "ingredients": ["tomato", "cheese", "lettuce"],
            "nutrition": {"calories": 200, "protein": 10, "carbs": 20, "fat": 10, "fiber": 5}
        },
        "recipe2": {
            "diet": "Vegan",
            "ingredients": ["tomato", "avocado", "lettuce"],
            "nutrition": {"calories": 150, "protein": 5, "carbs": 20, "fat": 7, "fiber": 4}
        }
    }))
    def test_recommend_recpies(self, mock_file):
        preferences = {"diet": "vegetarian", "nutritional_goals": {"calories": 1800, "protein": 70, "carbs": 250, "fat": 70}}
        ingredients = [{"name": "tomato", "quantity": 5}, {"name": "cheese", "quantity": 2}]
        
        # Call the function to test
        recommended = recommend_recpies(preferences, ingredients)
        
        # Check that the recipe1 is recommended and recipe2 is not
        self.assertIn("recipe1", recommended)
        self.assertNotIn("recipe2", recommended)


class TestMeetsDailyNutritionalGoals(unittest.TestCase):
    # Test meets_daily_nutritional_goals function
    def test_goals_met(self):
        total_nutrition = {'calories': 1800, 'protein': 70, 'carbs': 250, 'fat': 70, 'fiber': 30}
        goals = {'calories': 1600, 'protein': 60, 'carbs': 220, 'fat': 60}
        
        # Check if the total nutrition meets the goals
        self.assertTrue(meets_daily_nutritional_goals(total_nutrition, goals))

    def test_goals_not_met(self):
        total_nutrition = {'calories': 1500, 'protein': 50, 'carbs': 200, 'fat': 50, 'fiber': 25}
        goals = {'calories': 1600, 'protein': 60, 'carbs': 220, 'fat': 60}
        
        # Check if the total nutrition does not meet the goals
        self.assertFalse(meets_daily_nutritional_goals(total_nutrition, goals))



class TestCreateMealPlan(unittest.TestCase):
    def test_create_meal_plan(self):
        # Define a set of recipes
        recipes = {
            "recipe1": {
                "diet": "vegetarian",
                "ingredients": {"tomato": 1, "cheese": 1},
                "nutrition": {"calories": 500, "protein": 20, "carbs": 40, "fat": 20, "fiber": 10},
                "missing_ingredients_count": 0
            },
            "recipe2": {
                "diet": "vegetarian",
                "ingredients": {"lettuce": 1, "chickpeas": 1},
                "nutrition": {"calories": 400, "protein": 15, "carbs": 60, "fat": 15, "fiber": 10},
                "missing_ingredients_count": 0
            },
            "recipe3": {
                "diet": "vegetarian",
                "ingredients": {"beans": 1, "rice": 1},
                "nutrition": {"calories": 600, "protein": 25, "carbs": 70, "fat": 20, "fiber": 15},
                "missing_ingredients_count": 0
            },
            "recipe4": {
                "diet": "vegetarian",
                "ingredients": {"pasta": 1, "sauce": 1},
                "nutrition": {"calories": 700, "protein": 30, "carbs": 80, "fat": 25, "fiber": 10},
                "missing_ingredients_count": 0
            }
        }

        # Define more achievable nutritional goals
        preferences = {
            "diet": "vegetarian",
            "nutritional_goals": {"calories": 1000, "protein": 50, "carbs": 100, "fat": 40}
        }

        # Call the function to test
        meal_plan = create_meal_plan(recipes, preferences)
        
        # Check if the meal plan includes meals for all 7 days
        self.assertEqual(len(meal_plan), 7)

        # Additional checks for nutritional goals and diet compliance for each day
        for day, meals in meal_plan.items():
            total_nutrition = {'calories': 0, 'protein': 0, 'carbs': 0, 'fat': 0, 'fiber': 0}
            
            for recipe_name, recipe in meals.items():
                # Check diet compliance
                self.assertEqual(recipe['diet'], preferences['diet'])

                # Accumulate the nutrition for the day's recipes
                for key in total_nutrition:
                    total_nutrition[key] += recipe['nutrition'].get(key, 0)

            # Ensure total nutrition meets or exceeds daily nutritional goals
            for key, goal in preferences['nutritional_goals'].items():
                self.assertGreaterEqual(total_nutrition[key], goal)


class TestGenerateShoppingList(unittest.TestCase):
    # Test generate_shopping_list function
    def test_generate_shopping_list(self):
        meal_plan = {
            "Monday": {
                "meal1": {"ingredients": {"tomato": 1, "cheese": 2}},
                "meal2": {"ingredients": {"lettuce": 2, "cheese": 1}}
            }
        }

        ingredients = [
            {"name": "tomato", "quantity": 5},
            {"name": "cheese", "quantity": 3},
            {"name": "lettuce", "quantity": 1}
        ]

        # Call the function to test
        shopping_list = generate_shopping_list(meal_plan, ingredients)
        
        # Check if shopping list contains the correct missing items
        self.assertEqual(shopping_list, {"lettuce": 1})  # Need 1 more lettuce

################
# Waiting on func
################

# class TestNutritionalAnalysis(unittest.TestCase):
#     # Test nutritional_analysis function (currently not implemented)


if __name__ == "__main__":
    unittest.main()
