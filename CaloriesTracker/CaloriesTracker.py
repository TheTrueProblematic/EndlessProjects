
# Hey there, fellow hungry coder! Welcome to your new favorite script: CaloriesTracker!
# Designed to help keep track of your daily calorie intake, this script is like your personal dietitian.
# It's here to keep an eye on whether you're stuffing too many doughnuts or sticking to your leafy greens!
# And the best part? You don't need an internet connection, and it's as platform independent as Python itself. Isn't it great?

# Let's start by setting up some basics; nothing fancy just yet.

# A dictionary that'll be our mini database for storing food and their respective calories.
# Feel free to add as many items as you like!
FOOD_CALORIES = {
    'apple': 95,
    'banana': 105,
    'cake slice': 235,
    'pizza slice': 285,
    'carrot': 25
}

class CaloriesTracker:
    def __init__(self):
        self.daily_intake = {}

    # A function to add eaten food and their calories.
    def add_food(self, food_name, food_count):
        # Make sure this food is in our database!
        if food_name in FOOD_CALORIES:
            if food_name in self.daily_intake:
                self.daily_intake[food_name] += food_count
            else:
                self.daily_intake[food_name] = food_count
        else:
            print(f"Sorry, we don't have {food_name} in our food database.")
    
    # A function to print a summary of the day's calorie intake.
    # This is where you find out if that extra slice of cake was a good idea!
    def print_summary(self):
        total_calories = 0
        print("\nToday's calorie intake:\n")
        for food, count in self.daily_intake.items():
            calories = FOOD_CALORIES[food] * count
            total_calories += calories
            print(f"{food}: {count} serving(s), {calories} calorie(s)")
        print(f"\nTotal: {total_calories} calorie(s)")

# Now for the main program!
def main():
    ct = CaloriesTracker()

    # Let's loop and ask the user to input what they ate!
    while True:
        print("\nInput the food you ate (or 'quit' to stop):")
        food = input().lower()
        if food == 'quit':
            # If they want to stop this gourmet session, let's show them the summary of their intake!
            ct.print_summary()
            break
        else:
            # Let's ask how much of the food they ate
            print(f"How many serving(s) of {food} did you eat?")
            count = int(input())
            ct.add_food(food, count)

if __name__ == '__main__':
    main()
# And that's it! Here's to a healthy, mindful eating! Bon Appétit!
