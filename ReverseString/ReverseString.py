
# Hello, happy coders! 
# Get ready for some fun with this little Python script.
# This script is called "ReverseString" and it does exactly what you'd expect,
# it can make your strings do a little flip and show them to you backwards! Neat, huh?
# So it's time to defy gravity and start reversing!

# By the way, this script embraces the beauty of simplicity:
# No graphical interfaces, no dependencies, no APIs and no internet.
# Just pure, unadulterated Python!

# As you might've guessed though, this script needs to be fed with a string.
# So, whenever you want to amaze yourself with some magic, just pass your string to the awesome "ReverseString" function.

# Let's get this show on the road!

# Here's our ReverseString function :)
def ReverseString(str):
    # Python's string slicing is being a real friend here.
    # By using the step of -1, we can reverse the input string.
    # Piece of cake!
    return str[::-1]

# Now, let's keep things interesting. We will grab the user's input from the command line.
# Are you ready to flip some text? Because I am!
if __name__ == "__main__":
    import sys
    # Check if the user has passed an argument.
    if len(sys.argv) > 1:
        # The magic happens here. Watch your string flip! :)
        reversed_string = ReverseString(sys.argv[1])
        print(reversed_string)
    else:
        print("Oh no! You forgot to pass a string to reverse. Try again ;)")
        
# And that's all folks! This neat little script will turn your strings into topsy-turvy text!
# Until next time, stay curious and keep coding. Peace out!!
