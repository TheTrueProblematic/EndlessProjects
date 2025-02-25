# Hey there, fellow Pythonista! You've stumbled upon the super-duper "EqualListsChecker" program.
# This is just a simple, fun Python script that's going to check if two lists contain the exact same elements.
# Remember it doesn't matter how many Python versions or snakes you've wrestled,
# this program doesn't discriminate - it runs perfectly on any platform with a fresh python install.

def check_if_equal(list1, list2):
    """
    This function takes two lists as input and checks whether they contain the same elements.
    
    :param list1: list, First list to be checked
    :param list2: list, Second list to be checked
    :return: bool, True if the lists are equal, False otherwise
    """

    # sort both lists because party time should always be organized!
    # This doesn't change the input lists (we respect private property),
    # but gives us two new ones which are identical to the originals and nicely sorted.
    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)

    # Now for the moment of truth! Are these lists identical twins or just distant cousins?
    # we simply check if sorted_list1 is exactly equal to sorted_list2.
    if sorted_list1 == sorted_list2:
        # Yay, an exact match! The lists are equals. Don't you just love it when that happens?
        return True
    else:
        # Oh no, not a match. But hey, it's their differences that make them unique!
        return False

# This is the end of the script! If you need to use it, simply call check_if_equal(list1, list2),
# where list1 and list2 are the two lists you want to compare.
# Stay coding and keep having fun! Python on, my friend.