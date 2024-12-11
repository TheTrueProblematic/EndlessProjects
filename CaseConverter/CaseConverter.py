
# Hey there, Pythonistas! We are about to embark on a fascinating journey of text transformations. Buckle up!

# This magical Python script can convert text between uppercase, lowercase, and title case. Exciting, isn't it?

# And guess what? It needs no GUI, no dependencies, no internet, and no API. It's just pure Python - good old snakes!
# Just one humble python file performing these chunks of tasks, that's what we love to see!

# Let's dive in!

# Importing the sys module to read command-line arguments
import sys

# Class to do the magic
class CaseConverter:

    # Function to convert text to uppercase
    def to_uppercase(self, text):
        return text.upper()

    # Function to convert text to lowercase
    def to_lowercase(self, text):
        return text.lower()

    # Function to convert text to title case
    def to_titlecase(self, text):
        return text.title()

def main():
    # Whoa, wait! Before diving in, make sure you've given us something to work with!
    if len(sys.argv)!=3:
        print("Usage: python CaseConverter.py [text] [case]")
        print("case: --upper, --lower, or --title")
        sys.exit()

    text = sys.argv[1]
    case_option = sys.argv[2]
    
    # Creating object of the CaseConverter class
    converter = CaseConverter()

    # Depending on the case_option, we'll call the appropriate function
    if case_option == "--upper":  # Go big or go home! Transform my text to uppercase
        print(converter.to_uppercase(text))
    elif case_option == "--lower":  # Shhh! Let's whisper in lowercase
        print(converter.to_lowercase(text))
    elif case_option == "--title":  # Every word deserves respect. Let's titlecase it!
        print(converter.to_titlecase(text))
    else:  # Not sure what you're asking for? Let us guide you.
        print("Invalid caseoption. Please choose among --upper, --lower, or --title")

# This is where the fun begins!
if __name__ == "__main__":
    main()

# That's all folks! Our Python script is ready to transform any text you throw at it.
# Have fun experimenting with different cases. Sayonara!


