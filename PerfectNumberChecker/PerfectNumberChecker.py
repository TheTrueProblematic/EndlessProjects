
# Hello and welcome on a fun journey with me! Today we're gonna find some Perfect Numbers!
# What's that you ask? Well, a perfect number is a positive integer that is equal to the sum of its proper positive divisors.
# So that's what we're gonna check for today! Let's get into it.

def check_perfect_number(n):
    # First, let's initialize the sum to 0. We're starting clean, nothing up our sleeves!
    sum = 0

    # And now, the magic begins! We're gonna check all numbers up to our given number.
    for i in range(1, n):
        # If our number is divisible by this one, it's a proper divisor so let's add it to the sum!
        if n % i == 0:
            sum += i
            
    # Finally, the moment of truth! If our sum equals the number we're looking for, then it's a Perfect Number!
    # Let's return that result, shall we?
    return sum == n

# Alright, we're set up! But we need a number to check, right? Let's get that from the user!
# We're using the command line here so we're gonna use input() to get that number.
number = int(input("Enter a number: "))

# And finally, let's tell the user if their number is perfect or not!
# We're using the function we just set up to check this.
if check_perfect_number(number):
    print(number,"is a Perfect Number")
else:
    print(number,"is not a Perfect Number")

# And that's it! We have a perfect number checker now!
# Hope you enjoyed our coding journey, and see you next time!
