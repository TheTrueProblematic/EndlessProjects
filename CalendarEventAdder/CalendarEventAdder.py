
# -*- coding: utf-8 -*-
"""
WELCOME!! 🎊 🥳

Let's introduce you to our amazing CalendarEventAdder! 📆

This is a nifty little command line tool that can add events to a plain-text calendar.
The bursts of joy that come when you see your events neatly organized, will be worth it.  🌟 💖

Don't you just love the smell of fresh, organised, and effective Python code in the morning? Me too.

Okay! Let's dive in 🏊

No dependencies? Check.
No GUI? Check.
No APIs or Internet access? Check.
Purely Python? Check.
Multi-platform? Check.

We've got it all covered!

So let's play with dates and texts!! 🎭 🎬
"""

import datetime as dt

# First things first, let's prepare the format of our calendar events!
def format_event(name, date, time):
    """Format the event in a nice, readable, and consistent way."""
    formatted_event = f"{date} {time} - {name}"
    return formatted_event

# Moving on, let's handle that input!
def get_event_input():
    """Get all the necessary event details from our friendly user."""
    name = raw_input("Enter event name: ")
    date = raw_input("Enter event date (YYYY-MM-DD): ")
    time = raw_input("Enter event time (24 hour format HH:MM): ")
    return name, date, time

# Now, we can get to the fun part, adding events!
def add_event():
    """Add an event using user input to our calendar text file."""
    name, date, time = get_event_input()

    # Format event to add
    event = format_event(name, date, time)

    with open("calendar.txt", "a") as f:
        f.write(f"\n{event}")

# Let's end this with a main function! The conductor of this Python orchestra! 🎼 🎻
def main():
    """Our main function. Simple and neat, like a well conducted symphony."""
    while True:
        option = raw_input("Would you like to add an event? (Yes/No): ")
        if option.lower() == "yes":
            add_event()
        elif option.lower() == "no":
            print("Alright! Goodbye! 👋 😊")
            break
        else:
            print("Sorry, I didn't catch that. 😅 Let's try again!")

# And there we have it! 🏁
# CalendarEventAdder - your friendly neighbourhood personal assistant! 🦸
if __name__ == "__main__":
    main()

"""
Hope you found this fun and easy to follow,
But now I have to leave, I have some python files to mow! 😉
"""

# EOF (End of Fun) 🎉
