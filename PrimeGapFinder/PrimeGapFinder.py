
# Woohoo! Let's dive into a world of prime numbers and their mysterious gaps!
# Prime numbers are like solitary islands in the vast sea of integers, but have you ever wondered how big the sea really is between two islands? 
# Well, that's exactly what we're going to find out in this PrimeGapFinder script! 

def is_prime(n):
    # First things first, we need our trusty prime-number verifier.
    # How else could we spot those lonely prime number islands?

    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    # If no divisor found, then congrats it's a prime number!
    return True

def find_prime_gaps(n):
    # Here is where the magic happens! 
    # We're gonna embark on an epic journey up to the number n, finding all the prime numbers on the way and the gaps between them.

    primes = []  # Here is where we'll store our discovered prime numbers.
    for i in range(n):
        if is_prime(i):
            primes.append(i)
            
    # Now that we have a list full of prime numbers, let's find the gaps!

    gap_list = [primes[i] - primes[i - 1] for i in range(1, len(primes))]
    return gap_list

if __name__ == "__main__":
    # The stage is set, the curtains are drawn, it's showtime!

    n = input("Enter the upper limit to find the gaps between prime numbers: ")
    # Quick check to see if the input is actually a number
    if n.isdigit():
        prime_gaps = find_prime_gaps(int(n))
        print("Here are the gaps between prime numbers up to", n, ":", prime_gaps)
    else:
        print("Oops! Seems like you didn't enter a number. The upper limit has to be a number, mate!")

# And poof! We're done!
# Our thrilling adventure of finding gaps between prime numbers comes to a brilliant close.
# Hope you had as much fun running the script as I had while writing it. Until next time, happy prime hunting!

