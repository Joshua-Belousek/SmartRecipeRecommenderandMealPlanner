import json
import random

#this function takes in all of the recipes that we have and sees if they fit the users preferences
def recommend_recpies(ingredients, preferences):
    with open("recieps.json", 'r') as file:
        recipes = json.load(file)

    diet = preferences['diet'].lower()
    recommended = {}
    for name, recipe in recipes.items():
        if recipe['diet'].lower() != diet and diet != 'non-vegetarian':
            continue
        if all(item in ingredients for item in recipe['ingredients']):
            recommended[name] = recipe
    return recommended

def create_meal_plan(preferences):
    with open("recieps.json", 'r') as file:
        recipes = json.load(file)

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    meal_plan = {}
    diet = preferences['diet'].lower()

    #This is used to filter out recipies that are not in the users prefernces
    filtered_recipes = {}
    for name in recipes.keys():
        recipe_diet = recipes[name]['diet'].lower()
        if diet == 'vegan' and recipe_diet != 'vegan':
            continue  
        elif diet == 'vegetarian' and recipe_diet not in ['vegetarian', 'vegan']:
            continue 
        filtered_recipes[name] = recipes[name]
    #we need 2 of these in case we need to use recipies again
    recipe_names = list(filtered_recipes.keys())
    recipe_names_main = recipe_names.copy()

    #if this is true, then there are no recipes that match the users preferences
    if not recipe_names:
        return {}

    #this is done to randomly chose a recipe by using pop to avoid duplicates
    random.shuffle(recipe_names)

    for day in days:
        if not recipe_names:
            recipe_names = recipe_names_main.copy()
            random.shuffle(recipe_names)
        
        meal_plan[day] = recipe_names.pop()


    return meal_plan




def generate_shopping_list(meal_plan, ingredients):
    with open("recieps.json", 'r') as file:
        recipes = json.load(file)

    shopping_list = {}
    for meal in meal_plan.values():
        for item, qty in recipes[meal]['ingredients'].items():
            if item not in ingredients:
                if item in shopping_list:
                    shopping_list[item] += qty
                else:
                    shopping_list[item] = qty
            else:
                available_qty = ingredients[item]['quantity']
                if available_qty < qty:
                    needed_qty = qty - available_qty
                    if item in shopping_list:
                        shopping_list[item] += needed_qty
                    else:
                        shopping_list[item] = needed_qty
    return shopping_list