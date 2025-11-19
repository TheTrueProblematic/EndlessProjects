
# =============================================================================
# Hey there, fellow coder! Welcome to the incredible land of "RandomWorkoutRoutine"!
# This is a place where all your workout dreams will become reality. Let's embark on this fantastic journey.
# =============================================================================

import random  # Oh, the places your workouts will go!

def main():
    # Let's start by defining our exercises and chalk out our workout plan!
    # Remember, feel free to change this list to suit your needs and preferences. Your workout, your rules!

    exercises = {
        'pushups': range(10, 31),
        'squats': range(15, 36),
        'lunges': range(15, 36),
        'jumping_jacks': range(25, 51),
        'plank': range(30, 91),  # note this is in seconds
        'high_knees': range(10, 31),
        'burpees': range(10, 31),
        'situps': range(15, 36),
    }

    # Time to pick some random exercises and make our own workout routine
    # Let's get ourselves a routine with 5 exercises, shall we?
    chosen_exercises = random.sample(list(exercises.keys()), 5)

    # Now that we have our exercises, let's count the reps!
    for exercise in chosen_exercises:
        reps = random.choice(list(exercises[exercise]))
        print(f"Do {reps} {exercise.replace('_', ' ')}")

    # And there you have it! A workout routine tailor-made for you!
    # Remember, the key to any good workout is a good attitude and a good sweat!
    # Happy workout!

if __name__ == '__main__':
    main()  # Ignition! Let's get that workout started!

# =============================================================================
# Woohoo! You made it to the end of the file! Go you!  
# I hope you found this journey as exciting as I did!
# Remember to breathe, hydrate and most importantly, enjoy your workouts!
# =============================================================================

