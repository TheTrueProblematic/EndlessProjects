
# Hey eager coders, welcome to our thrilling FileLockChecker script! This brilliant piece of code is going to help you
# determine if a certain file is locked by another process or not. Let's put the pedal to the metal and get started!

# We start off by importing the os module. The os module in Python provides functions for interacting with the operating system - no fancy stuff, it's all built-in!
import os

# We're all about that command line life. No fancy GUIs here, pure old-skool command line interactions!
def check_file_lock(file_path):
    """
    Woo-hoo, this is our main function! It's where all the magic happens.
    It accepts a file path as an argument and checks if the file is currently locked.
    """
    # First, we use the os.open method to try to open the file in read/write mode.
    # Don't worry about reading or writing anything right now, we're just using this to see if something else already has the file open.
    if os.access(file_path, os.R_OK) and os.access(file_path, os.W_OK):
        
        # Let's try to open the file! Will it work? Who knows! The tension is palpable!
        try:
            file_descriptor = os.open(file_path, os.O_RDWR)
            os.close(file_descriptor)
            
            # If we make it here, that means the file opened successfully and is not locked by another process.
            print("Smooth sailing! The file at {} is not locked.".format(file_path))
            return False
        except OSError:
            # If we encountered an OSError, that means the file is locked, we're blocked from opening it. Aw, shucks!
            print("Oh dear, looks like the file at {} is locked! Maybe next time.".format(file_path))
            return True
    else:
        print("Hmm, it seems we don't have the necessary permissions to access {file_path}. Let's not mess with those!")
        return True
        
# This built-in Python function lets us call our function straight from the command line. Super neat, right?
if __name__ == "__main__":
    import sys
    
    # sys.argv gives us all the words in the command line, and the [1] lets us take the second one (since we start counting at 0).
    file_path = sys.argv[1]
    
    # Call our function with the user's input. It's game time!
    check_file_lock(file_path)

