
# Hey there! Welcome to our LeapYearDetector python file. 
# This is a fun solution to determine if a given year is a leap year or not. 
# And guess what, we're doing it the Pythonic way which is neat and simple!

# This Python script will be run from the command line and no GUI needed at all.
# And the best part, it works on a fresh installation of Python with no additional dependencies required! 
# So, let's dive in!

# Let's start off by creating a function to detect leap years. 
def is_leap_year(year):

    # Here is the logic behind a leap year:
    # Leap years occur:
    # 1) Every 4 years.
    # 2) EXCEPT for years that are exactly divisible by 100.
    # 3) BUT still including the years that are exactly divisible by 400.

    # Isn't that cool?!  
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Now, we'll create some user input and response
def leap_year_detector():
    # Let's get the year from the user.
    year = int(input("Enter a year: "))

    # Check if the input year is a leap year
    if is_leap_year(year):
        print(f"Wow! The year {year} is a leap year.")
    else:
        print(f"Oh no! The year {year} is not a leap year.")

# Finally, we'll call our function
leap_year_detector()

# And that's it - our LeapYearDetector is complete! 
# Hope you had fun going through this code as much as I did writing it! 
# Happy Coding!
