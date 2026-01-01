
# Welcome to our joyful python journey!
# Today, we're going to create a fun little project that can render numeric data into a beautiful horizontal bar chart in ASCII.
# Remember, beauty is subjective, so ASCII art is absolutely beautiful. :)
# We're going to follow the rules of just python, no GUI, no external dependencies, no API or internet access. So let's dive in!

def draw_horizontal_bar_chart(data):
    # This function is the heart of our ASCII bar chart generator. It takes a data dictionary as an input.
  
    # To start with, let's first find out the maximum length of a label. This is required to align the bars correctly.
    max_len = max(len(str(i)) for i in data.keys())
    
    # Now, we'll iterate through each item in the data. Remember, each item is a key-value (label-value) pair.
    for label, value in data.items():
        # We are using the 'ljust' function to justify the labels to the left enough to accomodate the longest label.
        # We then join it with a row of '*' characters multiplied by the value to represent the bar.
        # So, if your value is 5, you get 5 '*' characters. How cool is that, huh?
        bar = str(label).ljust(max_len) + " " + "*" * value
        print(bar)  # Finally, we print the bar on the screen.

# Now, let's put our function to use. We need to define some data to be passed to the draw_horizontal_bar_chart function.
# Here, I'm defining a dictionary. Feel free to replace with your own data. The key is your label and the value will represent the length of the bar.

data = {
    'Apples': 5,
    'Oranges': 7,
    'Bananas': 3,
    'Grapes': 9
}

# Call our magical draw_horizontal_bar_chart function with the data we just defined. Now, sit back and watch the magic happen!
draw_horizontal_bar_chart(data)

# And that's a wrap, folks! An ASCII bar chart generator made from scratch! Wasn't that fun? 
# You can now try it on different data and have fun with it! Happy Coding! :) 
