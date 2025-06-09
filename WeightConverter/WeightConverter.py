
# Hey there happy programmers. Welcome to the WeightConverter project! 
# This whimsical little python script is here to help you convert between different units of weight.
# We'll be having fun with kilograms, pounds, and ounces today.

# Ready to dive in? Okay let's go!

# First things first, we'll want to create our conversion functions. 
# We need to be able to convert between any of the units, so we'll need a few different ones.

def kg_to_pounds(kg):
    # Convert Kilograms to Pounds? No problemo!
    return kg * 2.20462
  
def pounds_to_kg(pounds):
    # How about Pounds to Kilograms? We've got you covered!
    return pounds / 2.20462

def pounds_to_ounces(pounds):
    # Okay, how about Pounds to Ounces? You betcha!
    return pounds * 16

def ounces_to_pounds(ounces):
    # And finally, Ounces to Pounds? Easy peasy!
    return ounces / 16

# Alright awesome, we now have our conversion functions!
# Next, we're going to need a friendly little command-line interface to let our users make conversions.

def main():
    # First, we need a fancy menu for our users to see what options they have.
    print("Welcome to WeightConverter!")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    print("3. Pounds to Ounces")
    print("4. Ounces to Pounds")
    print("Enter any other key to quit")

    # Let's get the user's choice!
    option = input("Enter your option: ")
    if option == '1':
        kg = float(input("Enter weight in Kilograms: "))
        print("Weight in Pounds: ", kg_to_pounds(kg))
    elif option == '2':
        pounds = float(input("Enter weight in Pounds: "))
        print("Weight in Kilograms: ", pounds_to_kg(pounds))
    elif option == '3':
        pounds = float(input("Enter weight in Pounds: "))
        print("Weight in Ounces: ", pounds_to_ounces(pounds))
    elif option == '4':
        ounces = float(input("Enter weight in Ounces: "))
        print("Weight in Pounds: ", ounces_to_pounds(ounces))
    else:
        print("Thanks for using WeightConverter! See you next time!")

# And we're done! With just a few lines of python, we've created a simple, easy-to-use weight unit converter!
# I hope you've had as much fun reading this as I've had writing it. Happy converting!

# But wait, there's more! To make sure the fun never stops, let's make sure our script keeps running.

if __name__ == "__main__":
    while True:
        main()

