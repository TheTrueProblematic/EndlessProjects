
# First, let's start with a big hearty hello to all you coders out there! This is a "no frills", unpretentious piece of code aimed at carrying out a simple permutation test for the difference in means. So, buckle up and let's dive into the sea of code.

# Importing the basic libraries. It's like packing our bags before a journey.
import random
import math

def permute(test_list):
    # Every great story starts with a little bit of shuffling. 
    # So let's shuffle our list to randomize it.
    random.shuffle(test_list)
    return test_list

def mean(test_list):
    # Time to hit the central point, the mean of our list.
    return sum(test_list) / len(test_list)

def perm_test(sample1, sample2, perm_num=10000):
    """Function to perform permutation tests."""
    # These are our two samples, like two contrasting characters in our plot.
    
    size1, size2 = len(sample1), len(sample2)
    
    # We pool our samples, they don't mind mixing up a bit!
    pool = sample1 + sample2
    
    # Initial diff in means, kind of sets the expectations right. Storyline seems to be building up!
    initial_diff = abs(mean(sample1) - mean(sample2))

    # A counter, it's always fun to keep a count of our exciting journey.
    count = 0
    
    for _ in range(perm_num):
        # An exciting twist in the tale! We permute our pool.
        permuted_pool = permute(pool)
        
        # New samples drawn post permuting
        new_sample1 = permuted_pool[:size1]
        new_sample2 = permuted_pool[size1:]
        
        # Time for suspense! Let's see if our new difference beats the initial_diff under the hood. 
        if abs(mean(new_sample1) - mean(new_sample2)) >= initial_diff:
            # If it does, our counter get's a little push.
            count += 1
    
    # And here comes the climax! We calculate the p-value to figure out the significance.
    p_value = count / perm_num
    return p_value

# Quick test of our code. Replace with your own lists!
sample1 = [1, 2, 3, 4, 5]
sample2 = [2, 3, 4, 5, 6]

print(perm_test(sample1, sample2))

# And we arrive at "The End" of our thrilling journey of permutation tests!
# Happy coding folks. Keep that smile intact while you juggle with codes!!!

