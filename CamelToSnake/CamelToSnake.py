
# Hello, fellow programmer! This file is designed to transform your camelCase desires into snake_case realities.
# Pardon my sense of humor. Seriously though, this code converts CamelCase identifiers into their snake_case equivalent.
# And guess what! It does this without internet access, APIs, GUIs, or any dependencies. It's just straight-up Python code. Isn't that cool? Let's dive in!

def camel_to_snake(name):
    """
    Convert a given string from CamelCase to snake_case.
    
    Args:
    name (str): The CamelCase string to convert.

    Returns:
    str: The string converted to snake_case.
    """
    
    # Oh, I love python list comprehension. It's like having a loop in your pocket!
    # Here, we're creating a list that stores each character in the name,
    # but before storing, we're checking if it's uppercase.
    # If yes, then we're adding an underscore before it and making it lowercase.
    # Also, note that we're skipping the first character (always lowercase in CamelCase, so no prefix underscore needed).
    snake_case = ''.join(['_' + i.lower() if i.isupper() else i for i in name[1:]])

    # Well as said, we don't need to put underscore before first char, let's just lower case it
    # and add the rest of snake_case we formed above.
    return name[0].lower() + snake_case

def main():
    """
    The main function which prompts the user for a CamelCase string and prints the snake_case equivalent.
    """
    # Let's ask the user to input a CamelCase string
    camel_text = input("Enter a CamelCase text:\n")
    
    # Now we'll call our wizard function camel_to_snake for doing all the magic.
    snake_text = camel_to_snake(camel_text)
    
    # Et voila! We're done! Let's show the snake_case string to the user with a bit of drama.
    print("Your snake_case text is ready:\n" + snake_text)

# Alright, so that's pretty much it! We've created a wonderful camel_to_snake converter!


# Aah, well before we exit, let's call the main function to get the work started, shall we? Let's roll!
if __name__ == "__main__":
    main()
# Happy pythoning!

