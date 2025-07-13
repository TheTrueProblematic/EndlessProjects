
# Heeeeeeey! Welcome to our fun little project!
# Buckle up, we're going on a ride to the fascinating world of Twin Primes!
# "But what ARE Twin Primes?" You may ask! 
# Well, brave intrepid adventurer of code, Twin Primes are a pair of primes (funny numbers that only divide by 1 and themselves) that have a gap of 2 between them! 

# Let's get our boots dirty with the first block of code, shall we?

def is_prime(n):
    # Wise people say a number is 2's the only even prime. All other even numbers can be divided by 2.
    # So, if our n is not 2 (since it is fair and prime itself) AND is divisible by 2 then we have bad news - it is not prime at all!
    if n != 2 and n % 2 == 0:
        return False
    
    # If n is not 2 AND is not an integer then it's also not prime.
    # We start testing divisors from 3 up to sqrt(n)+1, jumping by 2, because is there a point in testing even numbers? Nope!
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    # If our n passed all tests, it's a prime!
    return True

# Great job! Now that we have a way to identify if a number is prime, let's apply that to find our Twin Prime pairs!

def find_twin_primes(limit):
    # Initialize our twins! Cute, empty list waiting for the prime numbers to arrive.
    twins = []
    
    # We are going to start our quest for Twin Primes from number 2 and go all the way up till the given limit
    for i in range(2, limit):
        # Using the prime identifying function from before to check if both i and i+2 are prime
        # If they are, it looks like we found ourselves a Twin Prime pair! Add it to our twins list.
        if is_prime(i) and is_prime(i+2):
            twins.append((i, i+2))
    
    # Once we've checked all the numbers up to our limit, return our twins!
    return twins

# Woo-hoo!! Made it to the end of this code jungle!
# The fun part - you can just call the 'find_twin_primes' function with the limit you desire, and get ready to play with the Twin Prime pairs!
# Happy Coding!

