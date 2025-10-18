
# Hello there, Happy Programmer!🎉
# Let's go on an epic journey together to create a delightfully simple Python script which will 
# convert basic BBCode tags to HTML!

# This adventure we are embarking on is quite exciting. Plus, no clunky GUI, no pesky dependencies 
# or troublesome internet access. Just pure, joyful Python! 😄

# Onward to the code! 🚀

# We are defining an exquisite list of tuples here that represents BBCode tags and their HTML counterparts. 
bb_html_map = [('[b]', '<b>'),('[/b]', '</b>'),
               ('[i]', '<i>'),('[/i]', '</i>'),
               ('[u]', '<u>'),('[/u]', '</u>')]

# Here is the main function, our trusty steed Mount BBCodeToHTML!
def bb_to_html(input_str):
    """This function takes in a string with BBCode and returns the string with the BBCode converted to HTML."""
    # We're walking through our bb_html_map with grace, replacing BBCode tags with HTML tags one by one!
    for bb, html in bb_html_map:
        input_str = input_str.replace(bb, html) # Voila! Tag replaced!
        
    return input_str 

# A beginning of our sentient journey with a casual print to Console. 
if __name__ == "__main__":
    bb_str = "This is a bbcode string with [b]bold[/b], [i]italic[/i] and [u]underline[/u]!"
    # Time to see our ‘bb_to_html’ function in action!
    converted_str = bb_to_html(bb_str)
    
    print(converted_str) # Ta-da! Here's the final result! Isn't it lovely?

# And that's the end of our little coding adventure. Easy peasy lemon squeezy! 🍋
# Take care and happy coding! 🐍

