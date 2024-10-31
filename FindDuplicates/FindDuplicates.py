
# Hey there, super coder! This is your friendly python script named 'FindDuplicates'.
# Our little task for the day is to find and display any duplicate values we find in a list.
# Now, buckle up, let the fun begin!

# For starters, let's import our only dependancy, the magnificent collections module!
# But hey, don't you worry! collections is a built-in module, so no extra installations required, woohoo!
from collections import Counter

def find_duplicates(input_list):
    # Let's use the sensational Counter from collections module to count the frequency of each element in the list.
    element_count = Counter(input_list)

    # Now that we have the count, let's find Sherlock Holmes inside us and find the culprits, umm, I mean duplicates.
    # We are defining duplicates here as elements appearing more than once in the list.
    # Our little buddy 'dupes' (short for duplicates) will hold these for us.
    dupes = [element for element, count in element_count.items() if count > 1]
  
    # Now that we have found our duplicates, time for the grand reveal!
    print('The duplicate elements in the list are :', dupes)

# Time to test our own little detective script!
# Just a random list for now, feel free to fill it with any list you like!
super_lista = [1, 2, 3, 2, 4, 5, 4, 4, 6, 7, 6, 8, 9, 9]
find_duplicates(super_lista)

# And that's it! Wasn't that fun?
# Just throw any list at our detective function and watch it unveil the secrets (duplicates) within!

