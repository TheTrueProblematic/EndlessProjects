
# FactorialDigits.py
# Hello friends! Let's adventure into the mathemagic land of factorials and digital counting!

# Python's math module will be our best pals! It has great functions for both factorial and logarithm, which we can use 
# to achieve our noble quest without any additional dependencies.
import math

# Let's get the current knight who is using our wonderful software to input his quest's number!
# We need to make sure it is a number so we are going to repeatedly ask for it until they give us a valid response.
while True:
    try:
        n = int(input("Please enter a positive number: ")) # Prompting the user for their input.
        if n < 0: # If the user input is less than 0, print a prompt again.
            print("That's not a positive number! Don't bring your negative energy here!")
            continue
        break
    except ValueError: # We've caught a wild ValueError, they didn't input a number!
        print("That's not even a number, silly! Try again!")

# Good job! They've passed the initiation. Now, let's get down to business - finding the factorial of their number!

def compute_factorial(n): 
    """
    This function uses Python's built-in 'math.factorial()' function to compute the factorial of our desired number.
    """
    return math.factorial(n)

def count_digits(number):
    """
    Now that we got our factorial, let's count the number of digits it has.
    We could convert it to a string and count, but that might be a little bit slow for large inputs.
    Instead, we are going to use a neat mathematical trick.
    Any number x has approximately log10(x)+1 digits.
    And since we are in love with approximation, we will floor it to get an int.
    """
    if number == 0:
        return 1
    else:
        digits = math.floor(math.log10(number) + 1)
    return digits

# Let's compute the factorial and count the digits!
n_factorial = compute_factorial(n)
digit_count = count_digits(n_factorial)
 
# Now it's time to reveal our calculations to the world!
print(f"The number of digits in {n} factorial is: {digit_count}")

# And... we are done! That was a fantastic journey! Thanks for tagging along!
