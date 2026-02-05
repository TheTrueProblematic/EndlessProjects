"""
Hello there, fellow Python lover! Ready to generate some Lucas numbers? Buckle up!

So, for those who just wandered in, Lucas numbers are a sequence of numbers in which
each number is the sum of its two immediate previous terms. And the sequence starts with 2 and 1. 
So it looks something like: 2, 1, 3, 4, 7, 11, 18, 29, ...

Let's have some fun!
"""

def generate_lucas_numbers(n):
    """
    This function accepts an integer n and generates Lucas numbers up to n terms.
    """

    # Initialize the first two Lucas numbers
    lucas_numbers = [2, 1]

    # Generate the remaining Lucas numbers
    while len(lucas_numbers) < n:
        # Add the last two numbers in the list to generate the next Lucas number
        lucas_numbers.append(lucas_numbers[-1] + lucas_numbers[-2])

    return lucas_numbers[:n] 

# Let's test it with some cases
if __name__ == "__main__":
    print("The first 10 Lucas numbers are:", generate_lucas_numbers(10))

"""
And voilà! We just generated some Lucas numbers right from the console. 
Isn't Python just the best? Have fun tinkering around!
"""

