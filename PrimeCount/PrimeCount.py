
# Welcome to our fantastic little PrimeCount Python script
# I'm your buddy programmer and If you follow my lead, we'll skip through some fun prime counting! 

# Python doesn't require us to import any modules for this script, it's all built-in fun!

# Let's write a helper function that checks if a number is prime or not. 
# A prime number (if you remember your school days) is a number that has only two distinct factors: 1 and itself!

def is_prime(n):
    # A happy little condition to check if number is less than 2 (as 2 is the smallest prime number)
    if n < 2:
        return False
    # 2 is a prime number, so let's get this one out of the way quickly
    if n == 2:
        return True
    # An even number can't be a prime number (except for 2 of course)
    if n % 2 == 0:
        return False
    # If we've gotten this far, it's time for a loop from 3 to the square root of n, checking for any factors.
    i = 3
    while i * i <= n:
        if n % i:
            i += 2
        else:
            return False
    return True

# Now, let's define the main function that will be our hero today, counting all prime numbers in a range!!

def count_primes(start, end):
    # We need to count our primes, let's setup an initial counter
    count = 0
    # Looping through our range (like sliding down a colourful rainbow!)
    for i in range(start, end + 1):
        # Check if each number in range is a prime, using our helper function
        if is_prime(i):
            # It's a Prime! Let's increase our counter (chiming bells and happy cheers)
            count += 1
    # Finally, return our counter (like giving away presents at the end of a fun day)
    return count

# Down here, we're outside the rollercoaster ride of our functions, and in the waiting line where we get inputs (lower and upper limits) from the user
lower = int(input("Enter lower limit of range for prime count: "))
upper = int(input("Enter upper limit of range for prime count: "))

# Now pass these inputs to our main function
num_primes = count_primes(lower, upper)

# We finally reveal the magic number of primes in the given range (like a magician opening his hat!)
print(f'There are {num_primes} prime numbers between {lower} and {upper}.')

# And....that's a wrap up folks! Take care and keep counting primes!

