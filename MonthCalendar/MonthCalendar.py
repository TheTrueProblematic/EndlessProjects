
# Hello, dear adventurous coders! Today, we are going on a journey to create a super handy CLI MonthCalendar.
# With this script, we'll be able to display a simple month calendar for any given month and year, neat isn't it?
# Remember, no GUI or internet access, we are doing it the old school way! Time to dive in!

# We're going to use only the built-in python modules (to respect the no-dependencies rule)
import calendar

# We are using Python's built-in calendar module, because it's too cool and makes our job way easier!

def print_month_calendar(year, month):
    # Time to roll up our sleeves to print our sweet calendar!
    # the Python's Calendar module asks weekday of first day of the week (0 is Monday, 6 is Sunday)
    # You can set it to 6 (for Sunday) if you wish, you're the boss! Here as per international standard, Monday is the first day of the week.
    my_calendar = calendar.TextCalendar(firstweekday=0)

    # Let's print out the calendar using prmonth() method because it's super useful and it does what we need.
    # It takes in a year and month parameters, and voila, we get a formatted text calendar!
    my_calendar.prmonth(year, month)


# Let's say we are calling this function with year as 2023 and month as 12 (December)
print_month_calendar(2023, 12)

# And that's a wrap! We now have a simple, yet stylish command line calendar for any given month and year. Hope you had as much fun coding this, as much as I did.

Output:
shell
   December 2023
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31
