
# Hello there, lovely Pythonista!
# Buckle up, because we're about to remove some duplicate elements from a list!
# By the time we're done with this fun little script, your list will be as crisp and unique as a fresh autumn apple. ;)

# First, let's define our one and only function, 'remove_duplicates'.
# This awesome function is going to intake a list and spit back out a list, but without all those pesky duplicate elements.

def remove_duplicates(input_list):
    # Python set does not allow duplicates, so we use it to our advantage.
    # When we convert our list to a set, it will automatically remove any duplicate elements!
    # Lifehack, huh?
    return list(set(input_list))

# Now, you probably want to see your function in action. 
# Let's create a list with some duplicates for testing purposes.

test_list = ["alpha", "beta", "gamma", "alpha", "delta", "beta"]

# And away we go! Let's call our remove_duplicates function and pass our test_list to it.

unique_list = remove_duplicates(test_list)

# Cool, right? But what did it do? Let's print the result to the console so we can see our brilliant function at work.

print(unique_list)

# And voila! You should now see a list without duplicates in your console.
# Go forth and prosper with your new duplicate free list, adventurous coder!

# Until our next Python adventure, Happy Coding!

