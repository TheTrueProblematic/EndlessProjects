
# Hello there, the awesome humans, aliens or bots reading this! 🚀
#
# Welcome to our beautiful TimeConverter script. This handy little guy right here is going to help you convert time
# into hours, minutes, or seconds because who has time to do that manually, am I right? 😏

# First and foremost, let's define our functions that will handle all the time conversions.

def seconds_to_minutes(seconds):
    # Time to convert some seconds to minutes!
    # Don't you just love when Python does all the math for you? 😅
    return seconds / 60

def seconds_to_hours(seconds):
    # And now, let's convert seconds to hours.
    # Isn't this just exciting? 🎉
    return seconds / 3600

def minutes_to_seconds(minutes):
    # Now, we're going in the other direction.
    # Converting minutes to seconds. Oh, the power of Python! 💪
    return minutes * 60

def minutes_to_hours(minutes):
    # Converting minutes to hours now, because why not?
    # Just another day in the life of a Python script! 🐍
    return minutes / 60

def hours_to_seconds(hours):
    # Did someone ask for hours in seconds? Your wish is my command!
    # Let's watch as all those hours melt into seconds. 🔥
    return hours * 3600

def hours_to_minutes(hours):
    # And finally, let's turn hours into minutes.
    # Who knew time could be so flexible? Python knew, that's who! 🧙‍♂️
    return hours * 60

# Now let's use Python's magical __name__ function to make sure our script runs when called from the command line.
if __name__ == "__main__":
    # Using a while-loop to keep our script running until the user decides they're done converting time.
    while True:
        # Let's provide the user with some options and guide them on their time-converting journey.
        print("\nHey there! What would you like to do?")
        print("1. Convert seconds to minutes")
        print("2. Convert seconds to hours")
        print("3. Convert minutes to seconds")
        print("4. Convert minutes to hours")
        print("5. Convert hours to seconds")
        print("6. Convert hours to minutes")
        print("7. Quit")
        
        # Getting the user's choice.
        choice = input("\nPlease enter the number of your choice: ")

        # Based on the user's choice, we'll call the appropriate function and print the result.
        if choice == '1':
            seconds = float(input("Enter seconds: "))
            print(f"That's {seconds_to_minutes(seconds)} minutes!")
        elif choice == '2':
            seconds = float(input("Enter seconds: "))
            print(f"That's {seconds_to_hours(seconds)} hours!")
        elif choice == '3':
            minutes = float(input("Enter minutes: "))
            print(f"That's {minutes_to_seconds(minutes)} seconds!")
        elif choice == '4':
            minutes = float(input("Enter minutes: "))
            print(f"That's {minutes_to_hours(minutes)} hours!")
        elif choice == '5':
            hours = float(input("Enter hours: "))
            print(f"That's {hours_to_seconds(hours)} seconds!")
        elif choice == '6':
            hours = float(input("Enter hours: "))
            print(f"That's {hours_to_minutes(hours)} minutes!")
        elif choice == '7':
            # If the user wants to quit, we'll break out of the loop and say our goodbyes.
            print("\nThanks for using our TimeConverter! Have a wonderful time! 😄")
            break
        else:
            # If the user entered an invalid choice, let's let them know.
            print("\nOops, that option doesn't exist. Please try again!")

# And that's a wrap, folks! 🎬
# Thanks for joining us on this fun-filled journey of time conversion in Python!

