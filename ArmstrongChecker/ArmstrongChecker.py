
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Hey there, future coder! 😊
# Welcome to the world of Armstrong numbers, it's a pretty fun place to be!
# This script is here to help you out in checking whether a number is an Armstrong number or not.
# Sounds cool, huh?! So without further ado, let's dive right in!

# Just to ensure we're on the same page, an Armstrong number of three digits is an integer 
# such that the sum of the cubes of its digits is equal to the number itself. 
# For example, 371 is an Armstrong number since 3**3 + 7**3 + 1**3 = 371.
# Excited yet? Great! Let's get to it!


def armstrong_check(n):
    """Check if the input number is an Armstrong number."""
    
    # Let's first take the number as a string to easily access each digit.
    str_n = str(n)
    # initialize a variable to store the sum of the cubes
    sum_of_cubes = 0
    
    # Let the fun begin! We calculate the cube of each digit and add it to our cube sum.
    for digit in str_n:
        sum_of_cubes += int(digit) ** len(str_n)
        
    # Magic time! Is our number an Armstrong number? Let's find out!
    if sum_of_cubes == n:
        
        # If the sum equals our number, rejoice! 😄 
        # We've found an Armstrong number! 
        return True
    else:
        
        # Otherwise, alas! 😢 
        # It's not an Armstrong number. But don’t worry, there's always a next time!
        return False


def main():
    """Main function to execute the script."""
    
    # Let's get the party started by asking the user for a number!
    number = int(input("Enter a number: "))
    
    # Now is the moment of truth! Is it an Armstrong number or not? Let's find out!
    if armstrong_check(number):
        
        # If it is, celebrate! 🎉 
        # We've got ourselves an Armstrong number! 
        print(f"{number} is an Armstrong number!")
    else:
        
        # If it's not, never mind! 😞 
        # Better luck next time!
        print(f"{number} is not an Armstrong number!")


# Finally, let's invoke our main function to let the magic happen!
if __name__ == "__main__":
    main()

# Woohoo! 🥳 You made it to the end of the script! High five!
# Not every number can be an Armstrong number, but that's okay, maybe next time.
# Keep exploring, keep learning, and as always, happy coding!


