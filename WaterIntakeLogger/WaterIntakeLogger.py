
# Hey there, beautiful people! Today we are logging water intake in a sparkly Python way. 
# This script logs the liters of water that you've consumed each day. Let's dive in!

import os  # Provides functions for interacting with the operating system. 
           # We will use it to check if our log file exists or not.

import datetime  # You know what it is. We are using it to date our hydration feats.

# First, let's define our log file. Let's call it "water_intake_log.txt". 
# We're gonna keep it simple and store this in the same directory as our script.
LOG_FILE_PATH = "water_intake_log.txt"

def log_water_intake(liters_of_water):
    """
    This function takes in the liters of water you've consumed, applies a timestamp to it, 
    and logs it. More hydration, more fun!
    """
    # Let's get the current date and time.
    now = datetime.datetime.now()

    # Aaand let's prepare the string that we're gonna write to our log file.
    log_entry = f"{now}: Drank {liters_of_water} liters of water \n"
    
    with open(LOG_FILE_PATH, "a") as log_file:  # We're opening the file in append mode.
        log_file.write(log_entry)               # Because we don't want to overwrite our previous victories.

if __name__ == "__main__":
    """
    And here is the entry point of our awesome script. If this script is run (not imported),
    we land here.
    
    Let's grab the liters of water from the command line arguments, log it, 
    and encourage the user to keep up their hydration hustle.
    """
    import sys                                 # We import sys to read command line arguments.  
    liters_of_water = sys.argv[1]               # The first argument is the script name itself, so we need the second one.

    log_water_intake(liters_of_water)
    
    print("Woot woot! Way to hydrate!")
    print("Your water intake has been logged. Keep it up!")

