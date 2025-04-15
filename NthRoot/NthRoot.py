
# Well hello there, friendly user! Welcome to our delightful little program, "NthRoot".
# This clever little script right here is designed to have some fun with math and find the nth root of any number you'd like.

# We've taken care to ensure it's easy to use and quite universal; as long as you have a basic Python
# environment up and running (no fancy additional dependencies needed!), and you're running it from your beloved command-line interface, you're all set!

# So, shall we embark on this numerical journey? Let's dive right in!

# We start by importing the 'argparse' module built into Python. This lets us handle input straight from the command line. Isn't Python awesome?☺
import argparse

# Now, we define our function, 'nth_root'. This is where the magic happens!
# It takes in two arguments: 'number' and 'n'. We raise 'number' to the power of 1/n, and hey presto, that's your nth root!
def nth_root(number: float, n: int) -> float:
    return number**(1/n)

# Alright, it's time to deal with user input from the command-line interface.
# We create an ArgumentParser object, which will hold all the information necessary to read the command line.
parser = argparse.ArgumentParser(description="Find the nth_root of a given positive number")

# We tell the parser to expect some arguments: the number and its root
parser.add_argument('number', type=float, help='The number you want to find the root of')
parser.add_argument('n', type=int, help='The root you want to find')

# We take those arguments and parse 'em! The results go into... you guessed it... 'args'!
args = parser.parse_args()

# Now we come to the final act! We feed the numbers from the arguments into our '~magnificent~' 'nth_root' function, 
# ...and print out the result in a user-friendly format.
print("The {}-th root of {} is: {}".format(args.n, args.number, nth_root(args.number, args.n)))

# Phew! There you have it, the nth root of your number, served up right from the terminal.
# Isn't Python wonderful?

# Hope you enjoyed running this program and see you on the next programming adventure!

# Happy coding, my friend!
