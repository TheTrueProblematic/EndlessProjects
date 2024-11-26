
# -*- coding: utf-8 -*-
"""
Hello there,
So here's the thing - This is a little script that does something super useful.
Yes, you heard it right! This script finds the UNION of two lists.
Remember, the UNION of lists deal with all the unique elements from both lists, just like in a set.
So, let's dive right into our quest to unify lists... Shall we?
"""

# Function to find Union of two lists
def list_union(list1, list2):
    """ Returns a list that's the union of the two lists. """

    # We'll use the built-in set() function to turn our lists into sets.
    # You know what's so cool about sets? All elements are UNIQUE. 
    # No repetition at all. Just like you, there's only one.

    set1 = set(list1)
    set2 = set(list2)

    # Now let's find the union of these two unique sets! 
    # Union in sets is all about having all the elements from both sets, 
    # but without any duplicates. It's kind of like inviting people to a grand party!
    # You don't invite one person twice, do you? Well, this works same way!

    union_set = set1.union(set2)

    # We have our union! But the game isn't over yet. 
    # We need our result as a LIST, not a set. So let's convert this back into a list.

    union_list = list(union_set)

    # Wow, we did it! Let's return this brand-new, shiny, unified list!

    return union_list

# Time to test our amazing function
def main():
    """ Driving function """

    # Two lists for our grand unification experiment!
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    
    # Print the union of these two lists.
    print("Union of two list is: ", list_union(list1, list2))

# Using the special variable __name__
# Evaluate whether the module was run directly, not imported.
if __name__ == "__main__":
    main()

# So, that's it for this job! 
# A simple, neat function to find union of two lists.
# Doesn't that feel awesome? 
# Making tiny little things that solve big problems... That's what coding is all about!
    
# Happy Coding. Adiós!
