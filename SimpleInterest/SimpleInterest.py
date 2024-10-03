
# Howdy! Let's calculate some simple interest. It's math time!

# Python's built-in function input() is here to save the day
# and helps us collect the data from a user. # Much appreciation to Python for making our life easier.

def main():

    # Let's ask our cool user to type in the principal amount.
    # We gotta make sure that the input is a float number (we'll accept both integers and decimal numbers).
    principal = float(input("\nEnter the principal amount: "))

    # Now it's time to ask for the rate of interest.
    # Likewise, let's convert it into a float.
    rate = float(input("Enter the rate of interest: "))

    # We won't forget the time period of course!
    # It's gonna be a float too.
    time = float(input("Enter the time (in years): "))

    # And here comes our simple interest formula - I = PRT/100.
    # I is. Without this lovely formula, we wouldn't have been able to calculate the simple interest. Thanks, math!
    simple_interest = (principal * rate * time) / 100

    # Finally, we let the user know the result by printing it out.
    print("\nThe simple interest is:", simple_interest,"\n")

# And here comes the moment to run our awesome script!
# This if __name__ == "__main__": piece means here that if this script is running directly (user
# invoked this script), then run the script. If the script is imported from other script, then do nothing.
if __name__ == "__main__":
    main()

