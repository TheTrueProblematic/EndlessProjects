
# Hey there, happy coder! 😄
# Welcome to CrossProductCalculator, your friendly neighborhood python script to calculate the cross product of two 3D vectors.
# Now, you don't have to worry about calculating the cross product manually. This script is here to do that heavy lifting for you! 💪

# We'll be sticking to Python's standard library, so no dependencies involved! 🙌

def cross_product(vec1, vec2):
    """ 
    Calculate cross product of two 3D vectors.
    
    Args:
      vec1: A list or tuple containing three floats or integers.
      vec2: A list or tuple containing three floats or integers.

    Returns:
      A list containing three floats, the cross product of the two input vectors.
    """
    # Check that both vectors have three components, while we're at it, let's be kind and give a friendly error message if they don't.
    assert len(vec1) == 3 and len(vec2) == 3, "Oops! Both vectors must have exactly three components. Kindly check your vectors again. 🤓"
    
    cross_product = [vec1[1]*vec2[2] - vec1[2]*vec2[1],
                    vec1[2]*vec2[0] - vec1[0]*vec2[2],
                    vec1[0]*vec2[1] - vec1[1]*vec2[0]]
    
    # We have the cross product. Let's return it!
    return cross_product

# Kicking off the command line interface, ask the user for the components of the two vectors.
# The script runs here! 🏃‍♂️

def main():
    vec1 = tuple(float(x) for x in input("Enter the components of vector 1, separated by spaces: ").split())
    vec2 = tuple(float(x) for x in input("Enter the components of vector 2, separated by spaces: ").split())
    
    result = cross_product(vec1, vec2)
    
    # Let's print out the result in a nice, human friendly way.
    print("Voila! The cross product of your vectors is: ", result)

if __name__ == "__main__":
    # Run the code if we're running this script directly. If someone imports this script, they can use the `cross_product` function themselves!
    main()

# Woohoo! We did it! 🥳 We've created a lightweight, portable Python script to calculate the cross product of two 3D vectors.
# Keep on coding and remember to always have fun! 😃
