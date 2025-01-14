
# Hello fellow coder! Hope you're having a great day :D
# Let's dive straight into some fun coding. 
# Today we'll be creating a pretty cool (if I may say so myself) square root calculator.
# The catch? We can't use the square root function. I know...crazy right? Well, hold on tight and enjoy the ride.

# So here's the starting point.
def squareRoot(number):
    
    # Initially we'll start guessing the square root (because who doesn't love guessing?)
    # We can use 0.0 as the start of our guess.
    guess = 0.0

    # Now we'll create an optimum level of precision we want our guess to reach.
    # We can tweak this as per our requirement.
    precision = 0.00001

    # Ok, onto the next step. We need to update our guesses until we get to that level of precision we talked about before.    
    while (guess * guess - number >= precision):
        # We're using the concept of Binary Search to approach the root value, which makes this method pretty efficient.
        guess += precision

    # And there you have it folks! We have our square root.
    # Just return the current guess when the difference becomes less than the precision.
    return guess
            
# This is where it all begins!
# Here, I'll prompt the user to input the number whose square root they wish to compute.
def main():
    number = float(input("Enter the number you want the square root of: "))
    root = squareRoot(number)  # There you go, passing it to the function we wrote above.
    print(f"The square root of {number} is approximately {root}.")  # Using an f-string to print out the calculated square root.

# Making sure the main function is our entry point.
if __name__ == "__main__":
    main()

# Hope the comments made the code easier to understand and maybe even brought a smile to your face. 
# After all, coding should always be fun, right? Happy coding! 

