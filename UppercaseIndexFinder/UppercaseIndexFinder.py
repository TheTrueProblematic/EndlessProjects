
# =====================
# The Adorable UppercaseIndexFinder Python Script!
# =====================

# Hi there, dear reader! Welcome to our tiny but mighty Python script
# affectionately named UppercaseIndexFinder!
# Our mission is fantastically simple: Find all the index positions of
# uppercase letters in a given string and return them as a list.

# Intrigued? Excited? Can't wait to see how it all unfolds? 
# Me neither! Hop in, let's get started!

def uppercase_index_finder(user_input):
    """
    The heart and soul of our script, the function that does the magic!
    It takes a string, and finds the index positions of all uppercase letters.
    """
    # Now we'll use the magic of list comprehension and enumerate
    # to get our indices in a neat and tidy list!
    uppercase_indices = [index for index, char in enumerate(user_input) if char.isupper()]

    # Achievement unlocked: Acquired list of uppercase indices!
    return uppercase_indices

def main():
    """
    Because every epic quest needs a beginning, this is ours!
    From here we collect the user's string and launch our uppercase index finder.
    """

    # Gather input from the user
    # All great adventures start by saying hello! In our case, it's to the user 😄
    user_string = input("Please enter a string and I'll find the indices of all the uppercase letters for you! ")

    # Now let's call our little helper function and pass it the user's string
    indices = uppercase_index_finder(user_string)
    
    # Now to reveal the results to the user!
    print(f"The uppercase letters in your string are at the following indices: {indices}")

if __name__ == "__main__":
    # This little line of code checks if script is being run directly or imported.
    # We only want to start our journey if script is being run directly.
    main()

# Well, that's it, folks! Our wonderful script has come to an end.
# Thanks for joining me on this magical ride! 
# Now you can carry on with your cool UppercaseIndexFinder! Happy Coding! 😊
