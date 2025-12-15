
# Hey there! Let's cook up something nice, shall we?
# This is a recipe manager script, just like a personal kitchen assistant, minus the frills.

import json
import os

# First, we need a place to store the recipes.
# Let's make it in the same directory where this python file is.
RECIPE_FILE_LOCATION = os.path.join(os.getcwd(), "recipes.json")

# Now, let's initially make sure our recipe 'box' is empty if it doesn't exist yet
if not os.path.exists(RECIPE_FILE_LOCATION):
    with open(RECIPE_FILE_LOCATION, 'w') as recipe_file:
        json.dump({}, recipe_file)

# Function to add a recipe to our recipe bank which is essentially a json file
def add_recipe():
    # Let's get the details of the recipe first
    name = input("Enter the name of the recipe: ")
    ingredients = input("Enter the ingredients of the recipe: ").split(',')
    steps = input("Enter the steps of the recipe, separated by ':': ").split(':')

    # Let's dump this recipe to the json file
    with open(RECIPE_FILE_LOCATION, 'r+') as recipe_file:
        data = json.load(recipe_file)
        data[name] = {"ingredients": ingredients, "steps": steps}
        recipe_file.seek(0)
        json.dump(data, recipe_file)

# Function to search a recipe from our recipe book
def search_recipe():
    name = input("Enter the name of the recipe you want to search for: ")
    with open(RECIPE_FILE_LOCATION, 'r') as recipe_file:
        data = json.load(recipe_file)
    # If the recipe is not present, return a failure message
    if name not in data:
        print("Recipe not found!")
    else:
        print(data[name])

# Function to display all recipes in the recipe bank
def display_all_recipes():
    with open(RECIPE_FILE_LOCATION, 'r') as recipe_file:
        data = json.load(recipe_file)
    for name, recipe in data.items():
        print(f"{name}: {recipe}\n")

# Function to handle user interaction
def main():
    while True:
        print("Welcome to Recipe Manager! What would you like to do?")
        print("1. Add a recipe")
        print("2. Search for a recipe")
        print("3. Display all recipes")
        print("4. Exit")

        user_input = input("Please enter your choice: ")
        if user_input == "1":
            add_recipe()
        elif user_input == "2":
            search_recipe()
        elif user_input == "3":
            display_all_recipes()
        elif user_input == "4":
            break
        else:
            print("Invalid option, please try again.")

# Call to the main function to start the script
if __name__ == "__main__":
    main()

