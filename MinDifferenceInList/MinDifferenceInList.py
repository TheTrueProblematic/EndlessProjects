
# Hello there! 🤓 Welcome to the world of Python. We're going to do something super fun today.
# We're writing a Python program that finds the minimum difference between any two elements in a list. "Come on, that can't be fun," you say? Oh, trust me, it is when it's in Python.
# Stay with me, we'll have lots of fun! 😀

def find_min_difference(lst):
    # Let's sort the list first. It will be easier to calculate the difference.
    lst.sort()
    
    # Minimum difference can be large, right? So, let's set our initial min_diff to a big number, infinity sounds pretty big to me! 😁
    min_diff = float('inf')

    # Then, we'll have a good ol' loop through our list, skipping the last element because we're comparing each element with the next
    for i in range(len(lst)-1):
        # If the difference between the current element and the next is less than our min_diff...
        if (lst[i+1] - lst[i]) < min_diff:
            # ... then, we assign this new value to min_diff. It's the new champion! 🏆
            min_diff = lst[i+1] - lst[i]
            
    # And there you go! We return the minimum difference we found.
    # I told you it's fun, like a treasure hunt. 😉
    return min_diff

# Now let's give it a test drive!
my_list = [23, 6, 7, 16, 45, 89, 5]

# Drumroll, please! 🥁
print(find_min_difference(my_list))

# And there you have it! The smallest difference between any two numbers in the list.

# Hope you had fun! Keep coding and smile! Python loves you! ❤️

