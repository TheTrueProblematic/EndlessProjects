# This is your friendly Python script, welcome :)
# We're here to calculate the centroid of a triangle. 
# It's geometry time! But don't worry. 
# I promise it won't be as scary as you think.

def calculate_centroid(x1, y1, x2, y2, x3, y3):
    # To find the centroid of a triangle with vertices (x1, y1), (x2, y2) and (x3, y3)
    # we're going to calculate the average of the x-coordinates and the y-coordinates.
    # Just a simple addition and division!
    centroid_x = (x1 + x2 + x3) / 3
    centroid_y = (y1 + y2 + y3) / 3

    # And that's it! Your centroid coordinate is (centroid_x, centroid_y)
    return centroid_x, centroid_y

# Let's test it with an example
# Here's a triangle with vertices at coordinates (1,3), (2,5) and (3,4)
print(calculate_centroid(1, 3, 2, 5, 3, 4))

# This script is your buddy even without a Graphical User Interface. 
# Just call it through your command line. 
# And don't worry, it won't go out and chat with the internet or call any API.
# Also, it's a pure Python script, no extra dependencies, nor unusual languages.
# And best of all, it fits nicely into one single Python file.
# Now go ahead, conquer your geometry problems with a smile! You've got this!