
# Well hello there! 😃 You're about to witness an awesome array union program.
# Just like a sweet reunion, we're gonna bring some array friends together!

# We'll use python's built in 'set' data structure to perform the array union.
# Why sets? Well, because they're like arrays, but with superpowers! 🦸‍♂️
# They automatically filter out duplicates, and have handy functions for improving this union task.

# This script works in any new machine with a standalone Python install, no internet, no GUI needed.

# It's console party time! 🎉

def array_union(array1, array2):
    """
    This function takes two arrays (array1 and array2) as input and returns their union.
    The returned array contains all the unique elements present in both arrays.
    Duplicate elements are presented only once in the result.

    Args:
    array1: List
    array2: List

    Returns:
    list: Union of array1 and array2.

    """
    # Converting arrays to sets. This gets rid of any duplicates in each array.
    set1 = set(array1)
    set2 = set(array2)

    # The union of two sets is a set of all elements from both sets. 
    # order isn't guaranteed (but we don't care about order, do we? 😜)
    union_set = set1.union(set2)

    # Converting the result back to list, as our requirements say we deal with arrays (not sets).
    # Also, its easier to work with lists in python (and more fun, hehe! 🎈)
    union_array = list(union_set)

    return union_array

# Testing our function because we believe in the "test as you go" lifestyle!!!✌️
def test_array_union():
    """
    This function tests the 'array_union' function by providing sample inputs
    and asserting the outputs to be equal to the expected results.

    """

    assert array_union([1, 2, 3], [2, 3, 4]) == [1, 2, 3, 4]
    assert array_union([5, 6], [6, 7]) == [5, 6, 7]
    assert array_union([8, 9, 10], [11, 12]) == [8, 9, 10, 11, 12]

    # Whew! everything passed!
    print("All tests passed! We're good to go!")

# Well, it's time to run our tests!
test_array_union()

# Please provide your array inputs to our function when using it in production.
# E.g., array_union(['John', 'Doe'], ['Doe', 'Smith'])
# Returns: ['John', 'Doe', 'Smith']

# Do have a fun-tastic time using this script, and here's to many more array unions! 🥳🥂 Cheers, Happy Programmer.
