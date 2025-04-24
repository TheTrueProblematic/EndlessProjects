
# Hello, awesome coder! This here is your trusty PatternPrinter. 
# It's all decked-up to churn out some interesting shapes, such as pyramids and triangles on the command line. 
# Best part is, it doesn't need anything but plain ol' Python. So let's get rolling...

def print_pyramid(n):
    """
    This fun little function prints a pyramid.
    You know, like the beautiful ones in Egypt. But made with characters. Not so big though. :)
    """
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))

def print_triangle(n):
    """
    This one does triangles.
    Not the Bermuda kind of course! We don't want to get lost. :P
    """
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (i + 1))

def main():
    """
    Here's where we decide which lovely pattern to print.
    It's like our tour guide to the world of patterns. Cool, huh?
    """
    print("\nWelcome to the Pattern Printer!\nHope you're having an awesome coding day!\n")

    while True:
        print("\nChoose the pattern you want to print:\n1. Pyramid\n2. Triangle\n3. Exit\n")

        # Get user's choice
        choice = int(input())

        if choice == 1:
            num = int(input("\nSweet! How tall should the pyramid be?\n"))
            print_pyramid(num)

        elif choice == 2:
            num = int(input("\nAwesome! How tall should the triangle be?\n"))
            print_triangle(num)
            
        elif choice == 3:
            print("\nThank you for using Pattern Printer! Keep Coding, Stay Awesome!\n")
            break

        else:
            print("\nWhoops! I didn't get that. Could you try again, please?\n")

if __name__ == "__main__":
    main()

# And that's it! We've created our own fun patterns. With a few keystrokes, 
# you're now the artist and the canvas is your command line. Happy pattern printing! :)

