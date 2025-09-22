
# -*- coding: utf-8 -*-
"""
Hello, joyful codemate! Welcome to the DirectoryTreePrinter.
This script will bring the whole directory tree right to your terminal. 
‘Cause, who doesn’t like a good tree, eh?
"""

import os

def list_files(start_path):
    """Alright, let's gear up! This function is the heart of our script.
    It starts from a given path and walks through all its sub-folders to print a delightful tree view. 
    It's just like taking a walk in the woods, without leaving your desk!
    """
    for root, dirs, files in os.walk(start_path):
        # start_path can be any directory, let it be your oyster!
        level = root.replace(start_path, '').count(os.sep)
        # Count the number of separators in the path to calculate the indentation level.
        # Boom! Your path is now pretty as a sunflower.
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        # It's time to list and print all the files in the current path.
        sub_indent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(sub_indent, f))
        """
        That's it! You've just walked through the whole directory. 
        Isn't it amazing how a bit of Python can save your day?
        """


if __name__ == "__main__":
    """You've made it this far and now the adventure begins!
    Just call this script from the command line and enjoy a tree view of your directories.
    """
    list_files('.')
    """
    See, that wasn't so hard, was it? 
    You've just printed your entire directory tree, from the comfort of your own terminal! 
    Pat yourself on the back, because you've earned it, my friend!
    """

