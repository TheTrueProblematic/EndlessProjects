# Here we go! Ready to dive into the ocean of Python, my friends?
# Our mission today is to find the second largest element in a list.
# Sounds fun, right?

# First off, we'll need to define a function that can do this task for us.
def second_largest_in_list(input_list):
    """
    This function takes a list as input and returns the second largest element from the list.
    If the list has less than 2 unique elements, it will return None.
    """

    # Check if the list is empty or has only one element. If so, there's no second largest element, so we return None.
    # Also, isn't it cool how Python makes this kind of checking super easy? Love it!
    if len(input_list) <= 1:
        return None

    # Now we'll remove duplicates from the list by turning it into a set.
    # Sets are like the superhero version of lists. They can't have duplicates, and they're super fast!
    # Bear in mind, this doesn't preserve the original order of elements, but for our task, that's not important.
    unique_elements = list(set(input_list))

    # If there's only one unique element in the list - again, there's no second largest, so we return None.
    # Imagine you're the only person in a race. Funny, right? But you can't be the second fastest!
    if len(unique_elements) == 1:
        return None

    # Time to do some sorting. Python's sort() method to the rescue!
    # This will sort our list of unique elements in ascending order.
    unique_elements.sort()

    # Finally, return the second largest element.
    # This will be the second last element in the sorted list (-2 index).
    return unique_elements[-2]


# So, that's it for our cute little function! Now let's define a main() function
# so we can test on some example lists directly from the command line.

def main():
    """
    Let's test our function on some example lists.
    """
  
    # Here are some lists to test on. Feel free to add more!
    lists_to_test = [
        [],
        [1],
        [1, 1],
        [1, 2, 2],
        [1, 2, 3, 4, 5],
        [-1, -2, -3, -4, -5],
        [99, 99, 100],
    ]

    # Let's loop through our lists and print out the second largest element!
    for test_list in lists_to_test:
        print("The second largest element in", test_list, "is", second_largest_in_list(test_list))


# Finally, we use this bit of standard Python boilerplate.
# This means: when we run this script directly, the main() function will be executed.
# If we were to import this file as a module in another script, the main() function wouldn't be run.
# Now you know!
if __name__ == "__main__":
    main()
    
# And that's it! Our second-largest-element-finding adventure has come to an end.
# Hope you found it as exciting as I did!
# Happy coding and see you on our next Python journey!