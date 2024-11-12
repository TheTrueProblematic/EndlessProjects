
# Hello there, joyful coding friends! 🚀🎉🐍
# Today, we're designing a supercool Python script to calculate the area and perimeter of basic shapes.
# We don't need any fancy third-party libraries or the Internet to get the job done - pure Python magic is all we need! 💥✨

# Let's import the math module because we'll need pi for circle calculations
import math

# We're defining functions for each shape because that's how we like to keep things - neat and organized 😀🗂

def rectangle_area(length, breadth):
    """Calculate Rectangle Area"""
    # It's simple. The area of a rectangle is length * breadth. 📏
    return length * breadth

def rectangle_perimeter(length, breadth):
    """Calculate Rectangle Perimeter"""
    # Adding the lengths and breadths twice gives us the perimeter of our lovely rectangle. Who'd have thought? 🏞
    return 2 * (length + breadth)

def circle_area(radius):
    """Calculate Circle Area"""
    # For our cheery circles, the formula is pi*r^2. Thanks, math! 🧮
    return math.pi * radius * radius

def circle_circumference(radius):
    """Calculate Circle Perimeter or Circumference"""
    # And for the perimeter, or 'circumference', all we have to do is toss around some more pi! 2*pi*r 🎡
    return 2 * math.pi * radius

# Now comes the fun part!💡⌨

# We use a while loop to keep the program running until the user decides they're done being a geometry genius. 🧑‍🎓

while True:
    # Giving user options to choose
    shape = input("\nEnter shape to get Area and Perimeter - Rectangle(R), Circle(C), Exit(E): ").lower()

    if shape == 'r':
        length = int(input("Enter rectangle length: "))
        breadth = int(input("Enter rectangle breadth: "))
        print("Rectangle Area: ", rectangle_area(length, breadth))
        print("Rectangle Perimeter: ", rectangle_perimeter(length, breadth))
    
    elif shape == 'c':
        radius = int(input("Enter circle radius: "))
        print("Circle Area: ", circle_area(radius))
        print("Circle Perimeter (Circumference): ", circle_circumference(radius))

    elif shape == 'e':
        print("Exiting the Program. Have a great day and keep coding! ✌💻💫")
        break

    else: 
        print("Invalid Input, try again! Remember, you're doing great! 😄👍")

