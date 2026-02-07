
# Howdy partner! This little treasure right here is called RepunitChecker.
# It's a little command-line python script designed to check if a number is a repunit in decimal. 

# Guess what? No GUI required! You don't need no stirrup to ride this horse, cowboy.
# It's a solo rider, needs no dependencies, won't take help from no pesky API, and it's multilingual in python across all terrains— Windows, Mac, or Linux!

# Enough chitchat, let's giddy up!

def is_repunit(n):
    """
    Say hello to is_repunit, a function that checks if a given number 'n' is a repunit.
    What in tarnation is a repunit, you ask? It's a number like 11, 111, or 1111 where all digits are 1.
    """
    # To check if a number is a repunit, we gotta see if it's a '1' followed by zeroes (in binary). 
    # If so, it's a repunit because if you subtract 1 from it, you'll get a binary number that is nothing but '1's. 
    # And if we do an 'and' of these two numbers, we get 0. As simple as cow tipping, ain't it?

    return n & (n - 1) == 0 and n != 0

def main():
    """
    Wrangling all those repunits in the main function! This good ole' function is a conversationalist— 
    likes to interact with the user through the command line, you see.
    Type in a number and the function will tell ya if it's a repunit or not.
    """
    # Asking for a number.
    number = int(input("Gimme a number, partner: "))

    # Checking if it's a jolly good repunit.
    if is_repunit(number):
        print(f"Yeehaw! {number} is a repunit!")
    else:
        print(f"Dang! {number} ain't a repunit!")

# Telling python to start the rodeo from the main function.
if __name__=='__main__':
    main()
    
# You made it to the end, good job partner! Enjoy your ride in the wild, wild world of python!
