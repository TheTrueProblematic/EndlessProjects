
# Welcome to AutomorphicChecker! :D
# This fun little script takes a number and checks if it can be called an 'Automorphic' number.
# What is an automorphic number you ask!? 
# An automorphic number is a number, the square of which ends with the same digits as the number itself! 
# Cool, isn't it? Let's see how it works! 

def is_automorphic(n):
    """
    Function to check if a number is automorphic.
    """
    # First, we square the number
    square = n**2

    # Now we convert our numbers to strings so we can check the endings!
    str_n = str(n)
    str_square = str(square)

    # If the end of our squared number string matches our original number string, voila, we have an automorphic number!
    # Else, it's just a regular, run of the mill number. Not exciting, but we still love it.
    return str_square.endswith(str_n)

# Alright, let's check for ourselves! Let's take an example of a number. How about 5?
print(is_automorphic(5))  # It should print True because 5*5=25 and it indeed ends with 5!

# Wow, thanks script, that was cool wasn't it? Feel free to substitute 5 with any number you want to check!
# Happy Automorphic hunting! ;)

