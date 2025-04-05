
# Howdy! Welcome to the awesome little script named "FindKthSmallest".
# This script knows how to find out the kth smallest number in a list. Isn't that fun?
# Let's discover how it does this magic trick!

# We are not using any dependencies, so let's just start with defining a function.
def find_kth_smallest(arr, k):
    # I'm just gonna do a quick check to make sure this list has at least k elements because, you know, I can't find the 10th smallest number in a two-element list. That's just a sad truth in life.
    if k > len(arr):
        raise Exception("Uh-oh! k is bigger than the list length!")

    # I love keeping things simple and clean, Python provides a cool function called sorted.
    # This function returns a new sorted list from the elements of any list.
    # Easy-peasy, lemon squeezy! No manual sorting, no hassle!
    sorted_arr = sorted(arr)

    # Now, we just return the kth smallest element. But, keep in mind, Python uses 0-based indexing
    # So, the "1st" smallest number is actually at index 0, and the kth smallest number is at index k-1. Got it?
    return sorted_arr[k-1]


# Now, our function is comfortably waiting to be used and show off its magic trick.

# Let's do one more thing, though. Let's write a tiny script to run our function dring the command-line run.
# This will take the first command-line argument as the list of numbers and the second as the k value.
# To be able to do this, we need a bit of help from sys module.
# But don’t worry, it’s a Python built-in module. No extra dependencies!
import sys

if __name__ == "__main__":
    # Converting the first command-line argument to a list
    numbers = list(map(int, sys.argv[1].split(',')))
    # The second argument is our k
    k = int(sys.argv[2])

    # Now, let's let our function do the trick!
    print(find_kth_smallest(numbers, k))

# And voila! Our fantastic little Python script ends here. Dreamy, wasn't it?
# Now, you can run this script from the command line and find the kth smallest number.
# Just type: "python FindKthSmallest.py num1,num2,num3,...numN K" in your command line.
# And magic will happen right before your eyes. Cool, right?

