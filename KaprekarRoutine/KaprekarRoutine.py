
# Hooray! Let's dive into the wonderful world of Kaprekar's routine!
# Our journey begins with this tiny little Python file which will spread positivity and math, both at the same time.

def kaprekar_routine(n):
    # Kaprekar's routine is an exciting roller coaster in mathematics' amusement park.
    # You take a 4-digit number and do the following until you reach a constant:
    # - Arrange the digits in descending order
    # - Now arrange the digits in ascending order
    # - Subtract the second number from the first one
    # Buckle up! Here we go!

    if not (999 < n < 10000):
        return 'Hold up! Make sure your number is a 4-digit one!'  # Because Kaprekar's routine only works with 4‑digit numbers

    ride = []  # A list to keep track of our thrilling ride
    while n not in ride:
        ride.append(n)  # Board the ride
        # Rearranging digits...
        max_digit = int(''.join(sorted(str(n), reverse=True)))  # Seats are going up!
        min_digit = int(''.join(sorted(str(n))))  # and now they're going down!
        n = max_digit - min_digit  # Weeee!

    return ride  # There goes our thrill-filled ride!

# Now let's ask the user for a 4-digit number to start the ride!
if __name__ == '__main__':
    try:
        number = int(input("Give me a 4 digit number to start the ride: "))
        print('Kaprekar roller coaster:', kaprekar_routine(number))
    except ValueError:
        print("Whoops! That's not a valid ticket! Make sure to input a 4-digit number.")

# Yee-haw! There we have it! A lovely little Python script performing Kaprekar's routine!
# It loves hanging out in command line and is multi-platform capable.
# Remember, no amount of ups and downs can bring it down!

