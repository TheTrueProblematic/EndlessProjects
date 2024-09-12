
# Yay! Let's have some fun renaming files in a directory!
# Bored of typing every single new name? Let's automate it!

# First things first, let's import os module - our knight in shining armor who helps us interact with the operating system.
import os

def rename_files(directory, pattern, replacement):
    """
    This function will rename multiple files in a directory based on a user-specified pattern.
 
    Parameters:
    directory (str): The directory containing the files to be renamed.
    pattern (str): The pattern in the file names to be replaced.
    replacement (str): The string to replace the pattern.
    """
    
    # Don't you worry about cross-platform compatibility, dear! Our os.path module got this for us!
    directory = os.path.expanduser(directory)
    
    # Now let's be adventurous! Dive into the directory and start renaming!
    for filename in os.listdir(directory):
        # Remember our mission - only rename those who match our pattern!
        if pattern in filename:
            # calculate the new name for the ones who are lucky to get chosen!
            new_name = filename.replace(pattern, replacement)
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_name)
            
            # And Boom! Our chosen ones get their new identities!
            os.rename(old_path, new_path)
            # We did it! Let's print out  their glorious new names!
            print(f"Renamed file {filename} to {new_name}")

# Time to see our magic in action! Run this file as:
# python FileRenamer.py [directory] [pattern] [replacement]
if __name__ == "__main__":
    import sys
    # Make sure we got all the right spells... I mean arguments!
    if len(sys.argv) != 4:
        print("Usage: python FileRenamer.py [directory] [pattern] [replacement]")
    else:
        directory, pattern, replacement = sys.argv[1:4]
        rename_files(directory, pattern, replacement)

# Hurray! Another day, another successful adventure in the world of Python!
# Now sit back, relax and enjoy the rest of your day!

