
# Hey there fellow coder! I'm a jolly happy Python script called ValidParentheses 
# and I'm here to help you check if a string has valid parentheses. 
# We're going on a parentheses adventure, just you and me!

# As a scripting magician, I don't need any internet connection, 
# nor do I need to use a fancy API or any external dependencies.
# Plus, I'm so simple that I only need a single Python file to exist. Isn't that neat?

# Alright, let's dive in!

def isValid(s):
    """
    This fun function checks if the input string has valid parentheses. Yay!

    Args:
        s (str): The input string. 

    Returns:
        bool: True if parentheses are valid, False otherwise.
    """

    # Let's create a cool stack to keep track of opening parentheses
    stack = []

    # Let's also remember what each opening parenthesis matches with
    mapping = {")": "(", "}": "{", "]": "["}

    # Woosh! Time to start traversing the string
    for char in s:

        # If the character is an closing parentheses 
        # Let's check the top of our stack - did we have an opening one waiting for a mate?
        if char in mapping:

            # Our stack might be empty, but that's okay, we'll just take the top element as '#'
            top_element = stack.pop() if stack else '#'

            # Let's see if our top element is the companion our current character needs. If not, return False.
            if mapping[char] != top_element:
                return False
        else:
            # The character is an opening bracket, let's add it to our stack and continue our quest!
            stack.append(char)

    # If at the end of our exciting journey, our stack is empty, then we have indeed found valid parentheses.
    # Let's return True and celebrate our victory!
    return not stack

# My command line friends, feel free to test me by feeding me a string via command line argument
if __name__ == "__main__":
    import sys
    # Command line arguments are strings by default, no need for extra parsing
    # I'm so user friendly, I'll just use the first argument as the string to check
    print(isValid(sys.argv[1]))

