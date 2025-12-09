
# Welcome to the Habit Tracker
# This simple python script will help you track your daily habits and visualize your streaks..
# Whether you're maintaining a workout schedule or learning a new language, keeping a habit can be fun (and sometimes a little challenging)
# So, why not make it a little more interesting with some visualization and tracking?

# First of all, we'll need a tiny bit of storage - a simple dictionary will do the trick
Habits = {}

# Now, let's create a function to add and remove habits
def manageHabits(habit, action='add'):
    # Adding a new habit
    if action == 'add':
        if habit not in Habits:
            Habits[habit] = []
            print(f"Yay! Added {habit} to your habit list.")
        else:
            print(f"Hmm, looks like {habit} is already on your list!")
    # Removing an existing habit
    elif action == 'remove':
        if habit in Habits:
            Habits.pop(habit)
            print(f"Removed {habit} from your habit list.")
        else:
            print(f"Hmm, can't find {habit} in your list!")

# Now, a function to track a habit
def trackHabit(habit):
    if habit in Habits:
        # We'll mark each day the habit is tracked with a simple 'X'
        Habits[habit].append('X')
        print(f"Good job! You've kept up with {habit} for {len(Habits[habit])} day(s).")
    else:
        print(f"Hmm, {habit} isn't in your habit list!")

# And finally, let's visualize those streaks!
def visualizeStreak(habit):
    if habit in Habits:
        streak = "".join(Habits[habit])
        print('Here is your current streak: '+ streak)
    else:
        print(f"Hmm, {habit} isn't in your habit list!")

# Now you can go conquer your habits! To update a habit, simply call the trackHabit() method with the habit's name as a parameter.
# To see your progress, call the visualizeStreak() method with the habit's name as a parameter.
# If you want to add or remove a habit, call the manageHabits() method with the habit's name as a parameter, and 'add' or 'remove' as the second, respectively.
# Happy habit tracking!
