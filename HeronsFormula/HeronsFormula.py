
# Hello, happy coders! Let's dive into some fun geometry stuff! We're going to find the area of a triangle here.
# You know, those three-sided shapes you learned about in grade school? Triangles are everywhere! 
# Alright, enough chatter — time to code!

# So, we're going to use Heron's Formula. The Greek scholar Heron of Alexandria is credited with its creation.
# This is a smart formula that calculates the area of a triangle if we know the lengths of all three sides.
# Did you know that? I didn't either, until I had to write this code! You learn something new every day, huh?

def calculate_triangle_area(a, b, c):
    """
    Function to calculate the area of a triangle using Heron's Formula.

    Parameters: 
    a, b, c (float): lengths of the three sides of the triangle

    Returns: 
    float: area of the triangle
    """
    
    # First, we calculate the semi-perimeter of the triangle.
    # The semi-perimeter is just half of the triangle's perimeter.
    s = (a + b + c) / 2

    # Next, we plug our semi-perimeter and side lengths into Heron's formula.
    # We'll use the math.sqrt function to take the square root.
    # It’s as simple as ‘abc’, but it’s, you know, ‘s(s - a)(s - b)(s - c)’, under a square root! :D
    area = (s*(s-a)*(s-b)*(s-c))**0.5

    # Finally, we return our answer! Area - you are finally decoded!
    return area

# Okay, we got our function! Now, let's get to the execution part!
# But we're not hardcoding! We're going to make our program interactive. How fun is that?
if __name__ == '__main__':
    # Prompting the user for the lengths of the sides of the triangle
    a = float(input("Enter length of side a: "))
    b = float(input("Enter length of side b: "))
    c = float(input("Enter length of side c: "))
    
    # Now we simply feed our sides' lengths into our awesome function!
    area = calculate_triangle_area(a, b, c)
    
    # Let's print our result out with a nice little message.
    print("The area of the triangle is ", area)

# That's it, folks! Hope you enjoyed this code. Keep on coding and exploring. Python rules, am I right?
# Happy Coding!

