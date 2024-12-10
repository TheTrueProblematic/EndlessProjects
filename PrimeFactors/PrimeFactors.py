
# Well hello there! Ready to do some number-crunching, are you?
# This script is lovingly named 'PrimeFactors' and its sole purpose is to serve you prime factors of any given numbers. Cool, right?
# We don't believe in fancy GUIs or APIs - just plain old command line is way more intriguing! So let's jump right in!

# It's prime time, baby!

def prime_factors(n):
    """
    Your one-stop-shop for prime factors! Isn't it exciting?
    Just feed this function a number, and watch as if magic, all prime factors are lovingly calculated and listed.
    """
    # Kick things off with an empty list to store all our prime factors
    prime_facts = []

    # Keep hammering down the number with twos until it can take no more!
    while n % 2 == 0:
        prime_facts.append(2),  # Two's company!
        n = n / 2

    # Now time for the odd fellows (pun intended!)
    # Starting from 3, iterate over every odd number up to square root of the initial number
    for i in range(3, int(n**0.5)+1, 2):

        # divide n by the odd number for as long as it's a perfect division
        while n % i == 0:
            prime_facts.append(int(i)),
            n = n / i

    # Finally if the number is still greater than 2 it means it's a prime number! So let's add it in the prime_facts list.
    if n > 2:
        prime_facts.append(int(n))

    return prime_facts  # Voila! It's Prime Time!

# And now, let's make sure our script actually does something when we run it!
if __name__ == "__main__":
    # Take a number from the user. Just play nice and ensure it's an integer :)
    num = int(input("Enter a number: "))

    # Feed the number to our awesome prime_factors function. Bon Appetite!
    prime_facts = prime_factors(num)

    # Finally let's make awesome console outputs with the prime factors of the number
    print(f"Prime factors of {num} are: ", *prime_facts)
# Till next time, Happy Number Crunching!

