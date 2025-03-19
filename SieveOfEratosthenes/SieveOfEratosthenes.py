
# Hey there buddy! Guess what this file does?
# It lists all prime numbers up to a given number 
# using a nifty trick known as the Sieve of Eratosthenes. Exciting isn't it?

# For our new friends: A prime number is a natural number greater than 1 
# that has no positive divisors other than 1 and itself. 
# The Sieve of Eratosthenes is an ancient algorithm used to find all primes up to any given limit.

# Alright, enough chatter, let's get coding!

def sieve_of_eratosthenes(max_num):
    """Generate all prime numbers up to max_num using the Sieve of Eratosthenes."""
    
    # I'm creating a list with 'max_num' positions, all set to 'True'
    primes = [True] * (max_num + 1)
    
    # Let's start from the first prime number, which is 2
    p = 2
    
    while p * p <= max_num:
        # If primes[p] is still True, then it's a prime
        if primes[p] is True:
            # Mark the multiples of p greater than or equal to the square of it
            # numbers which are multiple of p and are less than p^2 were already marked 
            for i in range(p * p, max_num + 1, p):
                primes[i] = False
        p += 1 
    
    # Printing all primes numbers
    for p in range(2, max_num):
        if primes[p]:
            print(p)

# Let's test our function! Feel free to change the number to test with other values
sieve_of_eratosthenes(30)

# If this script made your day a little less mundane, then my job as a friendly neighborhood Python script is done!
# Remember, the number you input will determine how large the list of primes is, so don't go too wild!
# On second thought... go wild, we live for a little random number chaos! ;)
# Until our next coding adventure, keep being awesomely awesome!
