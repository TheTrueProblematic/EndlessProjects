# Hi there, welcome to the RandomExercisePicker! 🎉
# This little script is all set to brighten up your workout routine by picking a random exercise for you.  
# Let's embrace the thrill of the unpredictability, shall we?

# We just need the built-in 'random' module of python.
import random 

# We'll create a list of exercises to choose from. Feel free to change these to suit your workout regimen.
exercise_list = ['Push-ups', 'Sit-ups', 'Jumping Jacks', 'Burpees', 'Lunges', 'Planks', 'High Knees', 'Mountain Climbers']

# Here comes the fun part! 
# We'll use the 'choice' method from our 'random' module to pick a random exercise from our list. 
# Each time you run this script, you'll get a different exercise! Sounds exciting, huh?

def choose_random_exercise():
    chosen_exercise = random.choice(exercise_list)
    print(f"Today's exercise is: {chosen_exercise}")

# Time to get sweaty! 💪 Run the function and let's get moving!
choose_random_exercise() 

# That's all folks! Keeping it simple, neat and newbie friendly!
# Remember, your body can stand almost anything. It's your mind that you have to convince.
# So, keep up the good work and never give up on your fitness journey!

# Stay safe and have an awesome workout! 💜
# Code written with 💜 by a happy programmer
