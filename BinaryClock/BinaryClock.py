
# BinaryClock.py
# Yay! Let's have some fun with binary representation of time!
# This script will display the current time in binary. 

# Import the necessary python library.
# One blessing of python is that it comes with built-in libraries 
# that pretty much lets you do all you want without accessing the internet or installing other libraries.
import time

# Function to convert time instances to binary
# Cheer up, this is the heart of our program!
def binary_time():
    # get the current time
    current_time = time.localtime()
    hours = current_time.tm_hour
    minutes = current_time.tm_min
    seconds = current_time.tm_sec
    
    # convert time to binary
    # don't worry, it's not that hard!
    binary_hours = format(hours, '06b')
    binary_minutes = format(minutes, '06b')
    binary_seconds = format(seconds, '06b')
    
    # return the binary time
    return binary_hours, binary_minutes, binary_seconds

# main function to tie up everything beautifully
# can't wait to see the outcome!
def main():
    while True:
        binary_hours, binary_minutes, binary_seconds = binary_time()
        
        # let's print the time in our super cool binary format, shall we?
        print(f'Current Binary Time: {binary_hours}:{binary_minutes}:{binary_seconds}')
        
        # print the time in binary every second
        time.sleep(1)

# call our main function
# off we go!
if __name__ == "__main__":
    main()

