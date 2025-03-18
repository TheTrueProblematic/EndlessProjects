# Isn't it fun to play with numbers? In this script, I'll show you how we can reverse the digits of a number.
# It's going to be a blast! Let's get started!

def reverse_number(n):
    # This function takes a number as input and reverses its digits!

    # Let's first convert the number to string because strings in python are fun to play with!!
    str_n = str(n)

    # Woohoo!! Now let's reverse the string using python's slicing feature.
    # It's quite simple actually - just ":" means take everything and "-1" means start from the end.
    # So it's like taking a stroll, but backwards! Neat, right?
    reversed_str_n = str_n[::-1]

    # Oops! Our reversed string is still a string, we want it in number form
    # Let's convert it back to integer using int() function.
    reversed_n = int(reversed_str_n)

    # And voila! We're done!
    return reversed_n


# Now we'll use our function in the main section of our code.
# Let's ask the user for a number to reverse and print it out!
# This is the interaction part, so exciting!

def main():
    # Ask for a number
    n = int(input("Hey there! Give me a number, and I'll reverse it for you! "))

    # Use our amazing number reversing function
    reversed_n = reverse_number(n)

    # Show our masterpiece to the user! 
    print(f"And voila! The reversed number is {reversed_n}. Pretty cool, huh?")

# Now the main function needs to be called when this script is run from the command line. 
# Python gives us a unique variable __name__  (Yeah it's funny like that). 
# When the script is run from command line, this variable is "__main__". 
# So we'll use this to know when to call our main function!

if __name__ == "__main__":
    # Feel the magic happen!
    main()