# main.py
import inputs
import algorithms
import output
import json
import os

def display_preferences(preferences):
    # Display the current prefrences
    print("\nCurrent Preferences:")
    print(f"Diet: {preferences.get('diet', 'Not Set')}")
    print("Nutritional Goals:")
    for goal, value in preferences.get("nutritional_goals", {}).items():
        print(f"  {goal.capitalize()}: {value}")
    print()

def update_preferences(preferences_file):
    # Allow the user to update dietary preferences and nutritional goals.
    if os.path.exists(preferences_file):
        with open(preferences_file, 'r') as file:
            preferences = json.load(file)
    else:
        # Default structure if the file doesn't exist
        preferences = {
            "diet": "",
            "nutritional_goals": {
                "calories": 0,
                "protein": 0,
                "carbs": 0,
                "fat": 0,
                "fiber": 0
            }
        }
    
    # Display current preferences
    display_preferences(preferences)

    # Ask if the user wants to update preferences
    update_choice = input("Do you want to update your preferences? (yes/no): ").strip().lower()
    if update_choice not in ["yes", "y"]:
        return preferences

    print("\nUpdate your preferences:\n")
    
    # Update diet preference
    preferences["diet"] = input(f"Enter your diet preference (current: {preferences.get('diet', '')}): ").strip() or preferences["diet"]
    
    # Update nutritional goals
    for goal in preferences["nutritional_goals"]:
        current_value = preferences["nutritional_goals"].get(goal, 0)
        new_value = input(f"Enter your {goal} goal (current: {current_value}): ").strip()
        if new_value.isdigit():
            preferences["nutritional_goals"][goal] = int(new_value)
    
    # Save the updated preferences back to the file
    with open(preferences_file, 'w') as file:
        json.dump(preferences, file, indent=4)
    
    print("\nPreferences updated successfully!\n")
    return preferences

if __name__ == "__main__":
    # Get file paths
    ingredients_file = "data\\ingredients.csv"
    preferences_file = "data\\preferences.json"

    # Read or update preferences
    preferences = update_preferences(preferences_file)

    # Process ingredients and preferences
    ingredients = inputs.read_ingredients_csv(ingredients_file)
    recommended_recipes = algorithms.recommend_recpies(preferences, ingredients)
    meal_plan = algorithms.create_meal_plan(recommended_recipes, preferences)

    # Generate and display shopping list
    shopping_list = algorithms.generate_shopping_list(meal_plan, ingredients)
    
    # generate nutrional analysis 
    nutrional_summary = algorithms.nutritional_analysis(meal_plan,preferences)

    # Save output
    output_file_path = "meal_plan_and_shopping_list.txt"
    output.output_meal_plan_and_analysis(output_file_path, meal_plan, shopping_list, nutrional_summary)