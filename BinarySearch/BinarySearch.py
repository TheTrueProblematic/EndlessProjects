
# Welcome to our Binary Search Adventure! This exciting little file is crafted to
# implement the classic binary search algorithm in python, for your command-line delight.
# Can you feel the excitement?! I know I can!

def binary_search(sorted_array, target):
    # Let's start with defining our search space. At the start, it's the whole array.
    left, right = 0, len(sorted_array) - 1

    # Time for the main event: the search loop! We'll keep narrowing down our search
    # space until we've found our target or exhausted all possibilities.
    while left <= right:

        # Every fairytale needs a hero, and in this adventure, the "middle element" plays that role!
        mid = left + (right - left) // 2

        # Ah-ha! We've found our target, living happily at the middle of our current search space!
        # Let's return its index and be done with it.
        if sorted_array[mid] == target:
            return mid

        # Our target isn't at the middle, oh no! But fear not – if it's smaller than our
        # hero (the middle element), it's got to be hiding in the first half of our current search space.
        elif sorted_array[mid] > target:
            right = mid - 1

        # Our target is bigger than our hero? Then it must be in the second half.
        else:
            left = mid + 1

    # After all that, if we haven't found our target it's not in the array... sad, but possible.
    # That's why we'll return -1 in this case.
    return -1

# Testing time!
# Let's define a sorted list to search for some targets.
my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(binary_search(my_list, 15))  # Great! We should see an index of 7.
print(binary_search(my_list, 20))  # Oh no, our target isn't here... we should get -1.

# That's all, folks! You've just traversed the exciting wilderness of the Binary Search algorithm
# and lived to tell the tale. Use your new-found powers wisely!

