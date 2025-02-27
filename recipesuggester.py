import pandas as pd

def load_recipes(file_path):
    return pd.read_csv(file_path)

def find_recipes(user_ingredients, recipes_df):
    suggestions = {}
    user_ingredients = set(map(str.lower, user_ingredients))
    missing_ingredients = set()
    
    for _, row in recipes_df.iterrows():
        recipe_name = row['Dish Name']
        recipe_ingredients = set(map(str.lower, str(row['Ingredients']).split(', ')))
        missing = recipe_ingredients - user_ingredients
        
        if recipe_name not in suggestions:
            if not missing:
                suggestions[recipe_name] = ("You have all ingredients!", recipe_ingredients)
            elif len(missing) <= 3:
                suggestions[recipe_name] = (f"Missing: {', '.join(missing)}", recipe_ingredients)
                missing_ingredients.update(missing)
    
    return suggestions, missing_ingredients

def get_recipe_instructions(recipe_name, recipes_df):
    recipe = recipes_df[recipes_df['Dish Name'] == recipe_name]
    if not recipe.empty:
        return recipe.iloc[0]['Cooking Method']
    return "Instructions not available."

def main():
    file_path = r"C:\\internshhip\\recipesuggester\\large_recipe_book.csv"
    recipes_df = load_recipes(file_path)
    
    user_input = input("Enter available ingredients (comma-separated): ").strip()
    user_ingredients = [item.strip().lower() for item in user_input.split(',')]
    
    suggested_recipes, missing_ingredients = find_recipes(user_ingredients, recipes_df)
    
    if suggested_recipes:
        print("\nRecipes you can make:")
        recipe_list = list(suggested_recipes.keys())
        for i, dish in enumerate(recipe_list, 1):
            print(f"{i}. {dish}: {suggested_recipes[dish][0]}")
        
        choice = input("\nEnter the number of the recipe you want to cook: ")
        if choice.isdigit() and 1 <= int(choice) <= len(recipe_list):
            selected_recipe = recipe_list[int(choice) - 1]
            instructions = get_recipe_instructions(selected_recipe, recipes_df)
            print(f"\nGreat choice! Here’s how you can make {selected_recipe}:\n{instructions}")
        else:
            print("Invalid selection. Please try again next time!")
    else:
        print("No matching recipes found. Consider shopping for more ingredients!")
        if missing_ingredients:
            print("Suggested ingredients to shop:", ", ".join(missing_ingredients))

if __name__ == "__main__":
    main()

