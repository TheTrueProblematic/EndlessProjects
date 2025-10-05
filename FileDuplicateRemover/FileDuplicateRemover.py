
# Hello, Python enthusiasts! This is a fun, simple script named "FileDuplicateRemover.py"
# Joyful? Aren't we? Let's dive in!

# Python built-in libraries are quite powerful, aren't they? No need to install anything!
import sys  # For command-line arguments
import os  # For checking if files exist

# FileDuplicateRemover coming in! Its mission? Removing duplicate lines in a text file
# provided through the command line

# But before reaching for the stars, let's make sure we're on stable ground
# Check if there's the right amount of arguments
if len(sys.argv) != 2:
    print("Usage: python FileDuplicateRemover.py <filename>")
    sys.exit(1)  # Exits with a general error status

filename = sys.argv[1]  # Filename via command line argument

# Does the file exist? Let's check!
# If not, no point going further, right? Save the universe another day. Or file.
if not os.path.isfile(filename):
    print("File not found. Please input a valid file path.")
    sys.exit(1)

# Our spaceship has launched! Now, we open the file
with open(filename, "r") as file:
    # Remember, preparation is key for any space hero!
    # We store the content in a set; it ensures uniqueness, duplicates vanish like black holes!
    content = set(file.readlines())

# Time to go back to Earth and write down our adventures!
# We reopen the file in write mode to remove all previous content
with open(filename, "w") as file:
    for line in content:
        file.write(line)

# Script done! The universe, or at least that duplicate-lines-filled file, is saved!
# Innocent, joyful script? Or world-class hero? How about both!
print("Successfully removed duplicates!")

# Close curtains, the adventure is over! Mission accomplished, let's do another run!
sys.exit(0)  # Exits with a successful status

