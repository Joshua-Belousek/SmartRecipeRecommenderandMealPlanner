
import inputs, algorithms


if __name__ == "__main__":
    #Get names of files with ingredients and preferences in them
    #ingredients_file = input("What is the file that your ingredients are in")
    #preferences_file = input("What is the file that your preferences are in")
    ingredients_file = "data\\ingredients.csv"
    preferences_file = "data\\preferences.json"

    #open the files and get the contences stored in a data structure
    ingredients = inputs.read_ingredients_csv(ingredients_file)
    preferences = inputs.read_Json(preferences_file)
    recommended_recipes = algorithms.recommend_recpies(preferences, ingredients) 
    meal_plan = algorithms.create_meal_plan(recommended_recipes,preferences)
    #print(meal_plan)
    #for days in meal_plan.keys():
    #    print(days)
    #    print(meal_plan[days])

    shopping_list = algorithms.generate_shopping_list(meal_plan, ingredients)
    print(shopping_list)
















#simple test for output uncomment to test
'''
meal_plan = [
    "Breakfast: Oatmeal with fruits",
    "Lunch: Grilled Chicken Salad",
    "Dinner: Salmon with vegetables"
]

shopping_list = [
    {"name": "Chicken", "quantity": "600", "unit": "grams"},
    {"name": "Oats", "quantity": "200", "unit": "grams"},
    {"name": "Salmon", "quantity": "500", "unit": "grams"},
    {"name": "Vegetables", "quantity": "300", "unit": "grams"}
]

output_meal_plan_Shopping_list("meal_plan_and_shopping_list.txt", meal_plan, shopping_list) 

'''
