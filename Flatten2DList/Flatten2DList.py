
# Hey there, my fellow Programmer! 😁
# I'm a simple Python script called 'Flatten2DList'!
# I was created to flatten a 2D list into a 1D list - Pretty awesome, huh?
# When run from the command line, I take a 2D list and transform it into a more friendly format.
# So, let's roll up our sleeves and dive straight into the code. 😎

# A sweet thing about python is its simplicity, and we're going to use built-in functions to achieve our goal.
# Specifically, we'll use sum() in combination with a neat little trick to sum the sublists into one big list.

def flatten_list(nested_list):
    """
    Function to flatten a 2D list 
    """
    # We're going to use the built-in sum function to,
    # well, sum together all the 1D lists inside our 2D list.
    # The trick here is to start with an empty list [] as the start of our sum.
    # This way, we're not adding numbers together (which sum usually does),
    # but instead we're adding lists together!

    # The result is like taking all the small lists and dumping them into one big list -
    # or in other words, flattening the 2D list. Neat, huh? 😄
    # Also, did you know? Using += on a list in Python is like using .extend, not .append.
    # This means each element from the input lists goes straight into the output list,
    # instead of the input lists themselves being added as elements! 🎉
    flattened = sum(nested_list, [])
    return flattened

# Now, let's test this piece of beauty with some test cases of our own.
# We'll just feed it a simple 2D list for now.
# Don't worry, our function is a tough cookie, it can handle any 2D list you throw at it! 😉
if __name__ == "__main__":
    test_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    print(flatten_list(test_list))

# And voilà! We're done! 😃
# Run me and watch a flat 1D list come to life from a nested 2D list. 🚀
# Happy Coding! 🤘
