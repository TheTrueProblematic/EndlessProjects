
# Hey there, fellow Pythonista! I'm your friendly neighborhood script, ready to sort your lists of tuples for you! 

# This script is all about taking a list of tuples and sorting them based on the second element in each tuple. 

# Best part is, I don't need no Internet to do my job. You just provide me with a list of tuples and I do the rest! Exciting, isn't it?

# Enough chit-chat, let's dive right in!

def sort_by_second_element(tuple_list):
    '''
    Function to sort a list of tuples by the second element in each tuple 
    '''
    
    # I'm just going to use the built-in sorted() function to sort our list.
    # This function takes two parameters: the list to sort, and a key to sort by.

    # The key should be a function that takes a single argument and returns a value to sort by. In our case, that's just the second element of the tuple: 
    # that's what the lambda function is doing. It extracts the second element (index 1) from the tuple.

    # The sorted function doesn't modify the original list. Instead, it returns a new list that's sorted in ascending order.
    # So let's return this newly sorted list and get the ball rolling!
    return sorted(tuple_list, key=lambda x: x[1]) # Voila! Your list is sorted by the second element in the tuples. 

# Test it out. Plug in some tuples and watch the magic happen!
print(sort_by_second_element([(2, 5), (1, 3), (4, 1), (7, 3), (9, 1)]))

# Well, that's it for now. I'll be here if you need me. Stay awesome! 

