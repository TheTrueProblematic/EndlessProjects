
# Hey there, happy coder! This cheerful little python script is here to help you figure out the day of the week for any given date.
# Isn't that a fun little trick? And the best part? It's all done without any external dependencies, internet access or any of that pesky cli.
# Whether you're just having fun with dates, or need to know if you were born on a Monday (spoiler: it doesn't really matter), this script is for you. Enjoy!

# Let's start by importing the 'datetime' module built-in python
import datetime

# Define function to get date from user and return respective day
def day_of_week():
    # Greet the user in a friendly way
    print("Hey there! Let's find out what the day of the week a certain date was!")
    
    # Ask for the date input in the format YYYY/MM/DD
    date_input = input("Please, enter a date in the format 'YYYY/MM/DD': ")
    
    # Try to convert the string to a date object
    try:
        # This line will try to convert the string into a date,
        # using the provided format. If it can't, it will throw an error
        # and take us straight to the 'except' block
        date = datetime.datetime.strptime(date_input, "%Y/%m/%d")
        
        # If we made it this far without an error, let's find out the day of the week for this date!
        # and display it to the user
        print("The date provided is a lovely "+date.strftime("%A")+"!")

    except ValueError:
        # This block will run if the user's date input was incorrect.
        # We just tell the user what went wrong and give them another shot
        print("Oops! Your date input wasn't recognized. Make sure it is in the format 'YYYY/MM/DD'. Let's try again!")
        day_of_week()

# Kick off the script by calling our function!
if __name__ == "__main__":
    day_of_week()
