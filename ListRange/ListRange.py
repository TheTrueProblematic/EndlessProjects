
# Hello, fellow Pythonistas! Get ready for some number crunching fun! 🐍🤓
# In this script, we are going to find the range of a list of numbers. 
# Not the typical Python range(), but the mathematical one, max - min.

# Let's start by defining our function, shall we?

def find_range(numbers):
    """
    This function receives a list of numbers, and calculates its range (max - min).
    """
    # Look at our Python script, handling exceptions like a boss! We don't want any "list is empty" accidents, do we?
    if len(numbers) == 0:
        raise ValueError("Oops! The list can't be empty. Try again with at least one number.")

    # Let's find the villains and the heroes of our story - the smallest and the largest number in the list!
    min_num = min(numbers)
    max_num = max(numbers)

    # The moment of truth... drum roll, please... 🥁 The range is...
    return max_num - min_num

# OK, let's roll! But first, looks like there are a few questions someone needs to answer...
while True:
    data = input('Enter a list of numbers (comma-separated): ')
    # A sprightly little line of code turning a string into a list. Such agility! Go, Python! 🦸‍♂️
    nums = list(map(int, data.split(',')))

    # It's showtime!
    print(f"The range of the list is {find_range(nums)}.\n")

# That was fun, wasn't it? Python makes number magic so easy! Toodles, until next time. Keep rocking that Python mojo! 🎸🐍
