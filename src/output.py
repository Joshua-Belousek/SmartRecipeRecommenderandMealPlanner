# output.py

def output_meal_plan_and_analysis(file_path, meal_plan, shopping_list, nutritional_analysis):
    try:
        with open(file_path, 'w') as f:
            # Write meal plan
            f.write("Meal Plan:\n")
            for day, meals in meal_plan.items():
                f.write(f"{day}:\n")
                for meal in meals:
                    f.write(f"  - {meal}\n")
            f.write("\n")

            # Write shopping list
            f.write("Shopping List:\n")
            for item, quantity in shopping_list.items():
                f.write(f"{item}: {quantity}\n")
            f.write("\n")

            # Write nutritional analysis
            f.write("Nutritional Analysis:\n")
            
            # Total analysis
            f.write("Total for the week:\n")
            for nutrient, value in nutritional_analysis['total'].items():
                f.write(f"  {nutrient.capitalize()}: {value}\n")
            f.write("\n")
            
            # Daily analysis
            f.write("Daily Breakdown:\n")
            for day, nutrients in nutritional_analysis['daily'].items():
                f.write(f"{day}:\n")
                for nutrient, value in nutrients.items():
                    f.write(f"  {nutrient.capitalize()}: {value}\n")
                f.write("\n")
            
            # Per meal analysis (optional)
            f.write("Per Meal Analysis:\n")
            for meal, nutrients in nutritional_analysis['per_meal'].items():
                f.write(f"{meal}:\n")
                for nutrient, value in nutrients.items():
                    f.write(f"  {nutrient.capitalize()}: {value}\n")
                f.write("\n")
            
            # Comparison to goals
            f.write("Comparison to Goals:\n")
            for nutrient, data in nutritional_analysis['comparison'].items():
                f.write(f"{nutrient.capitalize()}:\n")
                f.write(f"  Goal: {data['goal']}\n")
                f.write(f"  Actual: {data['actual']}\n")
                f.write(f"  Difference: {data['difference']}\n")
                f.write("\n")

        print(f"Nutritional analysis, meal plan, and shopping list saved to {file_path}.")
    except Exception as e:
        print(f"Error writing to file: {e}")
