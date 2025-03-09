
# Greetings! I'm your cheerful Python script, 'WordCountInFile'. 
# And, my purpose is pretty simple: count the number of words in a text file. 
# You run me from the command line, and I will get the job done in no time! 
# No GUI, no dependencies, no API, no Internet access, just plain ol' Python! 
# So, let's get started, shall we?

def count_words(filename):
    """Function to count words in a text file."""
    try:
        # Open the file in read mode ('r')
        with open(filename, 'r') as file: 
            # Read the contents of the file
            contents = file.read() 
            
            # Split the contents by whitespace to get a list of words
            words_list = contents.split()
            
            # Count the number of items in the list
            word_count = len(words_list)
            
            return word_count
    
    except FileNotFoundError:
        # If the file doesn't exist, print a friendly error message
        print(f"Oops! The file {filename} does not exist. Please check the file name and try again!")

if __name__ == "__main__":
    import sys

    # Check if the filename has been passed as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python WordCountInFile.py [filename]")
        sys.exit(1)

    # Extract the filename from command-line arguments
    filename = sys.argv[1]

    # Call the function to count words and store the result
    word_count = count_words(filename)

    # Print the word count result in a friendly manner
    print(f"The file {filename} contains {word_count} words!")

#And there you have it! A neat little script to count words in a text file with nothing but Python. 
#Hope you find it helpful and happy coding!
