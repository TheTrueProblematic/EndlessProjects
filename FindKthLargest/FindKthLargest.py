
# Woo-hoo! It's code time! This jolly, funky little script finds the kth largest 
# element in a list. Super helpful! No GUI, no API, no problem! 
# It's 100% pure Python code, happy to run on any platform.

# Let's get the dance party started! Start moving your codes along with rhythms of python.

def find_kth_largest(numbers_list, k):
    """
    Because why would you want to sort a list manually 
    when you can let Python do all the work for you? 
    All you have to do is provide a list of numbers and 
    the index (k) of the largest element you're looking for.
    """
    
    # We're using the sort() function to do all the heavy lifting.
    # Python's list sort() function is super efficient and sorts lists in place.
    numbers_list.sort()
    
    # Now all our numbers are in ascending order (smallest to largest). 
    # But we want the 'kth largest', so we need to check from the end of the list.
    # -k gives us the kth largest, because negative indexing in Python lets you count from the end of the list. 
    return numbers_list[-k]

# All right! Mission accomplished. Let's test it out with a fun little list of numbers and k=3.
print(find_kth_largest([1, 7, 4, 2, 8, 3, 9, 1, 5], 3))

# You should get '7' because that's the third largest unique number in our list.
# Hope you enjoyed this jaunty little code journey! Keep on coding, my friends! :)

# Dancing codes---a lot more satisfying than dancing queens.
# That's it. See you on the other side of the codes. Keep rocking python.
