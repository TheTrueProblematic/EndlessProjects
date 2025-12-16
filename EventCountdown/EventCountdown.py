
# Hey there, Happy Programmers! Welcome to the tiny, yet fascinating world of the EventCountdown script.
# We're here with one Python file to count down the days until a specific event.
# This program will work as a standalone piece, requiring no dependencies, no API, and certainly no internet access. 
# It's a cool little application designed to run from the comfort of your command line interface. Let's dive right in!

# First thing's first – let's import the one and only package we're going to need: the built-in python 'datetime'
import datetime

# The name of the game is EventCountdown, and we need to know 2 things: the event's name and its date.
def countdown(event_name, event_year, event_month, event_day):

    # We'll use Python's built-in datetime module to get today's date.
    today = datetime.date.today()

    # Our event's date is passed in as year, month, and day. 
    # Using such specific information, we'll create an accurate datetime object.
    event_date = datetime.date(event_year, event_month, event_day)

    # We're smart coders, and we know we cannot time travel (yet!). So, we handle this little time paradox.
    if event_date < today:
        print("Hey there, fellow coder! This event has already passed. Hope it was a good one!")
        return

    # Counting down the days is nothing more than a simple subtraction of dates. How cool is that?
    remaining_days = event_date - today

    # Drum roll... And here it comes, the awaited days until your event!
    print("There are " + str(remaining_days.days) + " days until " + event_name + ".")


# It's time to put your script to work. Go ahead, specify the details of the event and watch the magic happen.
# Example: There is an event named "New Year's Eve" on 2022, 12, 31.
countdown("New Year's Eve", 2022, 12, 31)
# Just replace the name and date above with your details. 

# And Voila! Here we are at the end of our tiny yet mighty program. Thanks for joining us on this coding adventure.
# Enjoy your countdown, and remember, each day is an event itself. Keep coding, keep smiling!
