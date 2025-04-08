
# Hey there! Welcome to the world of fun and magic with Python.
# I made this script just for you, to check if a number is a 'happy number'.
# For those who don't know, a 'happy number' is one that eventually reaches 1 
# when replaced by the sum of the squares of its digits.

def is_happy_number(num):
    # To keep track of numbers in the sequence
    seen = set()
    while num != 1:
        # Go ahead and add the number to the set
        seen.add(num)
        # Get the next number by replacing this number with the sum of the squares of all digits.
        num = sum(int(digit) ** 2 for digit in str(num))
        if num in seen:
            # If the number is already in our set, we've got a loop and it's definitely unhappy :(
            return False
    # If we're here, it means we've reached 1 and our number is happy! Hurray!!!
    return True

# Here comes the main driver code.
# It will give the user a chance to plug in a number,
# and then we'll use our trusty function to check if it's a happy number.

def main():
    # I know, I know, asking for input in a while loop is risky stuff,
    # but hey, let's live a little!
    while True:
        number = input("Enter a number (or 'quit' to exit): ")
        # Time to get serious and check for that quit command
        if number.lower() == 'quit':
            break
        # User has not asked us to quit, let's figure out if this number is happy
        if is_happy_number(int(number)):
            print(f"Woohoo! {number} is a happy number!")
        else:
            print(f"Oh no :( {number} seems to be unhappy.")

if __name__ == "__main__":
    # Finally, we're ready to run our little project.
    # This line will call the main function and the magic begins!
    main()

