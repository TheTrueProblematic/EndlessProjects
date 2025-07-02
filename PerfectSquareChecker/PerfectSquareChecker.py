
# Hey there, curious coder! Let's embark on a fun little journey to check if a number is a perfect square.
# And guess what? We are not using any in-built sqrt() function. Sounds cool, isn't it? Let's dive in!

# Our plan is simple! We are going to start from 1 and continue checking incrementally if the square 
# of the current number equals the input number until we reach a point where it exceeds the input number.
# If we don't find any number whose square matches the input number within this limit, then we can say 
# input number is not a perfect square. Otherwise, it is a perfect square.
# Exciting you say? Hold tight and let's jump to the code!

def is_perfect_square(n):
    '''
    Function to check if a number is a perfect square.

    Parameters:
        n (int): The number to check.
    
    Returns:
        bool: True if the number is a perfect square, False otherwise.
    '''

    if n < 1:
        # Every happy coder would love to handle exceptions, so we make sure n is a positive integer.
        return False

    # Exciting time begins, let's start our engine for checking perfect square.
    guess = 1
    while guess * guess <= n:
        if guess * guess == n:
            return True
        guess += 1

    # Well, if nothing matched by now, sorry mate, it's not a perfect square.
    return False

# Time to put our function to the test, let's go!

if __name__ == "__main__":
    n = int(input("Enter a number to check if it's a perfect square: "))
    result = is_perfect_square(n)
    if result:
        print(f"Yay! {n} is a perfect square.")
    else:
        print(f"Oh no! {n} is not a perfect square.")

# Congrats, we made it till end. Hope you enjoyed it as much as I did. Stay tuned for more fun coding adventures!


