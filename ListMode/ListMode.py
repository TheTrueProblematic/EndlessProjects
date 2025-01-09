
# Howdy partner! This wonderful piece of code, aptly named 'ListMode', finds the mode of a list of numbers.
# The mode, in case you didn't know, is the number that appears most frequently in a list.
# So sit back, relax, and let's get this show on the road!

# To keep things simple and dependency-free, we're going to be using Python's built-in functions only. (No APIs or GUIs here cowboy!)

def find_mode(numbers):   
    # Just like a smart sheriff keeps a tab on everyone in his town,
    # our friendly counter will keep track of all our numbers in the list
    count = {i: numbers.count(i) for i in numbers}
    
    # We'll now find which townsfolk (number) shows up the most (mode)
    max_frequency = max(list(count.values()))
    mode_val = [num for num, freq in count.items() if freq == max_frequency]
   
    # If mode_val has more than one number, we have multiple modes. 
    # Our small town's got quite a variety, eh? Let's display them all.
    if len(mode_val) > 1:
        return mode_val
    
    # Otherwise, there's just one mode: one number that loves to show up every now and then. 
    # Let's return this friendly fella!
    else:
        return mode_val[0]

# For now, we'll just use a random list of numbers for our tiny town.
# Feel free to replace "townsfolk" with your own list, or add a way to take inputs from the command line!
townsfolk = [1, 3, 6, 6, 6, 7, 7, 12, 12, 17]

# Time to see which townsfolk shows up the most!
print(find_mode(townsfolk))

# Yeehaw! Enjoy coding.


    