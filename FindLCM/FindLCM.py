
# This is a fun little Python script to find the least common multiple (LCM) of two numbers.
# It's gonna be a party in your command line terminal, no GUI invited!

# What's a script without some hardcore math stuff, right?
# Let's start by writing a function to find the greatest common divisor(GCD)

def gcd(n1, n2):
    """
    This function takes two numbers as the input and returns their greatest common divisor(GCD).
    """
    while(n2):
        n1, n2 = n2, n1 % n2

    return n1


def find_lcm(n1, n2):
    """
    This function takes two numbers as the input and returns their least common multiple(LCM).
    """
    # The LCM of two numbers is obtained by dividing the product of the two numbers by their GCD.
    return (n1*n2) // gcd(n1, n2)


# Now let's make it interactive!

def main():
    """
    This function asks for the input of two numbers and prints their LCM. 
    """
    num1 = int(input("Hello there! Magic number 1 please: "))
    num2 = int(input("Great choice! Now how about magic number 2: "))

    # Nagini! Fetch the LCM!
    lcm = find_lcm(num1, num2)

    print(f"\nAbracadabra! The Least Common Multiple of {num1} and {num2} is: {lcm} \n")

# Let's run this awesome LCM party!
if __name__ == "__main__":
    main()

