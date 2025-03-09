
#Hello there, hope you're having a splendid day! Let's get coding, shall we?
#Today, we're creating a neat little utility to sort a list of dictionaries. But not just any sort. 
#We're going to sort by a specific key. Very useful, isn't it?

#First things first, let's start with our imports.
#But wait! Our instructions say we mustn't have any dependencies.
#Good news! Python's built-in functions are more than enough for our task. So no import lines today. High five!

def sort_list_of_dicts(dict_list, sort_key):
    """
    Sorts a list of dictionaries by the specific key.

    Args:
    dict_list : List of Dictionaries
    sort_key : The key we want to sort by

    Returns:
    Sorted list of dictionaries
    """
    # Look at us, impressing others with our Python docstring capabilities! 
    # Always good to explain what our functions do.

    # Now, let's check if our given sort_key exists in all dictionaries.
    # It would be a bummer if it didn't, right?
    for dictionary in dict_list:
        if sort_key not in dictionary:
            # Uh-oh, the key doesn't exist in the dictionary. Let's let the users know
            print(f"The key '{sort_key}' does not exist in all dictionaries. Please check your input.")
            return [] # A friendly return of an empty list instead of an error

    # If we made it this far, it means our sort_key is good to go!
    # Now, time for the actual sorting. Python makes this super easy. 
    sorted_list = sorted(dict_list, key=lambda x: x[sort_key])

    # Ta-da! Our list is sorted and ready to go.
    # Let's return it back so it can go on its merry way.
    return sorted_list

# There you have it, folks! A handy dandy utility function to sort a list of dictionaries by a key you want.
# I hope you're as stoked as I am. Happy coding, and enjoy the rest of your day!
