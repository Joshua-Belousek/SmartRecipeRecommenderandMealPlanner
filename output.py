def output_meal_plan_Shopping_list(file_path, meal_plan, shopping_list):
    with open(file_path, 'w') as file:  #open the file on writing mode
        file.write("Meal Plan:\n")
        for meal in meal_plan:
            file.write(f"- {meal}\n")
        
        file.write("\nShopping List:\n")
        for item in shopping_list:
            file.write(f"- {item['quantity']} {item['unit']} {item['name']}\n")
