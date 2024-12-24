
# Hello there! Welcome to the marvelous world of coding where we create
# beautiful things with just a few lines of code.
# This fantastic script right here, is your one-way ticket to obtain the 
# nth Fibonacci number. Isn't that exciting?

# Couple of things to note:
# We are not reaching out to the wild internet here, so no worries about your 
# data plan.
# Absolutely no dependencies! Code so clean you can eat off it.
# Pure Python, and it's platform independent. The world is your oyster!

# So, grab a cup of coffee, sit back, and let's dive in!

def nth_fibonacci(n):
    """
    Calculate the nth Fibonacci number.
    This function uses a simple while loop to find the nth Fibonacci number.
    
    Args:
    n : int, required
        The position of the Fibonacci number to return.
        
    Returns:
    int
        The nth Fibonacci number.
        
    """
    # Initial values set to 0 and 1, the first two Fibonacci numbers.
    a, b = 0, 1

    # Every good while loop needs a counter. Ours is set to 0 initially.
    counter = 0

    # Here's the majestic while loop that does the magic!
    while True:

        # When the counter equals n, we have found our number!
        # a is always the current Fibonacci number in the loop, so return it.
        if counter == n:
            return a

        # Add the last two numbers in the sequence to get the new one,
        # and then shift the pair one place to the right.
        a, b = b, a + b

        # Don't forget to increment the counter, or we'll be stuck here forever!
        counter += 1
        
# Want to see it in action? Just call the function with a number!
# For example, the 10th Fibonacci number is:
#print(nth_fibonacci(10))

