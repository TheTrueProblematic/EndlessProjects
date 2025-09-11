
# Howdy coders! Welcome to SuffixArrayBuilder! 
# This is a neat little script to build suffix array for a string using a naive method. 
# Kiss goodbye to your suffix troubles! 

# The Python standard library is all we would need for our funny, little script here. 
# So don't worry about any other worldly dependencies!

# Without further ado, let's dive into the code!

# Function to make all the suffixes of the string
def get_all_suffixes(string):
    # We start from an empty list and fill up our magical bag of suffixes one by one 
    suffixes = [string[i:] for i in range(len(string))]
    # And the bag of suffixes is ready to go! 
    return suffixes

# Function to build the suffix array
def build_suffix_array(suffixes):
    # We use Python's in-built sorted() to sort the suffixes. Easy-peasy!
    suffix_array = sorted(range(len(suffixes)), key=lambda i: suffixes[i])
    # And Voila! Our suffix array is ready!
    return suffix_array

# Our main function, the ringmaster of our circus
def main():
    # Let's get the string from user input
    string = input("Enter a string: ")
    # and generate all suffixes of the string
    suffixes = get_all_suffixes(string)
    # It's time to build our suffix array now
    suffix_array = build_suffix_array(suffixes)
    # Let's print the suffix array for the user to see, because we love showing off our work
    print("Suffix Array is:", suffix_array)

# Python's way of saying let the show begin!
if __name__ == "__main__":
    main()
    
# That's all for now, folks! Enjoy your suffix arrays!

