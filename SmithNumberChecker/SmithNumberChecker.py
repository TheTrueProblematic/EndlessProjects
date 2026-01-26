
# Heysies folks! 🎉 We're gonna make our CLI Python script called SmithNumberChecker.
# It will determine whether a given number is a Smith Number.
# What is a Smith Number, you ask? Well, a Smith Number is a composite number
# (a number more than 1 that is not a prime number) where the sum of its digits
# is equal to the sum of the digits of its prime factors.

# Let's roll 🚀

def prime_factors(n):
    """Let's get the prime factors of a number."""
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def digit_sum(n):
    """Helper function to calculate the sum of digits of a number."""
    return sum(int(digit) for digit in str(n))

def check_smith_number(num):
    """Check if a number is a Smith number."""
    factors = prime_factors(num)
    return digit_sum(num) == sum(digit_sum(factor) for factor in factors)

def main():
    """Main program flow"""
    # Let's greet the user with a friendly welcome message
    print("Welcome to Smith Number Checker! 🧮🔍")
    
    while True:
        num = input("\nPlease enter a number to check if it's a Smith number (or 'exit' to quit): ")
        if num.lower() == 'exit':
            print("\nGoodbye! 🚀")
            break

        # Ensure user input is a valid positive integer
        try:
            num = int(num)
        except ValueError:
            print("Oops! That's not a valid number. Try again!")
            continue

        # Ensure user input is a composite number
        if num < 4 or prime_factors(num) == [num]:
            print("Hmm, that's not a composite number (a number more than 1 that is not a prime number). Try again!")
            continue

        if check_smith_number(num):
            print(f"\n🎉 Woohoo! {num} is a Smith number!")
        else:
            print(f"\n🙁 Oh no! {num} is not a Smith number. Try another?")

if __name__ == '__main__':
    main()

# And voila! 🎉 We've created a Smith Number Checker.
# Feed it a number and it'll tell you if it's a Smith Number or not.
# Pretty nifty, huh?

# I'm off to celebrate with a nice cup of coffee now. ☕️
# Until next time, happy coding! 🚀

