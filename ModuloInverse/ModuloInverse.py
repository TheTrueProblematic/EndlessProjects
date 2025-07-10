
# Hello coder!
# They say, "Every end is a new beginning!" And so it is with numbers in modular arithmetic.
# They just keep on going and going, wrapping around in endless loops, just like our interests in them.
# Welcome to the magic world of modular multiplicative inverse!

# We are going to implement a script which calculates the modular multiplicative inverse using the 
# Extended Euclidean Algorithm. But first, let me explain what a modular multiplicative inverse is.

# Given two integers 'a' and 'm', the modular multiplicative inverse of 'a' modulo 'm' is an integer 'b' such that,
# The product of 'a' and 'b' is congruent to 1 modulo 'm'. That is, (a*b) % m == 1.
 
# Let's dive in without further ado!

# The function extended_gcd computes the greatest common divisor (gcd) of two numbers using Extended Euclidean Algorithm.
# How math-y, fun, and important it is!
def extended_gcd(a, b):
    
    # Base case where the second number 'b' becomes 0. The gcd is the first number 'a'.
    if a == 0:
        return b, 0, 1
    else:
        # Recursive call itself until it becomes the base case. How smart and quick-thinking!
        gcd, x, y = extended_gcd(b % a, a)
        
        # Swap the values of 'x' and 'y' and return the gcd, 'x' and 'y'.
        return gcd, y - (b//a) * x, x

# The function mod_inv calculates the modular multiplicative inverse of 'a' modulo 'm'.
def mod_inv(a, m):
    
    # Okay, with good vibes and high spirits, we begin the computation.
    gcd, x, y = extended_gcd(a, m)
    
    # If the gcd is not 1, the modular multiplicative inverse does not exist. Oh no, so sad :(
    # So, we need to handle this somehow. Let's just return None.
    if gcd != 1:
        return None  # No modular multiplicative inverse exists.
    else:
        # The modular multiplicative inverse exists. Hurray!
        # Return 'x' modulo 'm'. This is the petty part of Python, it returns modulo difference for negative numbers too :)
        return x % m

# Now, let's test our program with some number pairs.
# Remember that Alice's favourite number was 7. In honor of Alice, let's test our function with 'a' as 3 and 'm' as 7.
# Run it with glee and enjoy the lovely output!
a = 3
m = 7
print(mod_inv(a, m))  # This should print: 5
# Because, ( 3 * 5 ) mod 7 == 1

# Alright hotshot, hope you are happy with our joyful little journey into the land of mathematics.
# Now go and multiply your knowledge with practice. Remember, learning is a cyclic process, just like our numbers in modulo :)
