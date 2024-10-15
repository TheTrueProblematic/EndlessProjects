
# Hello there! You're about to dive into a bit of code magic where we're gonna
# whip up a Leap Year checker! Sounds fun? Sure does! Let's go!

# Jumping straight in, we're gonna start with defining the function - leap_year

def is_leap(year):
    # Here we're checking if the year is evenly divisible by 4. If it isn't, 
    # our year can't be a leap year (too bad), so we'll return False.
    if year % 4 != 0:
        return False

    # Now if the year is also divisible by 100, it's not enough to be a leap year, 
    # it must also be divisible by 400. Weird, right?
    elif year % 100 == 0:
        if year % 400 != 0:
            return False

    # If we've made it through all those checks, then we've got a winner! 
    # The year is a leap year so we'll return True.
    return True

# Now, let's get the main part of our script going. We're going to have the
# user input the year they want to check.
def main():
    year = int(input("Enter a year to check if it's a leap year: "))
    
    # Then we'll pass their input to our function to see if it's a leap year or not.
    if is_leap(year):
        print(f"The year {year} is a leap year! Time to celebrate!")
    else:
        print(f"Oh no! The year {year} is not a leap year.")

# Making sure our main function is kicked off when we run the script
if __name__ == "__main__":
    main()

# And there we go! A super cheerful leap year checker! Simple and convoluted, all in one!
# Hope you enjoy using it as much as I enjoyed coding it. Happy leap year checking!
