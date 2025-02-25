
# Howdy! This chirpy little script right here is your best compadre, PrimeFactorsFinder.
# It's here to whip up some prime factors of any number you throw at it, real quick.
# So buckle up, let's get going! 

# First things first, we will need to use the sys library to work from the command line
import sys

def prime_factors_finder(n): 
    # Alrighty, so our mission is to find prime factors of a given number. 
    # Let's start with the smallest prime number, 2
    i = 2

    # And here we begin our little treasure hunt for prime factors 😉
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            # Jackpot! Found a prime factor
            factors.append(i)
    if n > 1:
        factors.append(n)
    
    return factors

if __name__ == "__main__":
    # Let's grab the number given by the user in the command line
    n = int(sys.argv[1])

    # Use our super-fast prime factors finder function on it
    factors = prime_factors_finder(n)
    
    # Finally, let's show the user what we found!
    print(f"The prime factors of {n} are: {', '.join(map(str, factors))}")

# And voilà! That's our little adventure with PrimeFactorsFinder, hope you had a blast! 😃 
# Remember, this script is yours, tweak it, modify it, and run it as per your needs.
# Stay curious, keep coding, and hasta la vista! 👋
