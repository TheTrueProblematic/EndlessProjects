
# Welcome to NetworkSpeedTest.py! Let's turn on the engineer's passion!
# This script provides a simple way to perform download/upload speed tests using local sockets. 

# This will be a CLI-based script since we love terminals, no GUIs messing around here!
# Also, we'll stick to the purest python, no external libraries, 
# making our lovely script portable across fresh python installations, isn't it amazing?

# One more thing! We respect privacy so no need to worry! No internet access, no APIs at all.

# Now, let's dive into the real thing!

import time # time is all we need here!
import socket # of course we need sockets for our tests!
import threading # got to make it snappy!

# Okay, let's define how much data we'll send in each test. I'm gonna go with 1024 bytes.
# Feel free to change it. But remember: by increasing it the test will take longer (but may be more accurate)!
DATA_AMOUNT = 1024

# Let's define the port we'll be using. I like 5000. It's a nice round number.
PORT = 5000

# Now the magic begins. Let's start with the download speed test.
def download_test():

    # Welcome to the server side of the test. Make yourself at home!
    def server_side():
        # First we'll create a socket. 
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            # Now we bind it to any IP at our chosen port.
            server.bind(('0.0.0.0', PORT))
            # Now we make our server start listening for connections.
            server.listen(1)
            # When a connection is detected, we'll get the client socket and address.
            client_socket, _ = server.accept()

            # Now we send our data!
            client_socket.sendall(b'0' * DATA_AMOUNT)
        finally:
            # Always clean up after yourself, we'll close our server socket when we're all done.
            server.close()

    # Alright, time to start the test!
    # We start the server side in a thread.
    thread = threading.Thread(target=server_side)
    thread.start()

    # Now we'll create a socket for the client side.
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # We then connect to our own IP at the chosen port.
    client.connect(('localhost', PORT))
    received_data = b''
    # We then start a timer. Race against time!
    start = time.time()
    while len(received_data) < DATA_AMOUNT:
        received_data += client.recv(1024) # receive 1024 bytes each time
    finish = time.time() # time's up!

    # Close the client socket. Keeping the environment clean.
    client.close()

    # Let's calculate how much data we received per second.
    speed = DATA_AMOUNT / (finish - start) # bytes/second
    return speed * 8 / 1024 / 1024 # return speed in megabits per second

# Let's do the same thing for the upload speed test.
# It's like looking at our download test through a mirror!
def upload_test():

    # Now we are on the client side, sending data home!
    def client_side():
        # Creating a client socket.
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            # Connect to our server
            client.connect(('localhost', PORT))
            # Start timer
            start = time.time()
            # Send data
            client.sendall(b'0' * DATA_AMOUNT)
            finish = time.time() # time's up!
        finally:
            # We close the client socket.
            client.close()

        # Same calculations here to get the upload speed!
        speed = DATA_AMOUNT / (finish - start) # bytes/second
        return speed * 8 / 1024 / 1024 # return speed in megabits per second

    # Do you remember our download test's server side? Here is its twin brother!
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', PORT))
    server.listen(1)
    _ = server.accept()
    server.close()

    # We do the same thing here, starting the client side in a thread.
    thread = threading.Thread(target=client_side)
    thread.start() 
    thread.join()

    return client_side() 

# Alright, let's run the test. Print the results. And have a coffee!
print(f'Download speed: {download_test()} Mbit/s')
print(f'Upload speed: {upload_test()} Mbit/s')

# That's it, we have finished! 
# Hope you enjoyed this joyride through NetworkSpeedTest.py!


