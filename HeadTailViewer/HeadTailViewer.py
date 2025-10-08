
# Oh, hello there! Welcome to the HeadTailViewer script.
# It's a delightful little tool that allows you to view the first or last N lines from a file.
# This script is simple, elegant, and oh-so-useful. I mean, who wouldn't want a script like this at their fingertips?
# Now, let's dive into the journey of Python! 

import sys

def head_tail_viewer(file_path, line_number, from_end=False):
    """Function to print the first or last N lines from a file."""

    try:
        with open(file_path, 'r') as file:
            # Let's open up that file and see what magic lies within!
            lines = file.readlines()

            # head operation (view from the start of file)
            if not from_end:
                # Oh, you want the HEAD of the file? Coming right up!
                for line in lines[:line_number]:
                    print(line, end="")
                
            # Tail operation (view from the end of the file)
            else:
                # Ah, seeking the tale of the TAIL, huh? Here you go!
                for line in lines[-line_number:]:
                    print(line, end="")
            
    except FileNotFoundError:
        # Oops! Looks like the file does not exist. Let's tell the user about it.
        print(f"Looks like the file '{file_path}' does not exist. Please check the path and try again.")

if __name__ == "__main__":
    """
    This magic spell tells python to execute the following lines only when the script
    is executed directly and not being imported in another script. Pretty neat, eh?
    """

    # Let's grab the arguments from the command line.
    file_path = sys.argv[1]
    line_number = int(sys.argv[2])
    from_end = False if len(sys.argv) <= 3 else sys.argv[3] == "tail"

    # Alright, let's feed all those lovely parameters into our function and feed our curiosity!
    head_tail_viewer(file_path, line_number, from_end)

# Thank you for joining me on this delightful journey through Python land.
# It's been an absolute pleasure serving as your guide. Happy scripting!
