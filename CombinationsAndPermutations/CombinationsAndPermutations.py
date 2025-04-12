
# Hello there! Welcome to the super exciting world of CombinationsAndPermutations!
# This handy dandy script will help you to calculate combinations (nCr) and permutations (nPr) of a set.
# And the best part? It's so compact and self-sufficient that it doesn't need any sort of fancy extras 
# like GUIs, dependencies, or internet access. Just pure, delightful Python!

# So let's dive right into it, shall we? First things first, let's import the math module.
# Don't worry, it comes standard with Python, so you don't need to install anything else!
import math

# Here we are defining the function for calculating combinations, often referred to as "n choose r".
# We'll use the factorial function from the math module to do the heavy lifting!
def calculate_combinations(n, r):
    # If you're curious, this function uses the formula nCr = n! / (r!(n-r)!).
    # "!"" stands for factorial, which is the product of an integer and all the integers below it, e.g. 4! = 4*3*2*1.
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))

# Now, let's make a similar function for permutations, or "n permutations r".
def calculate_permutations(n, r):
    # Permutations use a similar, but not exactly the same, formula: nPr = n! / (n-r)!.
    # This gives us all the ways we can arrange r items out of a set of n.
    return math.factorial(n) / math.factorial(n - r)

# Great work so far! Let's make a little command-line interface so users can interact with these functions.
def main():
    print("Welcome to CombinationsAndPermutations!")
    n = int(input("Please enter the total number of items (n): "))
    r = int(input("Now, please enter the number of items to select or arrange (r): "))
    # Let's make sure the user has input valid values to continue.
    if n >= r:
        print("Calculating... hang tight!")
        combinations = calculate_combinations(n, r)
        permutations = calculate_permutations(n, r)
        print("Combinations (nCr): ", combinations)
        print("Permutations (nPr): ", permutations)
    else:
        print("Oops! It looks like your 'r' value is greater than your 'n' value. Please start again and enter valid numbers.")

if __name__ == "__main__":
    main()
# And that's all, folks! A delightful CLI that calculates combinations and permutations. Enjoy!
