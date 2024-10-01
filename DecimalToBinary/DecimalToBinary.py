
# Woohoo! Python programming time, buckle up folks! 
# We're about to go on a wild ride through some number conversions.

# Remember when you first learned to count and the world was simply 1, 2, 3...? 
# Well, guess what! Numbers can wear different costumes, and today, we're going to dress them up in a binary outfit!

# So, this script right here is a tailor-made dressmaker. Its one sole purpose in life? 
# It's to take an integer in its decimal form and spin it around into its binary equivalent. Pretty cool, right?

def decimalToBinary(n):
    # While number is greater than zero
    if n > 1:
        # dividend divided by 2 calls decimalToBinary function
        decimalToBinary(n // 2)
    # Then print remainder of dividend % 2
    print(n % 2, end = '')

# Sweet! Now that's the spirit of a clever cobbler.
# But what good is a dressmaker with no customer? 

# We're now going to grab inputs from the user right from that spooky black box (otherwise known as the terminal).

# Asking user for the input
decimal_num = int(input("Enter an integer: "))

# Let's get to work, shall we?
print("Binary Representation of ", decimal_num, " is: ")
# Now decimal number will entered into function to be converted
decimalToBinary(decimal_num)
