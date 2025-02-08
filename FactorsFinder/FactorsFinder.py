
# FactorFinder: A cool little script that finds all the factors of a number
# Who said math had to be boring, right? Let's find some factors!

def find_factors(num):
    """
    This function finds the factors of the given number.
    It goes through a range from 1 to the number itself (inclusive) and checks if the current number is a divisor.
    If it is, it's added to our factors list.
    """
    
    # Initialize an empty list to store our factors
    factors = [] 

    # Loop through potential factors
    for potential_factor in range(1, num + 1):
        # If the number is divisible by the potential factor, it's a factor!
        if num % potential_factor == 0:
            factors.append(potential_factor)

    # Return the final list of factors
    return factors
  
# Let's get the party started by asking user for a number
number = int(input("Enter a number to find its factors: "))

# And BOOM! Call our function and print the factors
factors_of_number = find_factors(number)
print('The factors of {} are: {}'.format(number, factors_of_number))

# There you go! Game, Set, Match!
# I really hope you enjoyed this little mathematical adventure as much as I enjoyed coding it.
# Until next time. Happy factoring!

