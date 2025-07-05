
# Howdy, fellow Pythonistas! Get ready to dive into a fun and insightful script.
# This mini-project is going to generate the famous Pascal's Triangle up to a given number of rows, N.
# For those not familiar, Pascal's triangle is a triangular array of the binomial coefficients, and it's pretty neat!

def print_pascal_triangle(N):
    ''' Function to print Pascal Triangle'''

    # here's where the action takes place
    for line in range(0, N):
 
        # Accommodate spaces for the beauty of the triangle
        for i in range(0, N - line - 1):
            print(end=" ")
 
        # Calculate value for each element in a row
        value = 1
        for i in range(0, line+1):
            print(value, end=" "),
            value = value * (line - i)
            value = value // (i + 1)
         
        # Move to the new line
        print()
 

# Here is where we ask for the number of rows, this makes our function quite interactive 
# and lets the user decide the magnitude of the triangle!
if __name__ == "__main__":
    N = int(input("Enter the number of rows for the Pascal Triangle: "))
    print_pascal_triangle(N)

# Voila! You have just traversed across the mathematical beauty of a Pascal's Triangle! 
# Python truly is amazing, isn't it? Keep coding, keep exploring!

