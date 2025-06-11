
# Say hello to TimeZoneConverter! This smart little python script is going to help you convert time from one timezone to another.
# Isn't it fun to journey across time zones without leaving your comfy chair? Let's do this!

# First things first! We have to import datetime and pytz. These packages give us all the tools that we need to manipulate date and times.
# Remember, time travel is nothing for the faint of heart.
import datetime
import pytz

def convert_time_zone(time, current_tz, target_tz):
    """ Function to convert a datetime from one timezone to another.
    
    Args:
        time (datetime): A date time string in the format %Y-%m-%d %H:%M:%S
        current_tz (str): Current timezone of 'time'.
        target_tz (str): Target timezone to which 'time' is to be converted.

    Returns:
        datetime: 'time' converted into target_tz.
    """
    # We first convert the string to a datetime object and set its timezone as the current timezone.
    current_time = datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
    current_time = pytz.timezone(current_tz).localize(current_time)

    # Then we convert this datetime object into the target timezone. 
    # Ah! The sweet taste of success when we see our time in a new timezone.
    target_time = current_time.astimezone(pytz.timezone(target_tz))

    # Just a little print function to bid goodbye. After all, we are polite time travelers.
    print("The time in {} is {}".format(target_tz, target_time.strftime("%Y-%m-%d %H:%M:%S")))


if __name__ == "__main__":
    #To run the script input your time, initial timezone and the target timezone
    #It should look something along the lines convert_time_zone('2022-02-21 12:00:00', 'US/Eastern', 'Europe/London')
    #See you in another timezone!
    pass
