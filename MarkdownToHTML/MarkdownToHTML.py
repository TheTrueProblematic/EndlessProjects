
# Hey there fellow coder, today we have a really fun task ahead of us!
# We're going to be translating markdown into HTML, isn't that exciting?
# No, seriously it is. Let's get started!

# Also, let's make sure we stick to python and don't use other dependencies, only the standard libraries.

# Oh yeah, also we want this script to be CLI only and multi-platform.

# Like a multi-tool, but for markdown files. Neat, huh?

# So let's get our hands dirty.

import sys  # will need this to get cmdline args
import os  # will need this to work with file paths
import re  # will need this for text processing

def parse_paragraph(para):
    '''Parse plain paragraph text - convert markdown format to HTML'''
    # we are so smart, we know markdown uses ** for bold
    para = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', para)
    # markdown uses * for italics, let's handle that too!
    para = re.sub(r'\*(.+?)\*', r'<i>\1</i>', para)
    # finally, wrap it in paragraph tags
    para = '<p>' + para + '</p>'

    # Aaand... voilà! The paragraph is ready!
    return para

def main():
    '''Main function - reads cmdline, converts markdown file to HTML'''
    # check if the script got the correct arguments
    if len(sys.argv) != 3:
        print('Uhm, not quite the right usage pal. Correct usage:\n\tMarkdownToHtml src.md dst.html.\n')
        return

    # read the markdown file... and let's hope it exists!
    try:
        with open(sys.argv[1], 'r') as mdfile:
            lines = mdfile.readlines()
    except FileNotFoundError:
        print("Hey, couldn't find the source file. Make sure the file path and name are correct!")
        return

    # Let's convert this bad boy
    html = ""
    for line in lines:
        line = line.strip()
        # If the line starts with '# ', it's a heading! Let's switch it to HTML.
        if line.startswith('# '):
            html += '<h1>' + line[2:] + '</h1>'
        # If the line starts with '## ', it's a sub-heading! Let's switch that one too.
        elif line.startswith('## '):
            html += '<h2>' + line[3:] + '</h2>'
        # If the line is not a heading, it's a paragraph.
        else:
            html += parse_paragraph(line)

    # write it to an HTML file... we're creating a website, such pros! 
    with open(sys.argv[2], 'w') as htmlfile:
        htmlfile.write(html)

    print('All done, your file is ready! Look, it\'s so shiny and new!')

# time to get this party started!
if __name__ == '__main__':
    main()
