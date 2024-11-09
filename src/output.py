# output.py

def output_meal_plan_Shopping_list(file_path, meal_plan, shopping_list):
    try:
        # Open the file in write mode
        with open(file_path, 'w') as file:
            # Write the meal plan section
            file.write("Meal Plan:\n")
            for day, meals in meal_plan.items():
                file.write(f"- {day}:\n")
                for meal, details in meals.items():
                    file.write(f"  - {meal}\n")
            
            # Write the shopping list section
            file.write("\nShopping List:\n")
            for item, quantity in shopping_list.items():
                file.write(f"- {quantity} {item}\n")
                
    except Exception as e:
        print(f"Error writing to file: {e}")

