
# Salutations! Happy day! Let's embark on a thrilling programming journey, dabbling in the mesmerising creation of Fibonacci series!

# Just a quick pause: if you're clueless on Fibonacci series, it's a fascinating sequence of numbers where each number is the sum of two preceding ones, usually starting with 0 and 1.

# Well, digressing from the introduction, let's grab your space suits as you are going to conquer the irresistible world of pythonic coding! Bon Voyage!

def fibonacci(n):
    """This is our main function that generates the Fibonacci sequence.
    We take an integer input `n` and generate all the numbers in the Fibonacci sequence up to `n`.
    """
    # Initializing our base case conditions.  
    a,b = 0,1
    # Start of journey to Fibonacci universe!

    # Let's start a loop that'd loop till `n`. Why `n` you wonder? That's where our journey ends!
    while a < n:
        print(a, end=' ')
        # A magical swap of values!
        a, b = b, a+b
    # End of journey to Fibonacci universe!
    print()

def main():
    """Our main driver function. This is where our journey actually begins!
    We prompt the user for how many numbers of the Fibonacci sequence they want to see.
    We then pass this number into our fibonacci function to start the generation!
    """

    # Let's request the user for the 'n' number to generate fibonacci sequence till 'n'.
    n = int(input('\nHello User! Enter the number till where you want to generate the Fibonacci sequence: '))
    print("\nBuckle up! Here comes the Fibonacci sequence!\n")

    # Let's call our fibonacci function which takes off to a new universe!
    fibonacci(n)
    print("\nHope you had a fantastic journey! Until next time!\n")

# Pythonic way to call main function.
if __name__ == '__main__':
    main()

# End of our code! Partying time!!
# Hope you enjoyed the ride through the fibonacci sequence! It was ecstatic to have your company during this journey!
# This was our fun and enthusiastic take on creating a fibonacci sequence in python.
# Python is our happy place and coding brings joy and passion in an extraordinary way.
