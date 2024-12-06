# Start of the fun code journey :)
# This python script merges two lists by alternating elements.
# This works directly from the command line! No GUI, no internet, no extras! Just pure Python!

# Let's import the built-in module we'll need.
from itertools import zip_longest

def merge_lists_alternating(list1, list2):
    # Hey! Here's where the magic begins. We use zip_longest from itertools.
    # It's great because it pairs up elements from the lists.
    # zip stops with the shortest list, but zip_longest keeps going. It fills any "overhang" with a filler value.
    # With Python, list1 and list2 dancing in perfect harmony, we get a new merged list!

    merged_list = []
    for item1, item2 in zip_longest(list1, list2, fillvalue=None):
        # We put the items from the first list and then from the second list into the merged list.

        # Let's do the first list.
        if item1 is not None: 
            merged_list.append(item1)

        # Now, the second list get's its turn!
        if item2 is not None:
            merged_list.append(item2)

    # And voila! We've got a merged list, alternating items from the two lists!
    return merged_list

# For the sake of making it more interactive, let's put a little test here.
# The script will ask for the lists and merge them for you ;)

if __name__ == '__main__':
    # We're using input to take in the lists.
    # Don't worry about security! There's no internet or API involved here!

    print("Enter elements of first list separated by space")
    list1 = [x for x in input().split()]
    print("Enter elements of second list separated by space")
    list2 = [x for x in input().split()]

    # Ta-dah! Here's your merged list!
    print("Merged list: ", merge_lists_alternating(list1, list2))

# And that's all for now, folks! A simple, fun little command-line script, just playing in Python. Enjoy!