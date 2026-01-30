
# Welcome to SophieGermainPrimeChecker! What an exciting journey we're about to embark on together.
# We're diving deep into the wonderful world of number theory to find some truly special primes – the Sophie Germain primes!

def is_prime(n):
    """Detect if number is prime"""
    # Always upbeat, we're starting off strong by checking if our number is less than 2.
    # If it is, then it can't be a prime, so let's return False!
    if n <= 1:
        return False
    # Now, we're going to iterate from 2 through n, our number. It's like we're throwing a party and everyone's invited up to n!
    for i in range(2, n):
        # If our number n can be divided evenly by i (with no remainder), then it's not primitive enough for our party.
        if n % i == 0:
            return False  # Whoops, not a prime. Better luck next time, n!
    # If n made it through the party without offending any guests (i.e., it's not divisible by any other numbers), then it's a prime!
    return True


def is_sophie_germain(n):
    """Check if a number n is a Sophie Germain prime"""
    # In the spirit of Sophie Germain, we're going to first check if our number is prime.
    # Sophie would surely want us to make sure of that!
    if not is_prime(n):
        return False
    # But being just a prime number itself is not enough to be a Sophie Germain prime.
    # A Sophie Germain prime is a prime number if 2n + 1 is also a prime number.
    # So let's make sure of that too!
    if not is_prime(2 * n + 1):
        return False
    # And there we have it! If n is a prime and 2n + 1 is also a prime, then n is a Sophie Germain prime.
    # Isn't that just splendid?
    return True


# Let's put our functions to use!

if __name__ == '__main__':
    # We'll start by inviting a number, let's say 5, to our prime party.
    # Change the number here to check if any other number is a Sophie Germain prime.
    test_number = 5
    # Then we put it through our Sophie Germain test!
    if is_sophie_germain(test_number):
        # If it passes, then hooray! We've found ourselves a Sophie Germain prime!
        print('{} is a Sophie Germain prime!'.format(test_number))
    else:
        # If not, that's okay too. Not all numbers can be Sophie Germain primes, but they're still special in their own ways.
        print('{} is not a Sophie Germain prime.'.format(test_number))

# That's it! I hope you enjoyed our little number party! Until next time!

