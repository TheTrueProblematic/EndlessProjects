
# Hello World!
# Or more appropriate here would be: Hello math enthusiasts and prime number lovers!
# The joy and love of prime numbers brought us here. If a number could be classified as a superhero, prime numbers would be it!
# They form the building blocks of the number system
# And today, we're heading on a joyous journey — a quest to find the 'Nth' prime number!

# Like all great journeys, let's start with a small step.
# Let us define a function that checks if a number is prime

def is_prime(n):
    """Check if a number is prime.
    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself."""
    # If it's less than 2, it can't be prime.
    if n < 2:
        return False
    # '2' is the first and only even prime number 
    if n == 2:
        return True
    # All other even numbers are not primes
    if n % 2 == 0:
        return False
    # Let's check for factors up to the square root of n
    # To improve efficiency, we will increment by '2'
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    # If we've reached this far, we've checked all factors from '2' to 'sqrt(n)', and if we found none, it's a prime
    return True


# Now we have our superhero-checker function. Let's move forward to our main quest: finding the 'Nth' prime number!

def nth_prime(n):
    """Find the nth prime number.
    We will iterate through the number space and count primes until we reach the nth one."""
    # Our prime counter starts at 0
    count = 0
    # Our candidate number starts from 2 (the first prime number)
    candidate = 2
    while True:  
        # Check if this candidate number is prime
        if is_prime(candidate):
            # Yay! We found a prime. 
            count += 1      
            # If this is the prime we're looking for, our journey ends, and we return victorious!
            if count == n:
                return candidate
        # Either way, we move to the next candidate (Step by step, remember?)    
        candidate += 1

# We're all set! The quest can be fulfilled by typing something like this:
# print(nth_prime(10))

