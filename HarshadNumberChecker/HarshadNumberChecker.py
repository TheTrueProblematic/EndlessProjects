
# Hello there, future programmer! Welcome to "HarshadNumberChecker.py"!
# This little piece of code has a fun and specific mission!
# It checks whether a given number is a Harshad Number or not. Hold on! What's a Harshad Number? 
# Great question buddy! A Harshad Number (also known as a Niven Number), is a number that is divisible by the sum of its digits.

# So, let's dive right in and make it happen!

def is_harshad_number(n):
    """Check if a number n is a Harshad Number."""
    # First of all, let's find the sum of the digits. We do this by converting the number to a string,
    # looping over each character (which are the digits), converting those back to integers,
    # and adding them up. Phew, sounds like a workout!
    digit_sum = sum(int(digit) for digit in str(n))

    # Now the easy part. We just check if our original number can be divided evenly by the digit sum. 
    # If it can, congrats! You've got a Harshad Number!
    return n % digit_sum == 0

# Time to test out our function! We'll loop over some numbers and see which ones are Harshad Numbers.
# Remember, these results should be treated with the same reverence and awe as spotting a rare bird or a shooting star.

def main():
    """Function to test if 'is_harshad_number' works perfectly or not."""
    for i in range(1, 101):
        if is_harshad_number(i):
            print(f'Woohoo! Found a Harshad number: {i}')

# Make sure we're calling main when this script is run from the CLI
if __name__ == "__main__":
    main()

# And that's it! It's a beautiful wrap! You've got a cool python program that checks for Harshad Numbers. 
# I hope you've learned something from this or even better, had a bit of fun. Keep coding! Happy Programming!

## Remember:
## Is it a Harshad Number? Only "is_harshad_number" knows for sure... 😉

