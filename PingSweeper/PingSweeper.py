
# Importing os and platform for running the ping command and checking which host system we're on
import os
import platform

# Put on your seatbelt kids, this programming adventure is just starting.
# First, we create our function named 'ping'. This little buddy is our magic spell for pinging the IPs.
def ping(host):
    """Pings a host and returns a boolean value representing if the host responded."""
    
    # Let's first figure out who we're dealing with today
    # Is it Windows, Linux, macOS or someone else?
    platform_name = platform.platform().lower()

    # Oh, it's Windows? Cool. Let's perform the ping spell in his language
    if "windows" in platform_name:
        response = os.system(f"ping -n 1 -w 2 {host} > NUL")
    # Oh, it's a Unix-based system? Nice. Let's perform the ping spell in their language
    else:
        response = os.system(f"ping -c 1 -W 2 {host} > /dev/null 2>&1")

    # If response equals to 0, it means our spell worked and the host is up and alive!
    return True if response == 0 else False


if __name__ == "__main__":
    # Looks like we're starting the adventure. Hold on tight!

    # Let's specify our IP range. For example, "192.168.1.0" to "192.168.1.255"
    ip_range = ["192.168.1." + str(i) for i in range(0, 256)]

    # Magic begins here. Let's iterate through each IP in our IP range.
    for ip in ip_range:
        
        # Ping the IP and store the result
        result = ping(ip)

        # Let's print an adorable message for each IP
        if result:
            print(f"Hoory! {ip} is up and alive!")
        else:
            print(f"Oh no! {ip} is sleeping right now.")

    # Wow, this was one heck of a journey! Hope you had fun.

