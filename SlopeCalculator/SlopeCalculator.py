
# Hello! Welcome to the exciting world of Python and its wonders. 🐍🎉

# Today, let's solve some practical mathematics problems. We are going to create a Python script that calculates the slope and the intercept of a line, given two points. Love a bit of geometry, right? 😉

# WARNING: NO GUIs. NO APIs. NO INTERNET BASED FUNCTIONS. ONLY PURE PYTHON 🐍

# Let's get started:
  
def calculate_slope_and_intercept(x1, y1, x2, y2):
    # Here, we are calculating the slope (m) of the line using the formula m = (y2 - y1) / (x2 - x1). Nifty!
    slope = (y2 - y1) / (x2 - x1)

    # Now, let's calculate the y-intercept(b) using the formula b = y1 - m*x1. Isn't math amazing? 🤓
    intercept = y1 - slope * x1

    # Finally, we return the slope and intercept as a tuple because they are inseparable!
    return slope, intercept


# Now we're going right to the heart of the action 🎬
if __name__ == "__main__":
    # Let's get the coordinates of the two points from the lovely user! Make sure to type them as integers!
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))

    # Now we use our fantastic function to calculate the slope and intercept
    slope, intercept = calculate_slope_and_intercept(x1, y1, x2, y2)

    # And now to reveal our amazing results!
    print(f"The slope of the line is {slope} and the y-intercept is {intercept}.")

# And that's it. Simple, neat, and efficient! Who knew math can be such fun? 😄
# See you on the next adventure!

