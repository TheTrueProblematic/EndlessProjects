
# -------------------------------------------------------------------------------
# SIMPLEJOURNAL.PY
# A joyous little script that allows you to append journal entries with a timestamp
# It's really cool and it feels like you're talking directly to the machine, a bit of CLI magic ;)
# And hey! It's not connected with any awful dependencies, internet or APIs, Just necessarily you, python and your feelings!
# -------------------------------------------------------------------------------

# We need just the os and datetime module, and these sweet little pythoneers come builtin. No extra Installation, whoa!!
import os
import datetime

# Our wonderful little function that accepts your deep thoughts (input_text) and enchants them onto the journal file
def append_to_journal(input_text):
    # We're gonna add a date and time stamp to your entry so when you look back, you feel those tick-ticks
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Open up that journal file in append mode, 'cause we don't want to lose what was there already
    with open("journal.txt", "a") as journal_file:
        # Add in the new text with a timestamp
        journal_file.write("{} - {}\n".format(timestamp, input_text))
        
    # That's it! We've done what we set out to do and there's no clean up or anything required. YAY!!!
    # Now go write some deep thoughts :D

# Alright!!! let's test this! Ask a user for input and write it to the journal
print("Hello, dear user! Welcome to your personal CLI journal.")
print("Just write down your thoughts and I'll make sure they stick around.")
entry = input("So, what are you thinking? ")
append_to_journal(entry)

# Grinning emoji(Figuratively, can't print out here), We did it! Keep journalling, stay awesome!

