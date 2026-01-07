
# Hey folks! This groovy little script is called PortScanner, it's simple but fierce
# kind of like a raccoon with a YouTube channel: unassuming, but powerful!
#
# This little script gives you ability to scan open ports on a local network address,
# Nifty, huh! And it does all of this right in the console - no fancy GUIs here, just the good ol' command line!
# It also doesn't need internet access or any APIs - like an old school rock band, it doesn't need any fancy tools to make magic.
#
# And the best part? It's all in one python file! So grab your favorite terminal, Let's dive in!

import socket  # Hey, we know this guy! Good ol' socket!

# Time for a little function action! This one is called port_scanner
# Its job is to check a specific port, and it needs an IP and a port to do its job
def port_scanner(ip, port):
    # We start off by making a socket object - think of it as our tool belt for this operation
    socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_obj.settimeout(5)  # Let's set a timeout so we're not waiting around all day

    # Now we're checking if we can connect to the IP address on a specific port
    # If we can't, we return False. If we can, we return True. Easy peasy!
    if socket_obj.connect_ex((ip, port)) != 0:
        return False
    else:
        return True

# Okay, time to get hands-on! We're asking the user to input an IP address and a port range
# So, if you really wanted to, you could check every single port! (Not recommended, takes a while)
ip = input("Enter the IP Address: ")  # Tell me the IP!
port_start = int(input("Enter the starting port: "))  # Where are we starting?
port_end = int(input("Enter the ending port: "))  # Where are we going to?

# Now for the fun part! We're looping over our port range
# And every time, we're calling our port_scanner. Will it return True? Will it be False? The excitement!
for port in range(port_start, port_end + 1):
    if port_scanner(ip, port):  # If it's True...
        print(f"Port {port} is open on {ip}")  # Give the good news!

# That's it! So go forth, and scan some ports. Who knows what you'll find?
# Just remember to use your powers for good. And keep rockin'! 🤘

