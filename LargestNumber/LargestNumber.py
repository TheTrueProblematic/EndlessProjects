
# Hey there, adventure seeker! Welcome aboard!
# Our mission today is quite exciting! We are on a quest to find the largest number from a list. Sounds thrilling, right?

# So to kick things off, let's define our function called `find_largest()`.
def find_largest(numbers):
    # Luckily for us, Python is jam-packed with handy tools 
    # One of those is the `max()` function. It's just crazy about finding the biggest stuff!
    # So we pass our number list to `max()` and let it do its thing.
    largest = max(numbers)
    # And voila! We got our largest number. Now, let's send it back from whence it came.
    return largest

# Our journey does not end here. We will be given our list of numbers from the command line
# So, we need to make sure we can handle that.

# Python has a module called `sys` which is just phenomenal and is always ready for action.
# It has a `argv` attribute where it stores command line arguments, isn't that cool?
# We need to import this little helper.
import sys

# `sys.argv` is super helpful, but it does consider the file name as the first argument.
# So, our numbers will actually start from the second element.
# We will also need to convert them to integers because they will be string type initially.
numbers = list(map(int, sys.argv[1:]))

# Now we are ready for the grand finale.
# Let's call our `find_largest()` function with the numbers as the input and print its return value.
print(find_largest(numbers))

# Well, that wraps it up! We found the largest number and made sure to have some fun along the way.
# Until next time, happy coding! 
