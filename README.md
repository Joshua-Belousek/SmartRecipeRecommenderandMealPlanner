# Smart Recipe Recommender and Meal Planner

This app helps users plan their meals for the week based on their dietary preferences and nutritional goals. The app will recommend meal plans and generate shopping lists for the recipes.

## Overview

The Smart Recipe Recommender and Meal Planner is a console application that takes in user preferences for diet (e.g., vegetarian, vegan) and nutritional goals (e.g., calories, protein, carbs), then generates a personalized weekly meal plan. The app also provides a shopping list of ingredients required to prepare the meals.

## Features

- **Meal Plan Generation**: The app suggests meals for 7 days based on the user’s diet and nutritional goals.
- **Shopping List Generation**: It generates a shopping list containing missing ingredients for the selected meals.
- **Customizable Preferences**: Users can input their dietary preferences (vegetarian, vegan, etc.) and nutritional goals (e.g., calories, protein, carbs, fat).

## How to Use the App

1. **Launch the App**:
   - Run the `main.py` file to start the application.
   - For command line:
     ```bash
     python main.py
     ```

2. **Enter Your Preferences**:
   - The app will prompt you to input your diet preference (e.g., vegetarian, vegan).
   - Input your nutritional goals (e.g., calories, protein, carbs, fat).

3. **Meal Plan Generation**:
   - The app will generate a weekly meal plan for you based on your preferences to an output file ".txt".

4. **Shopping List**:
   - After meal plan generation, the app will provide a shopping list with ingredients you need for the selected meals to the same output file ".txt".

## How to Run Tests

To ensure the app is working correctly, you can run the automated tests:

1. **Open Terminal**:
   - In VS Code, open the terminal by selecting `Terminal` > `New Terminal` from the top menu.

2. **Run the Tests**:
   - The tests are located in the `tests/` directory. To run all the tests, use the following command:
     ```bash
     python -m unittest discover -s tests
     ```
   - This will automatically find and run all the tests in the `tests/` folder.

3. **View Test Results**:
   - The test results will be displayed in the terminal. If everything is working correctly, you should see output indicating that all tests passed.

## Dependencies

Before running the app, ensure you have the required dependencies installed. Use `pip` to install them:

1. **Required Libraries**:
   - `unittest` 
   - `random`
   - `copy`
   - `itertools`
   - `json`
   - `csv`
   - `os`

## Division of Labor

The project is divided into the following tasks:

### Josh:
- **Algorithm Development**: Develop the core algorithms for generating meal plans based on dietary preferences and nutritional goals.
- **Documentation**: Help write the `README` file.
### Dominic:
- **Nutritional Analysis**: Handle the nutritional analysis of the recipes and ensure that the meal plan meets the specified goals.
- **Testing and Documentation**: Assist with testing and documentation.
### Bilal:
- **User Interaction**: Handle user input for diet preferences and nutritional goals.
- **Testing**: Ensure that the app works as expected by writing and running tests.
- **Documentation**: Help write the `README` file.


## Acknowledgments

- Thanks to our team members for contributing to the development of the Smart Recipe Recommender and Meal Planner.


