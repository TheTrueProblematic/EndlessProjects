
# Hey there, wonderful human (or bot) who's reading this! We're going on a little code-adventure today.
# Our mission? To find the greatest common divisor (GCD) of two numbers!

# Have no fear, our trusty steed throughout this journey would be Python, the beautiful and powerful language. Onwards!

# Let's start by defining our glorious function that will find the GCD of two numbers.
def find_gcd(x, y):
    # We're using a while loop here. It might seem scary at first, but don't worry, we've got this!
    while(y):
        # In Python, the single-equals symbol (=) means we're assigning something, and the double-equals symbol (==) means we're comparing. So x, y = y, x % y means that we're assigning new values to x and y.
        x, y = y, x % y

    # et voila! We have the GCD, which happens to be the new value of x we got from our loop.
    return x

# Now that we have our heroic GCD function,
# let's move on to the main function, the brains of our programme that dictates the flow and controls all proceedings.
def main():
    # Fear not, dear adventurer, for our input command will guide us to the numbers for our GCD quest.
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # This part is all about printing out the GCD to the user.
    # Notice how we're using the .format() function to dynamically replace {} with our variables. Pretty cool!
    print("The GCD of {} and {} is {}".format(num1, num2, find_gcd(num1, num2)))

# If our program is being run (as opposed to being imported),
# the below line will ensure our main function is fired up.
# It's like the secret password to start our adventure, how fun!
if __name__ == '__main__':
    main()
# Woohoo, programming adventure completed! You did great. We created a program to find the GCD of two numbers. An adventurer and a programmer, who would've thought? Keep up the fantastic work, my friend!    

