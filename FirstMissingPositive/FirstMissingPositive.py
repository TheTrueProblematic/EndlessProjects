
# Hey there! This is a fun little program that finds the first missing positive integer from a list.

def firstMissingPositive(nums):
    # We start by setting missing to 1, it's the smallest positive integer
    # It's like saying, "Alright, I'm counting on number 1 to be in this list, don't let me down!"
    missing = 1

    # Let's take a look at each number in the list
    for num in sorted(nums):
        # We skip the negative integers and zero because they're not positive
        # It's like they didn't even show up to the party!
        if num <= 0:
            continue

        # If our missing number shows up, we're so happy to see it
        # we start looking for its friend: missing number + 1. 
        if num == missing:
            missing += 1

        # If we see a number larger than our missing number, we can stop searching
        # We found the party pooper who made our missing number disappear!
        elif num > missing:
            break

    # At the end, missing will be the smallest positive integer that didn't show up to the party
    # Let's tell everyone we found the party pooper
    return missing

def main():
    # Make a list of integers to test our function
    nums = [3, 4, -1, 1]

    # Call the function and print the result
    print("First missing positive integer is:", firstMissingPositive(nums))

# This is like if __name__ == "__main__": in human language
# It means "if this is where the program started, do this next"
# The next thing is calling the main function we defined earlier
if __name__ == "__main__":
    main()

