
# Hello Happy Programmers!
# Welcome to our lovely script - QuartileCalculator! 
# This script is going to help you calculate the first and third quartiles of a dataset. 
# Let's do some cool statistics today! 🥳

# We use the sys module here to read data from standard input.
# Don't worry! Despite sounding fancy, it comes preinstalled with python.
import sys

def calculate_quartiles(data):
    """
    This function calculates the first and third quartiles of given data. 
    """
    # Firstly, we need to sort the data! 😄
    data.sort()

    # Here we find the middle index of our data.
    center = len(data) // 2

    # Now, let's find Q1 (the first quartile). 
    # If the center is even, we find the mean of center-1 and center. 
    # Otherwise, we return the center index of first half (This also shows how flexible Python is with fractional indices!)
    Q1 = data[:center][len(data[:center]) // 2] if center % 2 == 0 else (data[:center][(len(data[:center])-1) // 2] + data[:center][(len(data[:center])-1) // 2 + 1]) / 2

    # Similarly, let's find Q3 (the third quartile).
    # Just the same as how we found Q1, but we use the other half of the data this time. 
    Q3 = data[center:][len(data[center:]) // 2] if len(data) % 2 == 0 else (data[center:][(len(data[center:])-1) // 2] + data[center:][(len(data[center:])-1) // 2 + 1]) / 2

    return Q1, Q3

def main():
    # Here's our input data! 
    # We receive it from standard input as a space-separated string, split it and convert to integers.
    data = list(map(int, sys.stdin.readline().split()))

    # Pass our lovely data to the calculating function!
    Q1, Q3 = calculate_quartiles(data)
    
    # Print the results in a fun and interesting format for our user!
    print(f"Yay! The first quartile (Q1) of your data is {Q1}, and the third quartile (Q3) is {Q3}! 🎉")

# Call the main function
if __name__ == "__main__":
    main()
    
# That's all, happy coders! 
# Keep on having fun with Python and all the cool things you can do with coding! 🚀

