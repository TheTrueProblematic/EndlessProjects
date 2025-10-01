
# Hello, World of Python! Here's a treat for all you neat freaks out there!
# Our little Python script here, called DirectoryCleaner, will help
# you keep your file system just as tidy as your room (I hope your room is tidy!).

# Alright, let's dive in!

import os

# The path of the directory to clean
# TODO: Replace this with the path of the directory you want to clean
DIR_PATH = 'enter-your-directory-path-here'

def remove_empty_dirs(dir_path):
    '''A fun little function to check if directory is empty and remove it.'''
    # Isn't life just simpler without empty directories?
    try:
        os.rmdir(dir_path)  
        print(f"Removed empty directory: {dir_path}")
    except OSError as ex:
        pass  # Oops! The directory wasn't empty. No worries, moving on...

def remove_empty_files(dir_path):
    '''An equally fun function to check if a file is empty and remove it.'''
    # An empty file is like a jug without water. Pointless, right?
    for file_path in os.listdir(dir_path):
        full_path = os.path.join(dir_path, file_path)
        if os.path.isfile(full_path):
            if os.path.getsize(full_path) == 0:
                os.remove(full_path)
                print(f"Removed empty file: {full_path}")

def cleanup_dir(dir_path):
    '''Okay, here's our main cleanup function.'''
    # We'll use it to roll out our cleanup operations.
    for path in os.listdir(dir_path):
        full_path = os.path.join(dir_path, path)
        if os.path.isdir(full_path):
            cleanup_dir(full_path)
            remove_empty_dirs(full_path)

        elif os.path.isfile(full_path):
            remove_empty_files(dir_path)

if __name__ == "__main__":
    # Let the cleaning begin!
    cleanup_dir(DIR_PATH)
    print('Directory cleanup completed successfully!')

# Phew! That was fun right? Until next time, keep being awesome and coding funky Python stuff!

