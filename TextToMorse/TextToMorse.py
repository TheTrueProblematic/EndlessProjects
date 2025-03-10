
# Hello my friendly programmer peers! Are you excited about Morse code as much as I am? Let's dive into this fun project!

# This fast and fun piece of code is a text to Morse code converter!
# It'll operate purely from the command line, making it smooth and easy for a simple program to run!
# It is purely written in Python and has no external dependencies, APIs, or internet access. So, no worries, it will run hassle free!
# It runs on every platform that supports Python, and it's only one Python file!

# Here's our Morse code equivalence dictionary.
# This way conversion will be a piece of cake!
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

# Now let's define our function that will convert text to Morse code!
def text_to_morse(input_text):
    # Capitalize the input since Morse code is case insensitive
    input_text = input_text.upper()
    # Transform each character via the dictionary, and join with spaces
    morse_text = ' '.join(morse_code[i] for i in input_text if i in morse_code)

    # Voila! We have the Morse code equivalent of our text. Return the result!
    return morse_text

# Here is the fun part! Let's accept input from the command line!
if __name__ == "__main__":
    import sys
    # Get the input as a string from the command line
    user_input = ' '.join(sys.argv[1:])
    # Convert the input to Morse code
    morse_code_text = text_to_morse(user_input)
    # Present the converted Morse code!
    print(morse_code_text)

# That's it! Wasn't that a fun, quick and easy Python adventure? Enjoy your Morse code and keep coding! 😀
