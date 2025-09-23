
# FileExtensionSorter.py
# Greetings! I'm a happy little script designed to sort files into folders based on their extension.
# Handy, right? Now let's dive into the fun!

# First off, let's import the modules we need. Don't worry, these are all built into Python.
# os for working with files and folders, shutil for moving stuff around.
import os
import shutil

# Now we're going to ask for a directory to sort. Exciting, isn't it?
# We'll stick this inside a function so we can call it again later if needed.
# No one likes repeating themselves!
def get_directory():
    print("Please enter the directory to be sorted:")
    dir_path = input()
    return dir_path

# Now we'll go through the directory and sort things out.
# This is where the magic happens!
def sort_files(dir_path):
    # Let's make sure our path is okay first.
    if not os.path.isdir(dir_path):
        print(f"Whoops! {dir_path} does not exist. Let's try that again, shall we?")
        sort_files(get_directory())
    
    # Now for the main event! We'll go through each file in the directory.
    for filename in os.listdir(dir_path):
        # Get the file extension. This will be our folder name!
        extension = os.path.splitext(filename)[1][1:]
        
        # If the extension folder doesn't exist, we'll make it.
        # It's like spring cleaning, but all year round!
        if extension and not os.path.exists(os.path.join(dir_path, extension)):
            os.makedirs(os.path.join(dir_path, extension))
        
        # Finally, we'll move the file into its new home.
        # It's like a housewarming party for files!
        if extension:
            shutil.move(os.path.join(dir_path, filename), os.path.join(dir_path, extension, filename))

# And that's it! Tidy and efficient, just like our sorted files.
# Now we'll just call our functions to get things rolling!
sort_files(get_directory())

