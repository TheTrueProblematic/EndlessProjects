
# Hi, Python Pals! Welcome to our fantastic Kaprekar Checker!
# In the wonderful world of numbers, Kaprekar numbers hold a special place.
# They have this magical property related to the squares of the number.
# E.g., number 45 is a Kaprekar number since 45^2 = 2025 and 20 + 25 is 45!

# So put on your mathematician hat, as we dive into the world of special numbers!

# We're following some project rules: Command Line Interface only, no dependencies, no APIs, no internet access,
# and we're staying true to our Python roots. Let's get started!

def is_kaprekar(num):
    # The square of number as a string
    square_str = str(num ** 2)
    # Length to split the square into
    length = len(square_str) // 2

    # If the number is 1, it's a Kaprekar number by definition
    if num == 1:
        return True

    # For numbers other than one, we can't have a 0 on the left split
    # because 0 won't contribute to any sum, not even nothingness!
    elif square_str[:length] == '0':
        return False

    else:
        # Magic Kaprekar check! Split the square into two parts and see if they sum to our original number
        return num == int(square_str[:length]) + int(square_str[length:])

# Main function to get user's input and check if it's that special Kaprekar number!
def main():
    # Gathering input from the lovely users!
    num = int(input("Enter a number to check if it's a Kaprekar number: "))
    
    # Time for the Kaprekar check!
    if is_kaprekar(num):
        print(f"Voila! {num} is a Kaprekar number!")
    else:
        print(f"Oops! {num} is not a Kaprekar number. Try another one!")
        
# Making sure the main function is called when we run the script!
if __name__ == '__main__':
    main()

# And that's it, folks! Our fun, number-filled adventure comes to an end. Until next time!


