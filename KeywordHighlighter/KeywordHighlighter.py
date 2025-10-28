
# Hi there! This is your friendly python script, ready to jazz up your text files!
# The goal for today? Highlighting specific keywords in your file. Fun, right?

# We're keeping things smooth and simple here, so no fancy libraries required. Just plain old Python.

def highlight_keywords(file_path, keywords, output_file_path):
    # Open up that beautiful suitcase (I mean, file)
    # and we're going for a read-mode road trip!
    with open(file_path, 'r') as file:
        content = file.read()

    # Time to shine some spotlight on those keywords!
    # Finding them in the jumble of words and enhancing them. Exciting!
    for keyword in keywords:
        # We bold the keyword by surrounding it with **, 
        # because even keywords need some extra love.
        content = content.replace(keyword, "**" + keyword + "**")

    # Phew! All that jazzing up must have tired the text.
    # Let's put it to rest in a new shiny file.
    with open(output_file_path, 'w') as file:
        file.write(content)

# Hey you! Yes, you. Let's give this script a spin, shall we?
# Simply fill up the blanks with your file path, keywords and the output file path 
# Do remember to keep them in quotes ('')
highlight_keywords('', [''], '')

# And there you have it folks!
# your friendly neighbourhood KeywordHighlighter, turning up the fun in python scripting.

# Remember, the aim here isn't perfection, but progress!
# Happy coding, until next time!

