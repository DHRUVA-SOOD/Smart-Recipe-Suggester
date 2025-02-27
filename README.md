# Smart-Recipe-Suggester

## Overview
The Recipe Suggester is a Python-based tool that helps users find recipes based on available ingredients. It suggests possible dishes, highlights missing ingredients, and provides cooking instructions for selected recipes.

## Features
- Reads recipes from a CSV file.
- Matches user-provided ingredients with available recipes.
- Suggests recipes that can be made with minimal missing ingredients.
- Provides cooking instructions for selected recipes.
- Suggests additional ingredients to shop for if no complete recipes match.

## Requirements
- Python 3.x
- Pandas library

## Installation
1. Clone the repository or download the script.
2. Ensure you have Python installed.
3. Install required dependencies using:
   ```sh
   pip install pandas
   ```
4. Place your recipe dataset (CSV file) in the appropriate directory.

## Usage
1. Run the script using:
   ```sh
   python recipesuggester.py
   ```
2. Enter available ingredients when prompted (comma-separated).
3. The script will display suggested recipes with missing ingredients.
4. Select a recipe by entering the corresponding number.
5. The script will display the cooking method for the selected dish.
6. If no matching recipes are found, the script suggests additional ingredients to purchase.

## File Structure
- `recipesuggester.py` - Main script to run the program.
- `large_recipe_book.csv` - CSV file containing recipe data.

## CSV File Format
The CSV file should have the following columns:
- `Dish Name` - Name of the recipe.
- `Ingredients` - Comma-separated list of required ingredients.
- `Cooking Method` - Instructions to prepare the dish.

## Example Run
```
Enter available ingredients (comma-separated): Chicken, Rice, Spices

Recipes you can make:
1. Chicken Biryani: Missing: Yogurt, Ghee

Enter the number of the recipe you want to cook: 1

Great choice! Here’s how you can make Chicken Biryani:
[Cooking instructions displayed]
```

## Contributing
Feel free to contribute by adding more recipes, improving the script, or optimizing ingredient matching.

## License
This project is licensed under the MIT License.

