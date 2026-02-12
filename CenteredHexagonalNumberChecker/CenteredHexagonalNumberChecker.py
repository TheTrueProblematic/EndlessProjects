
# Welcome to the CenteredHexagonalNumberChecker!
# This neat little script is a bona fide number nerd! It loves to check if any given number
# is a centered hexagonal number. Ah, number theory, isn't it beautiful?
# And best of all, this script is absolutely self-contained and needs no internet or API access.
# It's good to go on any system with a fresh python install, isn't that just simply awesome?!

# In order to use this script, all you need to do is provide it with a number via the command line,
# and it will tell you if it is a centered hexagonal number or not. It's as simple as that!

# So, without further ado, lets get into the meat of this program. Ready? Here we go!

def isCenteredHexagonalNumber(num):
    """
    This function checks whether a number is a centered hexagonal number.
    To do this, it uses the formula for the nth centered hexagonal number: 1 + 6n(n-1)/2, 
    where n is an integer. It checks if the input number equals this formula for any 
    positive integer n, up to the square root of the number.
    """
    n = 1
    while True:
        centeredHexagonal = 3*n*n - 3*n + 1 # calculating the nth centered hexagonal number
        if centeredHexagonal == num:
            return True
        elif centeredHexagonal > num:
            return False
        n += 1

if __name__ == "__main__":
    import sys
    num = int(sys.argv[1]) 
    if isCenteredHexagonalNumber(num):
        print(f"Yipee! The number {num} is a centered hexagonal number!")
    else:
        print(f"Oh no, the number {num} is not a centered hexagonal number. Better luck next time!")

# And that's all there is to it! If you've read down this far, I hope you learned something new 
# about this cool (and maybe a bit strange) little concept in number theory.
# Have fun using the CenteredHexagonalNumberChecker! Keep exploring and keep programming!
