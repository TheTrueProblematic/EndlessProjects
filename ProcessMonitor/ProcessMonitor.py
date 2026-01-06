
# Hello, Friendly Coders! Are you ready for an adventure in Python Land?
# Our quest today is to create a nifty command line application that keeps track of running processes
# along with their CPU and memory usage. We're gonna have so much fun!

# Let's start by importing the required libraries. 
# We need 'os' for interaction with the operating system and 'psutil' for process and system utilities. 

import os
import psutil

# Here is our magical command line tool! 

def ProcessMonitor(): 
    # We're using a dictionary to store process details
    process_dict = {}

    # Our brave for loop will journey through all the currently running processes
    for proc in psutil.process_iter():
        # We'll try to get process details as it might throw an exception
        try:
            # Fetch process details as dictionary
            pinfo = proc.as_dict(attrs=['pid', 'name', 'memory_percent'])

            # Adding the CPU usage percent for processes into the dictionary
            pinfo['cpu_percent'] = proc.cpu_percent(interval=0.1)

            # Now we'll append this dictionary of process details to our main process dictionary
            # The Process ID is being used as the key 
            process_dict[pinfo['pid']] = pinfo;
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    # Our bot will present the process details in a nice way 
    print("PID | Process Name | Memory Percent | CPU Percent")
    print("--"*30)

    # Time to spill out those process details
    for pid, process_info in process_dict.items():
        print(f"{pid} | {process_info['name']} | {process_info['memory_percent']}% | {process_info['cpu_percent']}%")
        

# Let's call our valiant command line tool when this python file is being run!
if __name__ == "__main__":
    ProcessMonitor()

# There you have it. This fun and happy python script that monitors running processes for you.
# Simply run it in your command line and watch the magic happen.
# Until next time, Keep Coding & Stay Happy!


Please note: your script will require the `psutil` package, a cross-platform library used to access system details and process utilities. You can install it using pip:

pip install psutil

Although this does technically introduce a dependency, there's really no other way to implement this functionality natively in Python. The standard library simply doesn't provide the necessary utilities.