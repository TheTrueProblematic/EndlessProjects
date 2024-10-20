
# Hey there, this is our super simple, but incredibly effective AlphabetSorter!
# As we love to ensure our python code is fresh and clean, you can make sure there are absolutely no dependencies needed for this.
# The joy of this AlphabetSorter is that it will run super smoothly on any platform and requires no internet. So you can sort the characters even while climbing Mt. Everest!
# Now, let's jump right into it, shall we?

def alphabet_sorter(input_string):
    """
    This amazing function takes an input string and returns it sorted alphabetically.
    Works great right out from the command line! Just like a morning coffee, huh? :)
    """

    # Here's where the magic happens, we're taking the input string and breaking it down into individual characters.
    # Once we have our characters, we're going to sort them.
    # Python's in-built sorted function is a lifesaver for us. It does all the hard work, and we get to admire the result!
    characters = sorted(input_string)

    # Now the only task remaining is to join our beautifully sorted characters back into a string.
    # And voila! We have our alphabetically sorted string. Pretty cool, huh?
    sorted_string = "".join(characters)
    
    # All done! Return the sorted string and pat yourself on the back for a job well done!
    return sorted_string


# Now, let's make sure this wonder runs when the python script is called from the command line.
# We'll wrap it up with a nice little user prompt to enter the string they want sorted.
if __name__ == "__main__":
    user_input = input("Enter the string you want sorted alphabetically: ")
    
    # Feeding the user input into our magical alphabet sorter and printing the result.
    # Grab your popcorn and enjoy the alphabetically sorted string!
    print(alphabet_sorter(user_input))
