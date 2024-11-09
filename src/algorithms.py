import json
import random
import copy
import itertools


#################################################################################################
##                          Recommend all recipies that fit diet                               ##
#################################################################################################
#This will get all recipes that are in the users diet preferences and then caculate how many 
#ingredients are missing
def recommend_recpies(preferences, ingredients):
    with open("data\\recieps.json", mode = 'r') as file:
        recipes = json.load(file)
    diet = preferences['diet'].lower()
    recommended = {}
    #First finds if the meal is in the users diet
    for name, recipe in recipes.items():
        if recipe['diet'].lower() != diet and diet != 'non-vegetarian':
            continue
        recommended[name] = recipes[name]
    #Then find the number of missing ingredients
    for meal in recommended:
        missing_ingredients = 0
        for item in recommended[meal]['ingredients']:
            for list_ingred in ingredients:
                if list_ingred['name'] == item:
                    break
            else:
                missing_ingredients +=1
        recommended[meal]['missing_ingredients_count'] = missing_ingredients
    return recommended


#################################################################################################
##                          Helper Functions for create meal plan                              ##
#################################################################################################

def meets_daily_nutritional_goals(total_nutrition, goals):
    if 0.9*total_nutrition['calories'] >= goals['calories']:
        return True
    else:
        return False


#################################################################################################
##                                Create meal plan function                                    ##
#################################################################################################
def create_meal_plan(recipes, preferences):

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    nutritional_goals = preferences['nutritional_goals']
    diet = preferences['diet'].lower()

    #Initialize the meal plan
    meal_plan = {}

    #Keep track of recipes used overall
    used_recipes_overall = set()

    #For each day
    for day in days:
        day_meals = {}
        day_nutrition = {'calories': 0, 'protein': 0, 'carbs': 0, 'fat': 0, 'fiber': 0}
        recipes_used_today = set()

        #While the day's nutrition does not meet the goals
        while not meets_daily_nutritional_goals(day_nutrition, nutritional_goals):
            #Get list of recipes that have not been used today
            possible_recipes = {
                name: recipe for name, recipe in recipes.items()
                if name not in recipes_used_today
            }

            #If possible, prioritize recipes not yet used overall
            unused_recipes = {
                name: recipe for name, recipe in possible_recipes.items()
                if name not in used_recipes_overall
            }

            #If we have unused recipes, use them
            if unused_recipes:
                possible_recipes = unused_recipes

            #If no recipes are left, we cannot meet the goals
            if not possible_recipes:
                print(f"No more recipes available to meet nutritional goals for {day}.")
                break
            
            #Prioritize recipes with fewer missing ingredients
            possible_recipes_list = sorted(possible_recipes.items(),
                                      key=lambda x: x[1]['missing_ingredients_count'])

            #Randomize recipes with same missing ingredients count
            min_missing = possible_recipes_list[0][1]['missing_ingredients_count']
            best_recipes = [item for item in possible_recipes_list if item[1]['missing_ingredients_count'] == min_missing]
            selected_recipe_name, selected_recipe = random.choice(best_recipes)

            #Add the recipe to today's meals
            day_meals[selected_recipe_name] = recipes[selected_recipe_name]

            #Update day's nutrition
            for key in day_nutrition:
                day_nutrition[key] += selected_recipe['nutrition'].get(key, 0)

            #Mark recipe as used today
            recipes_used_today.add(selected_recipe_name)

            #Mark recipe as used overall if all recipes haven't been used yet
            if len(used_recipes_overall) < len(recipes):
                used_recipes_overall.add(selected_recipe_name)

        #Assign the day's meals to the meal plan
        meal_plan[day] = day_meals

    return meal_plan


#################################################################################################
##                            Function to get the shopping list                                ##
#################################################################################################
def generate_shopping_list(meal_plan, ingredients):
    #Make a new ingredients list, deep copy where we will keep tract of how much the
    #user has left after each meal we go over
    after_meal_ingredients = copy.deepcopy(ingredients)

    shopping_list = {}
    for day in meal_plan:
        for meal in meal_plan[day]:
            for item, qty in meal_plan[day][meal]['ingredients'].items():
                available_qty = 0
                have_item = None
                for ingredients_item in after_meal_ingredients:
                    if ingredients_item['name'] == item:
                        available_qty = ingredients_item['quantity']
                        have_Item = ingredients_item
                if available_qty < qty:
                    if have_Item:
                        have_Item['quantity'] = 0
                    needed_qty = qty - available_qty
                    if item in shopping_list:
                         shopping_list[item] += needed_qty
                    else:
                        shopping_list[item] = needed_qty
                else:
                    have_Item['quantity'] -= qty

    return shopping_list

#################################################################################################
##                                  Nutritional Analysis                                       ##
#################################################################################################

def nutritional_analysis(meal_plan):
    pass