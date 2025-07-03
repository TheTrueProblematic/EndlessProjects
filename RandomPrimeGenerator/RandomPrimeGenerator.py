
# Hello happy coders! Let's dive right into this exciting project, i.e., a Random Prime Number Generator.
# What's so cool about this? You may ask. Well, in two words: Story Power.
# Primes have this magical property of being 'indivisible', adding a beautiful layer of mathematical mystery to it!

# Anyways, enough chit-chat, let's start coding!

import random

def is_prime(num):
    # A fun little function to check if a number is as 'indivisible' as it claims to be,
    # i.e., we're checking if a number is prime.
  
    if num > 1:
        # check for factors
        for i in range(2,num):
            if (num % i) == 0: # a classic divisibility check! 'indivisible' and proud?
                return False
        else:
            return True
    else:
        return False

def generate_prime(start, end):
    # OK, guys, now we're getting into the heart of our project.
    # This function is going to give us a random prime number within a given range.
    # Let's see how it works:

    # First, we get a list of all possible candidates, that is,
    # all the numbers in the range we're given.
    nums = list(range(start, end + 1))

    # Then we shuffle this list, because, hey, we want our prime to be RANDOM, remember?
    random.shuffle(nums)

    for num in nums: # Now, for each of these numbers,
        if is_prime(num): # if the number is a 'true' prime,
            return num # that's our guy! We return it right away!

    return None # If we didn't find any primes (how sad!), we return None.

# Time to test our random prime generator
# This is where we create an infinite co-routine of FUN! Imagine,
# every time the function runs, we could have a different prime. Isn't that cool?
# Note that it might look like a good oportunity to add a print statement here,
# but remember, we are just returning the prime, not printing it.
# The world outside this file need not know our prime secrets ;)
if __name__ == "__main__":
    start_range = 10
    end_range = 100
    print(generate_prime(start_range, end_range))
