
# Hello there, friendly coder! Welcome to our little coding project. 😊
# This script is named "OddOrEven", just like our favourite game back in childhood!
# We're going to check whether the number given by user is odd or even. Classic, right? 🧐

# Oh, and don't worry about running this in different platforms or being connected to the internet for this.
# Nope, none of that fancy stuff here, this script is plain old simple, yet joyful Python code that is self-sufficient.
# So, buckle up, let's dive into some coding fun! 🤓

# Let's start with a function that will do our main task - checking if a number is odd or even

def check_odd_or_even(number):
    """Function that checks if a number is odd or even."""
    # Here, we use the modulo operator '%', which gives the remainder of the division of the number by 2.
    # If the remainder is 0, then the number is even, otherwise it's odd. Magic! 🎩
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Okay, so that was easy, right? But we also want to interact with our user via the command line.
# So, let's write a little function to get an integer input from our user.

def get_user_input():
    """Function to get input from user."""
    # We'll use an infinite loop to keep asking for an input until we get a valid integer.
    # It's a bit like a stubborn mule, but it gets the job done! 😄
    while True:
        # Ask for input and try to convert it to an integer
        try:
            user_input = int(input("Please enter a number: "))
            # If conversion to integer is successful, then we break the loop and return the number
            return user_input
        except ValueError:
            # If the user was a bit naughty and didn't enter a valid integer, we just kindly remind them to do so 😉
            print("That's not a valid number! Try again, please.")

# Finally, we bring it all together in the main function.
# We get the user input, check if it's odd or even, and then tell the user about it. Voila! 🥳

def main():
    """Main function to run the script."""
    # Get number from user
    number = get_user_input()
    # Check if it's odd or even
    result = check_odd_or_even(number)
    # Tell the user the result
    print(f"The number {number} is {result}!")

# And to kick it all off, we call the main function
if __name__ == "__main__":
    main()
