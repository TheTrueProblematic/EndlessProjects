
# Hey, fellow coder! Welcome to this neat little Python project: our very own Alarm Clock in the CLI!
# Isn't it great when our code can wake us up on time, just like a cup of freshly brewed coffee? Let's dive right in!

# Here's what we'll need for this project: Python's built-in modules!
# - datetime for dealing with all things time-related.
# - winsound to play our alarm sound; it's as easy as pie on Windows.
import datetime
import winsound
import os

# Function to validate input time format
def validate_time(alarm_time):
    # We are considering the time in 24 hour format (HH:MM)
    if len(alarm_time) != 5:
        return False
    if int(alarm_time[0:2]) > 23:
        return False
    if int(alarm_time[3:5]) > 59:
        return False
    if int(alarm_time[2]) != ":":
        return False    
    return True

def set_alarm(alarm_time):
    # We'll print the time the user sets their alarm for.
    # It's always important to have feedback, even on the CLI!
    print(f"The alarm is set for {alarm_time}")

    while True:
        # The strftime function fetches the current time in the format we want
        current_time = datetime.datetime.now().strftime("%H:%M")

        # Check to see if it's the alarm time yet
        if current_time == alarm_time:
            print("Wake up! Your alarm is buzzing!")

            # This is where the magic happens! We're using the built-in winsound module to play this built-in Windows sound.
            # For non-Windows systems, you can use os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
            winsound.Beep(2500, 1000) 
            break
    
def main():
    print("Welcome to our CLI Alarm Clock!")

    # Let's get the input from the user. It's their alarm, after all!
    alarm_time = input("Enter the alarm time in format 'HH:MM' :")

    # We'll validate the time input. Always sanitize your inputs!
    if not validate_time(alarm_time):
        print("Invalid time format, please try again with format 'HH:MM'")
    else:
        # Now, we'll set the alarm with the input that we've just received
        set_alarm(alarm_time)
        
# Let's kick off this party!
if __name__ == '__main__':
    main()
  
