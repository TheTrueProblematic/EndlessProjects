
# Alrighty, programming pals, let's get to work on this nifty little project! 
# We're going to be creating a fabulous FileTimestampChanger.
# Now, this Python file's gonna turn any frown upside down by changing the modified time of your files to a given timestamp. 
# Bet your socks you've never seen anything quite like this before!

# No GUI here, folks - we're keeping it sleek and command-line only!
# And, guess what? No dependencies! Fresh install of Python on a brand new computer and you're good to roll.
# Also, we won't be needing an API or Internet access. Offline is the new online, right! 
# Oh, and before I forget: It’s python only. One platform to rule them all, eh?
# Last but not least, this entire wonder is just one python file in total! Pretty neat, huh?

# Gotta import the good ol' os and time modules for the magic to happen!
import os
import time

# Alright then. First things first, let's make sure we're running this script with two arguments: fileName and newTime.
if len(os.sys.argv) != 3:
    print("Usage: FileTimestampChanger fileName newTime")
    os.sys.exit()

# Grabbing the arguments from the command-line
fileName = os.sys.argv[1]
newTime = os.sys.argv[2]

# Now, let's convert our newTime into seconds from the epoch. That's how Python likes its timestamps, doesn't it?
newTimeInSeconds = time.mktime(time.strptime(newTime, '%Y-%m-%d %H:%M:%S'))

# Time to whip out the wand and repeat the magical mantra: os.utime!
# This little piece of sorcery is exactly what we need to set the last accessed and modified time.
os.utime(fileName, (newTimeInSeconds, newTimeInSeconds))

# And that's it, good folks! Our epic FileTimestampChanger is ready to rock and roll.
# Who knew changing file timestamps could be this much fun?

