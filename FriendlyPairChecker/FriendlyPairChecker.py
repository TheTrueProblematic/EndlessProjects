
# FriendlyPairChecker.py

# Woo! Embarking on a fun journey of checking if two numbers are amicable pairs. So, what's an amicable pair?
# An amicable pair (m,n) consists of two integers m and n for which the sum of proper divisors of one number is equal to the other number, 
# For example, (220, 284) is an amicable pair.

# Oh, and don't worry! This script is designed to run in a fresh python environment, no dependencies at all! Just pure, joyful Python! 

# Importing the math module for some math magic!
import math

# Define a function to calculate the sum of divisors
def calculate_sum(n):
    sum = 1

    # Hey! Looping through 2 to sqrt(n). Why sqrt(n)? Because a larger factor of n must be a multiple of a smaller factor that has already been checked.
    for i in range(2, math.isqrt(n) + 1):

        # Checking if i is a divisor
        if n % i == 0:

            # If both divisors are the same, add it only once
            if i == (n/i):
                sum = sum + i
            else:
                # Otherwise add both
                sum = sum + (i + n//i)
                   
    return sum
 

# Here comes the part where we check if the pair is amicable
def check_amicable(n1, n2):
    # If sum of divisors of n1 is equal to n2 and sum of divisors of n2 is 
    # equal to n1, then voila! We have an amicable pair!
    return calculate_sum(n1) == n2 and calculate_sum(n2) == n1 


# Command-line fun begins here!
if __name__ == "__main__":
    n1 = int(input("Hello there! Please, enter the first number of the pair: "))
    n2 = int(input("And now, the second one, please: "))
      
    if check_amicable(n1,n2):
        print("Yes! The numbers",n1,"and",n2,"do form an amicable pair! Isn't that fun?")
    else:
        print("Oh snap! The numbers",n1,"and",n2,"do not form an amicable pair. Better luck next time!")

