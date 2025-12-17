
# Well hello there, friendly future programmer!
# Welcome to GoalSetter, your little buddy in the CLI, designed to help you set goals and track your progress.
# We'll be creating goals and tracking them together, with absolutely no GUI, dependencies, or Internet connectivity.
# Pure pythonic fun!

# We're going to need a couple of python in-built packages to make this work
import os
import json

# Let's make a path for a JSON file to store our goals and their progress
# On every run of this script, this file will be loaded, and saved back
# It's our mini database, simple and fun!
db_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'goals.json')


def load_goals():
    # This function does all the magic of loading goals.
    # It reads from the JSON file, gets the goals & progress,
    # and loads it into the memory for us. How cool is that?
    if os.path.exists(db_path):
        with open(db_path, 'r') as fh:
            return json.load(fh)
    else:
        return {}


def save_goals(goals):
    # This buddy right here? It does the opposite of load_goals.
    # It takes your goals from the memory and saves it back to our mini database.
    # Never lets you forget a thing!
    with open(db_path, 'w') as fh:
        json.dump(goals, fh)


def add_goal(title, total):
    # Here's where you feed in your dreams and aspirations!
    # Give your goal a title and a total count.
    # And like a loyal friend, it will add it to your goals list.
    goals = load_goals()
    goals[title] = {'total': total, 'progress': 0}
    save_goals(goals)


def update_goal(title, progress):
    # Well, look at you making strides towards your goal!
    # Update your progress here and keep going, champ!
    goals = load_goals()
    if title not in goals:
        print(f"Goal {title} does not exist.")
    else:
        goals[title]['progress'] = progress
        save_goals(goals)


def view_goals():
    # Curious about where you're at with your goals? Fret not!
    # This function here gives you a full report of goals and their progress.
    # Get your updates right here!
    goals = load_goals()
    for title, goal in goals.items():
        percentage = (goal['progress'] / goal['total']) * 100
        print(f"Goal: {title}, Progress: {percentage:.2f}%")


# And voila! That's your very own GoalSetter.
# Set goals, make progress, have fun. All in Python!
# Happy goal-getting, champ!

