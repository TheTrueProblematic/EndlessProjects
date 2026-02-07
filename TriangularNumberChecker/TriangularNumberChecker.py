
# Hello there! Welcome to the 'TriangularNumberChecker' python script!
# This is an exciting, command-line fun python program, designed to check if a given number is a triangular number or not.
# Not to forget, it's multi-platform capable and doesn't have any dependencies!! Yippie!! 

# Now let's dive into the code...WHAT SAY?? Yeah, let's do this!!

# Oh, before that, do you know what a Triangular Number is?
# Triangular numbers are numbers that can form an equilateral triangle. The dot representation will form a perfect equilateral triangle.
# Cool, right? Yeah, it absolutely is!!
# Let's do some smart calculations now!!

import math

def check_triangular(n):
    """
    A function to check if a number is a Triangular Number.
    We use a little bit of math here. Wanna know what? ;)
    A natural number 'n' is a triangular number if '8n+1' is a perfect square.
    So, we compute this expression and take the square root.
    If the square root is an integer (indicating a perfect square), we say "GOTCHA, it's Triangular!!"
    Otherwise, give a sad sigh and say "Nay!! Not Triangular!!"
    """
    
    # calculate the expression 8n+1 
    check_val = 8 * n + 1

    # Taking the square root. And yeah, we use the inbuilt 'math' library in python for this. Mighty useful, isn't it? ;)
    root = math.sqrt(check_val)

    # Now, dear pythonista, let's check if the root is a whole number (an integer) and accordingly return the result.
    if int(root + 0.5) ** 2 == check_val:
        return True
    else:
        return False

# Now, we write a bit of code here to interact with the user. You can call it 'The Conversation Starter'!! ;D
def main():
    number = int(input("Hey there, buddy!! Please enter the number for me to check: "))
    if check_triangular(number):
        print("\nWhoopee!! You have got yourself a Triangular number, my friend!!")
    else:
        print("\nOops!! That doesn't seem to be a Triangular number!! Why don't you try again?")

# And, let the fun begin...!!
if __name__ == "__main__":
    main()

# That's all, folks!! Hope you enjoyed the codes and the little bits of knowledge sprinkled here and there!! 
# Hasta La Vista, Dear Pythonista!! :D
