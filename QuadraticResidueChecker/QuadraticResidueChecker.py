
# Hello, happy coders! Today we're going to explore a very interesting topic in number theory - quadratic residues!
# A number is said to be a quadratic residue modulo n if it is congruent to the square of an integer modulo n.
# Sounds mind-boggling right? But don't worry! Python and a little bit of math wizardry to the rescue.

# Let's start our code party!

def is_quadratic_residue(n, x):
    # Whoa! What's that giant modulo doing there? Well, in a nutshell, this function will tell us if x is a quadratic residue modulo n.
    # The logic here is fairly simple - we are just checking if there is an integer y such that y^2 is equivalent to x modulo n.
    # Let's dive in!
    
    # We'll use our good old buddy, the 'for' loop, to check for each integer from 0 to n
    for y in range(n):
        if (y * y) % n == x:
            # If y^2 is equivalent to x modulo n, then Eureka! We have a quadratic residue!
            return True
    
    # If the loop ends without finding a quadratic residue, then sadly x is not a quadratic residue modulo n. 
    # But don't lose heart, coder. There are infinitely many numbers waiting to be checked out!
    return False

# Now we'll take in user input so that they can test their very own numbers!
def main():
    # Let's add some print statements to make our CLI feel like a friendly conversation with the user.
    print("Hello, fellow number theorist! Ready to check some quadratic residues?")
    
    # We'll ask for n first
    n = int(input("Please enter a positive integer for 'n': "))
    # And now for x
    x = int(input("Please enter a positive integer for 'x': "))
    
    # Here we will call our quadratic residue function and store the result
    is_residue = is_quadratic_residue(n, x)
    
    # Then we'll print out a friendly message giving the user the result they're waiting for!
    if is_residue:
        print(f"Yes, {x} is a quadratic residue modulo {n}! Math magic!")
    else:
        print(f"Alas, {x} isn't a quadratic residue modulo {n}. Better luck next time!")
        
# And that's all there is to it! A friendly script to check quadratic residues in a jiffy.
# Remember - great coders are always exploring, always learning, always hacking. So keep the code flowing!

# Finally, let's call the main function to kick-start the whole process!
if __name__ == '__main__':
    main()
