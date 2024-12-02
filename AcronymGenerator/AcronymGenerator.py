# Well, buckle up because we are about to create a superfun AcronymGenerator!
# Oh, don't worry! It's just a simple python script to generate an acronym from a given phrase or words.
# Yay! Let's get started!!

def acronym_generator(phrase):
    """
    This is a fun function that takes a phrase and returns an acronym
    
    Parameters:
    phrase (str): The phrase to convert into an acronym.
    
    Returns:
    str: The acronym generated.
    """
    
    # Split each word in the phrase
    words = phrase.split()
    
    # Taking the first letter of each word
    letters = [word[0] for word in words]
    
    # Make them upercase
    letters = [letter.upper() for letter in letters]
    
    # Concatenate the letters
    acronym = ''.join(letters)
    
    # Returning the fun stuff
    return acronym

# Now let's give it a spin
if __name__ == "__main__":
    phrase = input("Enter your fun phrase: ")

    # Run the function and print the output
    print(f"The acronym for your phrase is: {acronym_generator(phrase)}")

# Oh, what a fun time we had. Until next time!
# Happy coding!