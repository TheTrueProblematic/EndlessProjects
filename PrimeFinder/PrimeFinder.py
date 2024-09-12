
# Heya! I'm your chirpy code companion and today we are going on a little adventure to find some prime numbers!
# A prime number (for those who don't remember their middle school math) is a number that has exactly two distinct positive divisors: 1 and itself.
# So, buckle up! And let's start this journey to find all prime numbers up to a given number.

def is_prime(n):
    """
    Oh, look here, a little function where the magic of checking if a number is prime or not happens! Isn't this exciting!
    This function takes an integer as input and returns True if it's a prime number and False otherwise. Simple, isn't it?
    """
    # A prime number must be greater than 1
    if n > 1:
        for i in range(2, n):
            # If the number has any divisor other than 1 and itself, it's not prime. So we break the loop and jump right out!
            if (n % i) == 0:
                return False
        else:
            # If we made it here, that means the number is indeed prime! Hooray!
            return True


def find_primes(num_limit):
    """
    Here is where the real hunt happens!
    This fun function collects all the prime numbers up to the 'num_limit' given as input.
    """
    # Prepare our empty prime list. It's like our treasure chest where we store our prime findings.
    prime_numbers = []

    # Alright, let's start our hunt from 2 till the given number
    for num in range(2, num_limit+1):
        if is_prime(num):
            # If the number is prime, add it to our prime_numbers list... I mean, treasure chest!
            prime_numbers.append(num)
    
    # Finally, we return our pull of prime numbers. Aren't you excited to see what we've got!
    return prime_numbers


# Now, we are going to use our prime hunting functions and see them in action!
if __name__ == "__main__":
    num_limit = int(input("Gimme a number to find all primes up to: "))
    primes = find_primes(num_limit)
    print("Boom! Here are all the prime numbers up to", num_limit, ":", primes)

# And voila! That's how you find some prime numbers. I hope you enjoyed this little adventure as much as I did. 
# Until next time, happy coding!
