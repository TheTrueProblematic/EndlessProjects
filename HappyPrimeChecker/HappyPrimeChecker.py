
# Howdy, partner! Welcome to HappyPrimeChecker: your new best friend for checking out if a number is both happy and prime.
# This file is written with lots of love and fun, because programming is not boring, you know? 😉

# So, let's dive into the program and join the fun!

# First things first, we'll define a function to check if the number is prime.
def is_prime(n):
    # Smallest prime number is 2. So, anything less than 2 is not prime.
    if n < 2:
        return False
    # 2 itself is a prime number.
    if n == 2:
        return True
    # If a number can be divided evenly by 2, it's not a prime number.
    if n % 2 == 0:
        return False
    # So, we check the odd factors and if we found a factor, the number is not a prime.
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False
    # If the number has passed all the tests, then it's a prime number. Congratulations!
    return True

# Now, let's move to the happiness test. Given a number, we'll check if it's a happy one.
def is_happy(n):
    # Our memory of visited cycles. Because if we stuck in a cycle, it means our number is not happy.
    visited_cycle = set()
    while n != 1 and n not in visited_cycle:
        visited_cycle.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))  # Living the happy life rule!
    # If our number is 1, then it's a happy number. Hurrah! 🎉
    return n == 1

# Now we go with the main function.
def happy_prime_checker(n):
    # If the number is prime and it's happy; it's a Happy Prime. Don't you love when things have happy endings?
    return is_prime(n) and is_happy(n)

# Now we interact with the command-line. Because we live in a CLI world!
if __name__ == "__main__":
    import sys
    # Let's say we get the number from command-line argument.
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
        # Call our happy prime checker and print the result to the user.
        print(f"Is {n} a Happy Prime number? {'Yes, it is!' if happy_prime_checker(n) else 'No, it is not!'}")
    else:
        print("Please provide a number to check. Like, python HappyPrimeChecker.py 7")

