
# Heyo future coders! Today we're going to be wrangling some text! 🤠
# Specifically, we're going to make a TextJustifier, 
# a script that fully justifies text to a specified line width. 
# We're keeping it pure Python, no extra dependencies, no GUI, and definitely no internet. 
# So sit back, grab a cup of coffee, and let's dive in!

def justify_text(input_text, line_width):
    '''
    Args:
    input_text (str): The text to be justified.
    line_width (int): The width of each line.

    Returns:
    (str): The justified text.
    '''
    # Part 1: Divide text into words. Easy peasy!
    words = input_text.split()

    # Part 2: Group words into lines. We'll start with an empty line and then work 
    # our way through the words, adding each one to the current line if it fits, 
    # and creating a new line otherwise.
    lines = []
    current_line = []
    current_length = 0

    for word in words:
        if current_length + len(word) <= line_width:
            # This word fits on the current line, so we add it.
            current_line.append(word)
            current_length += len(word) + 1  # +1 for the space after the word
        else:
            # This word doesn't fit, so we start a new line for it.
            lines.append(current_line)
            current_line = [word]
            current_length = len(word) + 1  # +1 for the space after the word

    # Don't forget to add the last line!
    lines.append(current_line)

    # Part 3: Justify the text. We'll go through each line and add extra spaces 
    # between the words to make the lines exactly the line_width long.
    justified_text = ""

    for line in lines[:-1]:  # We'll handle the last line separately
        if len(line) == 1:  # Special case: the line contains only one word
            justified_text += line[0].ljust(line_width)  # We can just pad the word with spaces
        else:
            # The line contains several words. We'll have to distribute the spaces between them.
            num_spaces = line_width - sum(len(word) for word in line)
            space_width, extra_spaces = divmod(num_spaces, len(line)-1)

            for i in range(len(line)-1):
                if i < extra_spaces:
                    # This word gets an extra space
                    justified_text += line[i] + " "*(space_width+1)
                else:
                    justified_text += line[i] + " "*space_width

            justified_text += line[-1]

        justified_text += "\n"

    # For the last line, we simply left justify it.
    justified_text += " ".join(lines[-1]).ljust(line_width)

    return justified_text

# And that's about it, folks! 🎉 We now have a pretty cool text justifier! Use it wisely. 😉
