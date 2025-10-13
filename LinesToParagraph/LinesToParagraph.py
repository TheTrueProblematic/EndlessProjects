
"""
Hey there Rockstar! Welcome to the magnificent tale of the LinesToParagraph script,
your ultimate fellow in combining lines into a wrapped paragraph format. This small-yet-powerful
script is a real game changer when you feed it with multiple lines.
Let's give it a spin, shall we?
"""

import textwrap # Here comes our hero- the textwrap module!

def convert_lines_to_paragraph(lines: str, width: int =70):
    """
    We define a function that takes in a string and concatenates the lines into a paragraph.
    You may also specify the width of the paragraph (the default value is 70)
    """
    wrapped_paragraph = textwrap.fill(lines, width) 
    """
    We use the fill function to 'fill' the text into a paragraph with specified width.
    """
    return wrapped_paragraph
    """
    Return the wrapped paragraph, your beautifully crafted paragraph is ready to shine!
    """

if __name__ == '__main__':
    """
    If we're running this script directly, we should test it, right? Right!
    We're fun programmers, we test.
    """
    lines = '''Lorem ipsum dolor sit amet,
                consectetur adipiscing elit,
                sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'''
    """
    We use a multi-line string (also called docstring) for testing. Aren't they cool?
    """
    # The moment of truth, calling the function with test lines
    print(convert_lines_to_paragraph(lines))

"""
Voila! There you go sunshine, you've just combined lines into a wrapped paragraph. 
Remember, even the mightiest of epics have simple beginnings.
Happy Coding, Cheers!!!
"""

