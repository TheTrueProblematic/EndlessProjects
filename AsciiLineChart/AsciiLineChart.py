
# Howdy Partner! Welcome to the AsciiLineChart.
# Our mission? Create a funky-fresh line chart from data. All in ASCII text. Mind-blowing, right?

# The rules of the game? No dependencies, no internet, no GUI. Pure Python Magic.
# Let's saddle up and get started, it's Python Time!

def plot_chart(data):
    # First off, let's handle the most important part. The data.
    # We take your data as an argument into our function. Easy-peasy.

    # Next up, we need to find the maximum and minimum values, couldn't plot the line chart without those, huh!
    max_value = max(data)
    min_value = min(data)

    # Now let's create a canvas for our ASCII art!
    # We'll have it as a two-dimensional list of spaces, plain and simple.
    # Oh, and we'll need to add 1 to the max_value to account for the top edge of the chart.
    canvas = [[" " for _ in range(len(data))] for _ in range(max_value - min_value + 1)]

    # The next stage? Plotting our data onto the canvas!
    # We'll mark each point with a "X", to give our line chart that authentic ASCII feel.
    for i, value in enumerate(data):
        canvas[max_value - value][i] = "X"

    # We've got our data all plotted, but it's a little muddled up. We gotta flip it!
    # Why? Because in 2D lists, rows are read from top to bottom. But we want our chart from bottom to top!
    # So we simply reverse the canvas.
    canvas = canvas[::-1]

    # Behold, the final step! Drum-roll, please...Presenting the chart!
    # Puttin' the pieces together and showin' you the final masterpiece, one row at a time.
    for row in canvas:
        print("".join(row))

# And there you have it folks, your ASCII line chart.
# Feed it some data and watch the magic happen!
# Have fun!

# Test the function with some data. Feel free to change the values to test it better.
plot_chart([1, 2, 3, 2, 3, 4, 3, 2, 1])

# Remember, I'm a friendly Python script. I don't bite!
# Made with coding love and a dash of ASCII art.

