
# Hey there, happy programmer! Here is a refreshing script for you.
# This program will determine if a given point is inside a triangle. Isn't that fun!
# And yes, every coder's dream, no GUIs, no dependencies, no APIs, no Internet access, only pure, vanilla Python.
# So, grab your coffee (or tea, or whatever you fancy), and let's dive in!

# Let's define our main function, point_in_triangle
def point_in_triangle():

    # Starting with some casual print statements for data input
    print("Hey there buddy, Enter the coordinates for the vertices of your triangle! (A, B, and C)" )
    print("Enter each coordinate as x,y pair e.g. 1,1 ")

    # Let's start by getting the triangle vertices. 
    # We split the input by commas to get two separate values.
    Ax, Ay = map(int, input("Vertex A: ").split(','))
    Bx, By = map(int, input("Vertex B: ").split(','))
    Cx, Cy = map(int, input("Vertex C: ").split(','))

    # Let's get our special point's coordinates
    print("Great! Now enter the coordinates for the point P")
    Px, Py = map(int, input("Point P: ").split(','))

    # Let's calculate the area of the triangle ABC
    # Don't worry, it's just a formula we derived in highschool, remember?
    ABC_area = abs(0.5 * (Ax*(By - Cy) + Bx*(Cy - Ay) + Cx*(Ay - By)))

    # Next, we calculate the areas of triangles ABP, BCP and CAP
    # It's the same formula, just different vertices
    # In essence we are dividing the main triangle ABC into three smaller ones with P as one of the vertices
    ABP_area = abs(0.5 * (Ax*(By - Py) + Bx*(Py - Ay) + Px*(Ay - By)))
    BCP_area = abs(0.5 * (Bx*(Cy - Py) + Cx*(Py - By) + Px*(By - Cy)))
    CAP_area = abs(0.5 * (Cx*(Ay - Py) + Ax*(Py - Cy) + Px*(Cy - Ay)))

    # So here is the trick, if P is inside ABC, then the sum of the areas of ABP, BCP and CAP will be equal to ABC
    # If not, then P lies outside the triangle
    # Isn't this smarter than your high school geometry teacher? (Just kidding)

    # Let's check this condition & print the result
    if ABC_area == ABP_area + BCP_area + CAP_area:
        print("Yay! Point P is inside Triangle ABC")
    else:
        print("Oops! Point P is not inside Triangle ABC")

# We're almost done. Let's just call our main function & run the script
# Let's compute & have some fun!
if __name__ == "__main__":
    point_in_triangle()

# And... that's it! Simple, right? Hope you enjoyed coding this as much as I did while writing. Happy coding!

