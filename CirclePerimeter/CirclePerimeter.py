
# ######################################
# Hello Happy Coder! Ready for a little fun Calculus session?
# This is a Python script to calculate the perimeter (also known as circumference) of a circle.
# You just need to provide the radius and voila! You'll get the circumference.
# Cool, isn't it?
# And guess what? No dependencies or internet access needed. 
# All you need is good old Python, and you're all set!
# Without further ado, let's hop on our coding adventure!
# ######################################

# First, let's import the required module
import math

# Now, let's create a function to calculate the circumference of the circle.
# Oh, remember that the formula to calculate the circumference of a circle is 2*pi*r? Yeah, that's what we're using here!

def calculate_circumference(radius):
    """Function to calculate circumference of a circle."""
    # Our beloved formula in action!
    circumference = 2 * math.pi * radius
    return circumference

def main():
    """Main function to get input and run the calculate_circumference function."""
    # Time to interact with the user! We're kindly asking for the radius of the circle.
    radius = float(input("Please enter the radius of the circle: "))
    
    # Let's calculate the circumference using the function we defined.
    circumference = calculate_circumference(radius)
    
     # Let's print out the result, so that the user knows the circumference of the circle!
    print("The circumference of the circle is: "+ str(circumference))

# To ensure that our little code adventure runs from the command line, let's use the following condition.
if __name__ == "__main__":
    main()
    
# And that's all folks! We just made a Python script to calculate the circumference of a circle.
# Great job! Celebrate with a cup of your favorite beverage!
# Happy coding!

