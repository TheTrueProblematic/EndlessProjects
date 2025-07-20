
# Hey there, fellow programmer!
# Welcome to a bright, shiny python script, lovingly named LineIntersection!
# This script is a cute little helper for everyone who’s embraced the joys of Geometry.
# So, what's the magic it does? Well, it computes the intersection point of two lines given in a coordinate form!

# Now, hold on to your hats because we're about to take off on a fun-filled Geometry adventure!

def line_intersection(line1, line2):
    # Let's start off by grabbing the coordinates of our lovely lines 
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    # We will compute the determinant - sounds fancy, huh? But it's just a number telling us something about our matrix.
    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    # Let's calculate that determinant!
    div = det(xdiff, ydiff)
    if div == 0:
       # Oops! Looks like our lines are parallel so no intersection in the Euclidean plane. But that's okay - makes life more interesting.
       # We return an empty tuple here. 
       return ()

    # Calculate the dazzle and the razzle (well, actually, the determinants) 
    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    # Behold! the point of intersection, returned as a tuple (because they're cozy and we like them).
    return x, y


# Well, that's all folks! The python magic is done...
# With this script at your side, line intersections won't be able to hide!
# Happy coding! Remember: def and for are your python friends forevermore! 😉
