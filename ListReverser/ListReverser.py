
# Hello, amazing coders! Welcome to 'ListReverser' - a simple and cool python script.
# Here, we are up to reverse the order of elements in a list, like a pro.
# Keep coding, keep smiling :)

# No extra modules needed, just pure python :)
# Multi-platform capable and no API or internet access. You can run this cool script anywhere!

def reverse_list(input_list):
    """
    This function takes a list as input and returns it in a reversed order.
    Using Python's built-in 'reverse' function to make our job easier.
    """
    
    # Python's reverse function in action
    input_list.reverse()
    
    # And voila! Returning the reversed list!
    return input_list

if __name__ == "__main__":
    # Defining an example list
    example_list = [1, 2, 3, 4, 5]

    # Here comes our reversed list
    print(f"Original List: {example_list}")

    # Let's reverse it! - passing the example list to our own function to see it in action
    reversed_list = reverse_list(example_list)

    # Drumroll... Here's the reversed list!
    print(f"Reversed List: {reversed_list}")

# Now see that in action. Run the script and enjoy.
# Happy coding!

