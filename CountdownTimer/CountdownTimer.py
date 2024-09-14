# Well hello there, happy coder. Today we are going to make a useful little script for a countdown timer.
# It's simple, clean, and most importantly, super enjoyable to make!
# The best part? No GUI, APIs, or other installed dependencies - this beauty runs beautifully from command line!
# So, fasten your seatbelts and let's jump right in!

import time

def countdown(t):
    # Wow wee, here we go!
    # This function takes an input 't' - in seconds!
    while t:
        # Defining the format of the output here,
        mins, secs = divmod(t, 60)
        # Python's inbuilt function divmod() splits 't' into minutes and seconds!
        timer = '{:02d}:{:02d}'.format(mins, secs)
        # We use .format here to ensure that the format always contains two places, 
        # even if the digit is 0.
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Countdown Over!')  # And there goes your timer!

# Now let's use our function -

t = input("Enter the time in seconds: ")
# Time to run the function!

countdown(int(t))
# Woohoo! Enjoy your timer!

# This little script will run on any system that supports Python, isn't that cool?
# Also, remember - only use the time in seconds. So if you want to set the timer for 2 minutes, 
# put in 120 (because 60s*2m = 120s).
# And when time's up, you get a lovely little message telling you so. Enjoy coding!
