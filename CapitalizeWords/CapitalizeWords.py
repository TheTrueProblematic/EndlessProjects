
# Hi! This is your friendly python script, CapitalizeWords.py!
# Our mission here is super simple, yet very crucial - Capitalize the first letter of every word in a string. Exciting, isn't it?

# Ok! Let's start!

# Remember, if Python is the body, then the 'main' function is the heart of our program. 
def main():

    # I'm sure you're thrilled to provide the string whose words to be capitalized, aren't you? 
    # The input function here will capture your string. 
    string = input("Enter the string that you want to Capitalize: ")
    
    # Nice! Now, we'll call our superstar function 'capitalize_words' passing your string as the guest of honor.
    # This function will do the real magic of capitalizing the first letter of every word in your string.
    capitalized_string = capitalize_words(string)
    
    # Voila! Let's celebrate our victory. Print your shining, capitalized string. 
    print(capitalized_string)

# Awesome. Ready to meet our superstar function 'capitalize_words'? Here it is.
def capitalize_words(input_string):

    # The split method is our first helper; it will convert your string into a list of words.
    words = input_string.split()

    # Let's create an empty list, capitalized_words, which will hold our capitalized words.
    capitalized_words = []

    # Now comes the touch of magic, capitalize each word in the list using a beautiful feature of python, 'List Comprehension'.
    # The 'title' function is our magician who actually capitalizes the first letter of each word.
    capitalized_words = [word.title() for word in words]
    
    # It's time to transform our list of capitalized words back into a string.
    # Join method is happy to do this task; we'll join every word in our list into a single string with spaces in between words.
    output_string = ' '.join(capitalized_words)
    
    # Bravo! Your capitalized string is ready to return.
    return output_string

# So, Dear friend, it's time to run our main function and enjoy the show.
# The entry point of our program starts here when the python interpreter reads the source code.
if __name__ == '__main__':
    main()

# We hope you enjoyed the journey. Have a great day!

