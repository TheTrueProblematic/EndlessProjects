
# Hey there, fellow coder! Welcome to SimpleCalculator.py!
# This gem is a basic calculator that performs addition, subtraction, multiplication, and division. 
# It's as minimalist as it comes - no GUI, no dependencies, no APIs, no internet access! 
# And all the fun is packed into just one python file. Oh, and it's multi-platform capable to boot!

# So let's dive right into it!

def add(a, b):
    # Got two numbers and need to find their sum? Just call this function!
    return a + b

def subtract(a, b):
    # Need to find the difference between two numbers instead? This function's got you covered!
    return a - b

def multiply(a, b):
    # Multiplication's a breeze with this function right here!
    return a * b

def divide(a, b):
    # Ah, division! This function does so beautifully, but remember, kiddos - no dividing by zero!
    if b == 0:
        return "Oops! Can't divide by zero, sorry! Try again."
    return a / b

# Now for the main event! This is where the magic happens.

def main():
    # First, let's greet our user!
    print("Hello! Welcome to SimpleCalculator!")
    print("You can add, subtract, multiply or divide two numbers here.")

    # Let's get the two numbers from the user.
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # And now for the operation. Let's present the user with the options.
    print("Select the operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # And let's get their choice
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == '1':
        print("The result is: ", add(num1, num2))
    elif choice == '2':
        print("The result is: ", subtract(num1, num2))
    elif choice == '3':
        print("The result is: ", multiply(num1, num2))
    elif choice == '4':
        print("The result is: ", divide(num1, num2))
    else:
        print("Hmmm, that choice is invalid, friend. Please try again with 1, 2, 3 or 4. Thanks!")

# Let's call the main function to get this party started!
if __name__ == "__main__":
    main()
