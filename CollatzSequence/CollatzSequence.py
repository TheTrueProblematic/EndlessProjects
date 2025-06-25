
# Hey there, cool Pythonistas!
# Welcome to the land of the Collatz Sequence, where numbers hop, skip and jump!
# In this little adventure we will create a neat sequence based on some quirky rules! 
# All the fun starts with an integer, any integer you fancy...

def collatz(number):
    """This is our magical function which churns out the Collatz sequence"""
    # Is it even? Chop it by half! 
    if number % 2 == 0:
        print(number // 2)
        return number // 2

    # If not, get ready for some fun! Multiply it by 3 and add one! 
    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result

# Fun starts here! We will ask our friendly user for an integer
print("Enter a number:")
n = int(input())

# Let's get the ball rolling! 
# Starting with our choice of integer, we call our `collatz` function 
# This will continue until... (surprise!) ...we reach the number 1!
while n != 1:
    n = collatz(n)

