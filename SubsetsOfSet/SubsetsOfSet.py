
# Yay! This is going to be fun! Off we go. To infinity and beyond!
# A program to find all subsets of a given set.

# Okay, let's import what we need. But wait, what am I saying?
# We don't need any imports. This is pure, raw, beautiful Python!

def find_subsets(mainSet):
    """
    This function takes a set and returns all subsets of the set. 
    The power of Python compel us!

    Args:
        mainSet (list): The main set you want the subsets from!

    Returns:
        list: A list of all possible subsets!
    """

    # Base case: If the set is empty, there's only one subset: the empty set itself!
    if len(mainSet) == 0:
        return [[]]

    # Let's get a little bit recursive here (just like my love for Python).
    # We store the first element, and recursively get all subsets of the remaining set.
    subsets = find_subsets(mainSet[1:])
    
    # Now comes the magic. For every subset, we create a new subset which is a combination of the current subset and the first element.
    for i in range(len(subsets)):
        subsets.append(subsets[i] + [mainSet[0]])
    
    return subsets  # Voila! Subsets are ready.

if __name__ == "__main__":
    # Time to test this baby! Feel free to play around with the set below.
    main_set = [1, 2, 3]
    print(find_subsets(main_set)) 

# Isn't Python utterly beautiful? So clean, so elegant.
# Remember, ‘code is like humor. When you have to explain it, it’s bad.’ - Cory House
# Keep coding, stay happy!

