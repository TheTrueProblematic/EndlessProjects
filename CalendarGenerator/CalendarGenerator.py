
# Hey there, fellow Pythonista! This is your happy little CalendarGenerator script.
# It creates a super neat text-based calendar for a given month and year!
# It's light, snappy and doesn't need the internet or any exotic imports to do its magic!
# Let's dive right in, shall we?

# First we'll need the 'calendar' module to generate the calendars.
import calendar

# Time to create our happy little calendar function.
def create_calendar(year, month):
    # The calendar.month() function does all the heavy lifting for us.
    # It takes a year and a month, then returns a multi-line string with the calendar for that month.
    # Remember Bob Ross's wise words - "We don't make mistakes, just happy little accidents."
    # So, let's be positive and hope the user enters the input correctly.
    return calendar.month(year, month)

# We need to take input from users. This block will run when the file is invoked from the command line.
if __name__ == "__main__":
    # Here, we are taking year and month inputs from our user.
    # We'll try to convert them to integers. If they can't be, Python will raise a ValueError.
    # Don't forget, we're anticipating happy little accidents! 
    try:
        year = int(input("Please enter a year (like 1996): "))
        month = int(input("Please enter a month (like 5 for May): "))
    except ValueError:
        print("Oops! Looks like you didn't enter a valid year or month. Try again.")
    else:
        # If inputs are good, we'll create their calendar and print it. Joy of painting? More like joy of calendars!
        print(create_calendar(year, month))

# That's the end of our happy little script! Remember, "you can do anything you want to do. This is your world."
# Happy coding!

