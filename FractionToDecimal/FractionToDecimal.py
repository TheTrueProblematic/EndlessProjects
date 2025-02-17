# Isn't it a beautiful day to code? Today we're going to have some fun converting fractions into decimal! Yippie!


# we'll start by defining our main function called 'fraction_to_decimal'
def fraction_to_decimal(numerator, denominator):
    # we'll be using 'try' and 'except' to catch any sneaky zero division errors
    try:
        # dividing the numerator by the denominator to get decimal
        decimal = numerator / denominator

        # using the format function to round decimal to 2 decimal places
        decimal = "{:.2f}".format(decimal)
    except ZeroDivisionError:
        # if denominator is 0, we return an error message instead
        decimal = "Error: Denominator of a fraction cannot be zero"
    # finally once all this is done, we return the decimal
    return decimal

# now we need a way to take user input from the command line
if __name__ == "__main__":
    # we're going to catch any non-integer inputs
    try:
        # prompt the user for the numerator and the denominator of the fraction
        numerator = int(input("Enter the numerator of the fraction: "))
        denominator = int(input("Enter the denominator of the fraction: "))

        # call the function with these inputs and print the output!
        print(f"Decimal of the fraction is {fraction_to_decimal(numerator, denominator)}")
    except ValueError:
        # in case someone tries to input anything other than integer
        print("Both numerator and denominator of a fraction have to be integers")

# Running this script from command line will prompt the user to input the numerator and the denominator of the fraction. Once the inputs are given, the script will calculate and display the decimal version of that fraction.  
