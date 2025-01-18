
# Hey there, future coders! Let's have some fun with time conversion today. 
# Welcome to "Time24To12", a simple Python tool that transforms time from 24-hour format to 12-hour format.

def convert_to_12hr_format(time_24): # This function takes in a string representation of a 24-hour time
    """Convert a given 24-hour time in 'HH:MM' format to a 12-hour format with am/pm indications."""
    
    # Here, we start by splitting the input string into hours and minutes using a colon as the delimiter.
    hours, minutes = map(int, time_24.split(':'))
    
    # Checking if the hours are greater than 12. If so, subtract 12 from the hours and tag "pm".
    if hours > 12:
        return f"{hours-12}:{minutes:02d} pm"
    
    # If hours are equal to 12 (noon), no change needed, just tag "pm". 
    elif hours == 12:
        return f"{hours}:{minutes:02d} pm"
    
    # If hours are equal to 0 (midnight). Convert it to 12 and tag "am".
    elif hours == 0:
        return f"{12}:{minutes:02d} am"
        
    # If none of the above conditions meet, that means the time is morning, so just tag "am".
    else:
        return f"{hours}:{minutes:02d} am"
        
# Okay folks, that's all! Now you can convert from 24-hour format to 12-hour format like a breeze.

# And how about testing this function? Let's give it a try!
if __name__ == "__main__":
    test_times = ["00:00", "12:00", "17:30", "23:59", "07:20", "12:30"]
    
    for test in test_times: # Loop through the test times
        print(f"24-hour format time: {test} --> 12-hour format: {convert_to_12hr_format(test)}") 

# Oh, don't forget: this script should be run from the command line. So, fire up your terminal and give it a go! 
# Enjoy and have a tremendous amount of fun!!

