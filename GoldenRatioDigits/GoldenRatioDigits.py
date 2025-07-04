
# Hello, lovely people!
# Welcome to our super-duper Python script!! 🎉🎉
# Today, we're going to have some fun with mathematics.
# Our project today is called "GoldenRatioDigits".
# Guess what that's about? Yep, you guessed it! 
# We are going to calculate digits of the glorious golden ratio, up to N places.
# Isn't that exciting? Let's dive right in!

# First of all, only one import for our task! We're running lean today, people.
from decimal import Decimal, getcontext

def calculate_golden_ratio(n):
    """
    This function calculates the golden ratio to N decimal places.
    🥳🎯💥

    Args:
    n : int, required
        The number of decimal places to calculate the golden ratio to.

    Returns:
    golden_ratio : Decimal
        The golden ratio calculated to n decimal places.
    """
    # We set our precision to N+1 (one extra place for the integer part of the number)
    getcontext().prec = n + 1

    # Golden Ratio is (1 + sqrt(5)) / 2, let's dive into calculation
    golden_ratio = (1 + Decimal(5).sqrt()) / 2

    return golden_ratio

if __name__ == "__main__":
    # This is where we ask the user how many decimal places they want 
    # to calculate the golden ratio to. We're all about customizability here!
    n = int(input("Enter the number of decimal places you want to calculate the golden ratio to: "))
    
    # Drum roll please... here is the big calculation!
    result = calculate_golden_ratio(n)

    # And voila! Here is our golden ratio, to N decimal places.
    print(f"The golden ratio to {n} decimal place(s) is {result}!")


# And that's it folks!! Hope you've enjoyed your ride! 
# Don't forget to come back for more mathematical wonders! 
# Stay awesome! 🔥🔥🔥

