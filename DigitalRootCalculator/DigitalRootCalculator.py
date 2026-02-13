
# Hey there! Welcome aboard to our cool python script! 🎉
# We're about to embark on an exciting journey to calculate "Digital Roots" of a number.
# You're probably wondering, "What in the world is a digital root?!" 🤨
# Pretty good question! 😄
# The digital root of a number is the a single-digit number that you get by continuously summing up the digits of a number until there’s just one digit left.
# Sounds cool, right? Now let's get down to business! 🚀

# Let's define a function 'digital_root' to do the heavy lifting for us.
def digital_root(n: int) -> int:
    """
    This function computes the Digital Root of a number.
    Parameters:
    n (int): Input number.
    Returns:
    Digital root (single digit).    
    """
    # Base condition: If the number is less than 10, it's already a single-digit number.
    # So, its digital root will be the number itself.
    if n < 10:
        return n
    # If the number isn't < 10, we'll need to split its digits and add them.
    # To split the digits, we'll convert it to a string—Python makes it super easy! 😎 
    digit_list = map(int, str(n))  # Here, map helps us cast each digit (string) back to an integer easily. Neat!
    # Now that we have the list of digits, let's use the amazing built-in 'sum' function to add 'em up!
    digit_sum = sum(digit_list)
    # But wait, what if the sum is still not a single digit number? What do we do?
    # We recursively call digital_root function, of course! 😁
    # Python's simplicity with recursion is super handy here
    return digital_root(digit_sum)

# Now, let's add the main driver function.
if __name__ == "__main__":
    # sample number to test our function
    num = 12345
    print(f"The digital root of {num} is {digital_root(num)}")
    # There you have it! The digital root of 12345 calculated at the speed of light (well, almost 😉). 
    # Care to try with your numbers? Just replace 'num' value! Have fun! 🥳

# Isn't Python just super fun and friendly? 😍 Happy Coding! 🐍

