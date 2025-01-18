
# Time12to24.py
# What a great day to write some beautiful python code!

# Ok so here's the game plan:

# We want to convert the time from the 12-hour format to the 24-hour format.
# No fancy GUIs, just good old command line interaction. 
# Isn't it fun to do this the old-school way?

def convert_time(time_string_12h):
    # Alright let's convert some time!

    # Python's standard library has a nice function called `strptime`.
    # This little beauty can parse time given in a string,
    # and it can understand both 12-hour and 24-hour formats,
    # among many other things! Isn't it awesome!

    from datetime import datetime

    # Let's use strptime to parse our 12-hour formatted time string.
    # We provide it with the format our time string is in to help it 
    # understand what the numbers and the AM/PM mean. Neato!
    time_object = datetime.strptime(time_string_12h, "%I:%M %p")

    # Now, our time_object is aware of the time it represents.
    # But it's still in 24-hour format.
    # So let's convert it back into a string, this time in 24-hour format!
    # Again, we instruct strftime about our desired output format.

    time_string_24h = time_object.strftime("%H:%M")

    # Done and dusted! Let's return this nicely formatted string.
    return time_string_24h

# Now, let's add some command line interaction.
# Python's sys module gives us access to command line arguments.

import sys

# sys.argv is a list that holds your command line arguments.
# It starts with the name of your script itself as argument number 0,
# followed by any additional arguments you may have passed.

# So if someone runs: 
# python Time12To24.py "02:30 PM"
# sys.argv[0] will be "Time12To24.py"
# sys.argv[1] will be "02:30 PM"

# Let's grab our time string from the command line.

time_string_12h_from_command_line = sys.argv[1]

# Time to do the conversion!

time_string_24h = convert_time(time_string_12h_from_command_line)

# Finally, let's give the user back their transformed time.
# print is enough to write to the command line. Easy peasy!

print(time_string_24h)

# And we're done!
# From now on, transforming time is as easy as
# python Time12To24.py "02:30 PM"
# Isn't code just magical?

# Now go convert some time, you time lord!
