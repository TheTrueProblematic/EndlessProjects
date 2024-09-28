
# Hey there! Welcome to the fun playground of Multiplication Table generator!
# This super simple, ultra lightweight Python script can generate a multiplication
# table up to any given number you want, all in your command line! Cool, right?
# Remember, this script is your best friend, not requiring any annoying dependencies,
# GUIs, internet access or APIs. A pure Python mate ready to roll on any platform.
# Let's dive right in!

def multiplication_table(n):
    """Function to generate a multiplication table up to a given number.

    :param n: The upper limit number for the multiplication table.
    :type n: int
    """
    # Loop from 1 up to and including n
    for i in range(1, n+1):
        # A cute little divider to separate the multiplication tables
        if i != 1:
            print("--------------------------------------------")
        # We start another loop here, to print the actual table
        for j in range(1, n+1):
            # Print the multiplication results, isn't multiplication fun?
            print(f"{i} * {j} = {i*j}")
        # Woohoo! One multiplication table coming right up!

# Now, let's wrap the main part of our program in a main function
# This is a common practice in Python and it allows us to control
# the flow of our program better.
def main():
    """Main function to keep the code clean and structured."""

    print("\nWelcome to the Multiplication Table generator! 🎉 \n")
    # Asking the user to enter the upper limit for the multiplication table
    n = int(input("Please enter the upper limit for the multiplication table: "))
    # Let's call our friendly multiplication_table function with the user given number
    multiplication_table(n)


# This line checks if this file is being run directly.
# In that case, it calls the main function which starts our program.
if __name__ == "__main__":
    main()

# And that's it, folks! A pretty darn simple and fun multiplication table generator!
# Give it a spin and let me know how you liked it. Until next time, happy coding! 🚀

