
# Hello there! Welcome to our fantastic SumOfSquares program.
# This happy little program will find and spit out the sum of squares of the first N natural numbers!
# It's just as excited to calculate it as you are to see the result!

def sum_of_squares(n):
    '''The function that does the magic! Given a number n, it will calculate the sum of squares of the first n natural numbers.

    Parameters:
    n (int): The number up to which the sum of squares needs to be calculated.
   
    Returns:
    int: The sum of squares of the first n natural numbers.
    '''
    # This formula will save us a lot of time. Math to the rescue!
    sum = (n*(n+1)*(2*n+1))//6

    # All done! Time to hand it back.
    return sum

if __name__ == "__main__":   
    # Let's ask our user how far they want to calculate!
    n = int(input("Enter a number to find the sum of squares up to: "))

    # Now we'll call our magical function with the user's number.
    result = sum_of_squares(n)

    # All done! Let's give our user their answer in a nice format.
    print("The sum of squares of the first", n, "natural numbers is:", result)

#  And that's it! Simple as pie, easy as cake!
#  The user enters a number, and we return them the sum of squares up to that number.
#  Thanks for coming on this journey with me. Happy calculating!


