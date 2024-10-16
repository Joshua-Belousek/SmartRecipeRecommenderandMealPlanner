import csv
import json

def read_ingredients_csv(file):
    with open(file, mode = 'r') as file: #open the file on reading mode
        ingredients = []
        reader = csv.reader(file)
        next(reader) # skip the header of the file
        for row in reader:
            ingredients.append({
                "name": row[0],     
                "quantity": row[1],
                "unit": row[2]})
                  
    return ingredients      #ingredients[0]['name'] will access the name of the first ingredient

#function to read Json file
def read_Json(file):
    with open(file, mode='r') as file:
        prefrences = json.load(file)
    return prefrences


# write the meal plan and shopping list to a text file considering meal_plan a list of stirngs
# and shopping_list a list of dictonaries
def output_meal_plan_Shopping_list(file_path, meal_plan, shopping_list):
    with open(file_path, 'w') as file:  #open the file on writing mode
        file.write("Meal Plan:\n")
        for meal in meal_plan:
            file.write(f"- {meal}\n")
        
        file.write("\nShopping List:\n")
        for item in shopping_list:
            file.write(f"- {item['quantity']} {item['unit']} {item['name']}\n")

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