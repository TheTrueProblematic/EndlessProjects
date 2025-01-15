
# Hello, fellow coder! Welcome to the Pattern Printer!
# This jolly little python script is designed to create fun patterns, like pyramids and triangles.
# Simply enter a shape, a character for building and a size, and voila - an ASCII art masterpiece for your viewing pleasure!

# We start by defining our function for printing a pyramid.

def print_pyramid(char, size):
    # Looping through the number of lines defined by the size.
    for i in range(size):
        # Creating each line, the ' ' * (size - i) makes sure that we properly center the pyramid.
        print(' ' * (size - i) + char * (2 * i + 1))

# Next, we define our function for printing a triangle.
def print_triangle(char, size):
    # Similar approach as before, but without the centering.
    for i in range(size):
        print(char * (i + 1))

# Now let's define a main function to tie things together.
def main():
    # Here we get the user's input - shape, character and size.
    shape = input('Enter a shape (pyramid/triangle): ')
    char = input('Enter a character for building: ')
    size = int(input('Enter the size of the shape: '))

    # If the user chose a pyramid..
    if shape.lower() == 'pyramid':
        print_pyramid(char, size)
    # ..or if they chose a triangle.
    elif shape.lower() == 'triangle':
        print_triangle(char, size)
    else:
        print("Invalid shape, please enter 'pyramid' or 'triangle'.")

# We'll make sure main() is only called when running this script directly, not when importing from another script.
if __name__ == '__main__':
    main()
