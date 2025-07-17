
# Hello there, happy coder! We're going to have some fun with polygons today.
# Specifically, we're calculating the sum of all the interior angles in an n-sided polygon.
# Strap in, it's going to be a geometric joyride!

# No external libraries needed for this one, we're keeping it simple.
# Just good old-fashioned math and logic. 

def calculate_polygon_angle_sum(sides):
    """
    This function calculates the sum of all interior angles for an n-sided polygon.

    The formula to calculate the sum of all interior angles of an n-sided polygon is given by:
    (n-2) * 180

    Parameters: 
    sides (int): The number of sides in the polygon.

    Returns: 
    int: The sum of all interior angles of the polygon.
    """

    # The formula is straight forward: (n-2) * 180 degrees.
    # Just plug in the number of sides, do the math, and voila! 
    return (sides - 2) * 180

# Now let's make this script interactive.
# We'll prompt the user to input the number of sides in their polygon.
# Then we'll return the sum of all interior angles for that polygon.

if __name__ == "__main__":
    # Let's get the number of sides from the user.
    # The `int(input())` part will convert the user's input to an integer.
    sides = int(input("Enter the number of sides in your polygon: "))
    
    # Let's make sure the input is valid.
    # A polygon should at least have 3 sides, right?
    if sides < 3:
        print("Wait a minute, that's not a polygon! Try again, and this time enter a number greater than or equal to 3. ")

    else:
        # Now we'll calculate and print the sum of the interior angles using our function.
        print("The sum of all interior angles in your polygon is: ", calculate_polygon_angle_sum(sides)) 

# And that's all folks!
# Thanks for taking this geometric journey with me.
# Until next time, happy coding!
