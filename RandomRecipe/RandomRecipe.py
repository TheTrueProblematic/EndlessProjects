
# RandomRecipe.py
# Hello there, thank you for using RandomRecipe, the fun and simple python project
# designed to add a bit of spice to your daily meal planning.
# This script is going to be your new best friend!
# This recipe generator doesn't need an internet connection, APIs or anything fancy like that
# 'cause this little script is one finely sharpened kitchen knife. 

# Let's get started, shall we?

# First off, let's import the random library.
# This is the secret ingredient to our recipe madness.
import random

# Just to keep things super tasty, let's predefine a couple of ingredient lists.
# These are the main ingredients every household should have or can easily get during a quick grocery run.
proteins = ["chicken", "beef", "tofu", "fish", "beans"]
grains = ["rice", "pasta", "quinoa", "barley", "couscous"]
vegetables = ["bell pepper", "broccoli", "spinach", "carrot", "zucchini"]
fruits = ["apple", "banana", "mango", "strawberries", "grapes"]
spices = ["salt", "pepper", "paprika", "oregano", "thyme"]

# Now, let's define our main course, also known as the star of the show - the function that generates our random recipe!
def generate_recipe():
    # With every magic trick, we pick a random ingredient from each list above.
    # Oh, don't worry about it getting boring, randomness will keep your taste buds guessing!
    protein = random.choice(proteins)
    grain = random.choice(grains)
    vegetable = random.choice(vegetables)
    fruit = random.choice(fruits)
    spice = random.choice(spices)

    # Now it's time for the grand reveal!
    # We'll print out our randomly selected ingredients, paving the way for your culinary creativity to play.
    print("Random Recipe Generator\n")
    print("Main Protein: " + protein)
    print("Grain: " + grain)
    print("Vegetable: " + vegetable)
    print("Fruit: " + fruit)
    print("Spice: " + spice)
    print("\nNow go make something delicious!")

# Alright, it's showtime! Let's run the function when the script is executed.
if __name__ == "__main__":
    generate_recipe()

# Bon Appetit! Hope you enjoy this recipe rollercoaster. Remember to never stop experimenting and adding new ingredients!

