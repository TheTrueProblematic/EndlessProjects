
# Hey there! Let's bake up some scrumptious python pie!
# Our juicy pie is going to find the LCM and GCD (yum, math!).

# Let's get our hands messy and dive right in!

def find_gcd(x, y):
    """
    A tasty function to find the GCD of two numbers.

    Param x : First number
    Param y : Second number
    Returns : GCD of x and y
    """
    # Euclidean Algorithm until we find the GCD, which is basically like finding the secret sauce to our pizza!
    while(y):
        x, y = y, x % y

    return x


def find_lcm(x, y):
    """
    A mouth-watering function to find the LCM of two numbers.

    Param  x : First number
    Param  y : Second number
    Returns  : LCM of x and y
    """
    # LCM can be found by dividing the product of the two numbers by their GCD.
    # It's like splitting the dessert evenly between friends!
    lcm = (x*y)//find_gcd(x,y)
    return lcm


if __name__ == "__main__":
    # We need two numbers, so let's ask the user for them.
    # It's like asking your guests what toppings they want on their pizza.
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("The LCM of", num1, "and", num2, "is", find_lcm(num1, num2))  # Serving the 
    print("The GCD of", num1, "and", num2, "is", find_gcd(num1, num2))  # Catching two birds with one stone!

