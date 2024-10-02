
# FactorialFinder.py
# Hey there, bright eyed programmer! This little script is your friendly neighborhood FactorialFinder. What does it do you ask? It finds factorials, silly!

def factorial(n):
    """Calculate the factorial of a number."""
    # It all begins with one, like all great things
    if n == 0:
        return 1
    # Then we multiply and build, step by step, never looking back!
    else:
        return n * factorial(n-1)

# A little function to check if the input is an integer.
# We're picky like that, but it's because we care about quality (and type)!
def check_int(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

def take_input():
    """Take user input for a number."""
    # Come, converse with us for a bit
    number = input("Enter a number: ")

    # Let's make sure we're speaking the same language
    # There's no room for misunderstanding in Factorial Land
    if check_int(number) and int(number) >= 0:
        # Fresh out of the factorial oven, enjoy your factorial pie!
        print(factorial(int(number)))
    else:
        print("Whoops! Please input a non-negative integer.")
        take_input()

def main():
    """The main program."""
    # And so, our journey begins...
    print("Welcome to Factorial Finder!")
    take_input()

# Don't be shy, step right in.
if __name__ == "__main__":
    main()

