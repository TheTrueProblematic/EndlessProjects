
# Welcome! This is your friendly neighborhood Python script, LinearRegressionCLI!
# This script was designed to perform simple linear regression and output the slope and intercepts.
# It runs on the command line, all by itself, without any GUI!
# And guess what? It doesn't need to access the internet or an API!
# It's a lone wolf, independent, relying on no dependencies whatsoever!
# Okay, enough talk. Let's crunch some numbers!

import sys

def mean(lst):
    """Computes the mean of a list"""
    # sum() and len() are built-ins in python. Pure vanilla, no dependencies!
    return sum(lst) / len(lst)

def linear_regression(x, y):
    """Performs simple linear regression and returns the slope and intercept"""

    x_mean = mean(x)
    y_mean = mean(y)
  
    n = len(x) if len(x) == len(y) else sys.exit("The lengths of x and y should be equal")

    # Calculation of slope (m) and intercept (c)
    numerator = sum([xi*yi for xi,yi in zip(x, y)]) - n * x_mean * y_mean
    denominator = sum([xi**2 for xi in x]) - n * x_mean**2

    m = numerator / denominator
    c = y_mean - m * x_mean

    return m, c


# Here's where the script starts running when it's called from the command line.
def main():
    # Command line arguments are accessed through sys.argv.
    # The first element, sys.argv[0], is the name of the python script itself.
    # The following elements are the arguments passed to the script on the command line.

    # Let's make sure cmd line passed some arguments to us!
    if len(sys.argv) < 2:
        print("Kindly provide x and y list as command line arguments")
        return

    # Inputs from the command line are strings by default
    # So, let's convert the list of strings represented as a string to a list of floats
    x = list(map(float, sys.argv[1].strip('[]').split(',')))
    y = list(map(float, sys.argv[2].strip('[]').split(',')))

    m, c = linear_regression(x, y)

    print("Processed your data! Here are the results:")
    print("Slope: ", m)
    print("Intercept: ", c)


# The following line is the official roller coaster launch trigger!
# It tells python to start running the main function when the script is called from the cmd line.
if __name__ == "__main__":
    main()
