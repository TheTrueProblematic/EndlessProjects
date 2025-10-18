
# Hello, fellow Pythonistas!
# Welcome to the "RegexTester" - a fun and nifty tool to test your regex skills straight from the comfort of your command line.

# Could there be anything better to brighten your day? 
# We're not using any fancy stuff here, no sir. Just good ol' Python in its purest form. 
# No dependencies, no API, no internet access. How's that for simplicity?

# So grab your favourite beverage, lean back, and let's get regex-ing!

import re  # Sweet, sweet regular expressions

def main():
    # Welcoming our awesome user. Geek humor never hurt anyone!
    print('Hello, Regex Tester at your service! Ready to test your patterns?\\n')

    # First, let's get the pattern from our wonderful user.
    pattern = input('Please, enter your awesome regex pattern: ')
    # And now, we're ready for the sample text. Bring it on!
    sample_text = input('Thank you! Now, provide your impossibly hard sample text: ')
    
    # Now, the magic happens. Do you feel the excitement in the air?
    # We're compiling the regular expression pattern. How cool is that?
    regex_pattern = re.compile(pattern)
    
    # And... ta-da! We're matching the pattern against the text.
    matches = regex_pattern.findall(sample_text)

    # Finally, the moment of truth. The reveal!
    if matches:
        print('Congratulations! Matches found:')
        for match in matches:
            print(match)
    else:
        print('No matches found. But remember- "Every mistake is a learning opportunity!"')

    print('Thank you for using Regex Tester. Keep those patterns coming!\\n')

# Now, we leave this in the capable hands of Python's if __name__== '__main__'.
# The perfect line of code to end any program. Elegant and effective!
if __name__ == '__main__':
    while True:
        main()
        continue_testing = input('Would you like to continue testing? (y/n): ')
        if continue_testing.lower() != 'y':
            break
    print('Bye! Hope to see you soon! Keep testing, keep learning!')

# That's it, folks! Wasn't that a wild ride?
# Keep rolling the dice, keep testing those patterns, and most importantly, keep being awesome!

