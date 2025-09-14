
# Howdy folks! Welcome to our little project: Implementing the Rail Fence Cipher encoder and decoder!
# This is going to be a fun ride! Let's get started.

# First off, we know that we need to create an encode and decode function for our Rail Fence Cipher. Crazy times, right?

def encode_rail_fence_cipher(string, num_rails):
    # In our rail fence cipher, imagine having num_rails rail tracks.
    # We zigzag our characters along these tracks as we encode our string. Like a wild rollercoaster ride!

    # Prepare our rail tracks!
    rails = [[] for _ in range(num_rails)]

    # This will determine if we're currently moving "down" or "up" the rails.
    rail_direction_down = True

    # This is the rail we're currently writing to.
    current_rail = 0

    # Encoding starts here!
    for char in string:
        # Add our character to the current rail.
        rails[current_rail].append(char)

        # Determine if we need to change direction at the edges.
        if current_rail == 0:
            rail_direction_down = True
        elif current_rail == num_rails - 1:
            rail_direction_down = False

        # Change our rail accordingly.
        current_rail += 1 if rail_direction_down else -1

    # Once we're done zigzagging along the rail tracks, we're going to consolidate them into a single string. Buckle up!
    encoded_string = ''
    for rail in rails:
        for char in rail:
            encoded_string += char

    # And voila, we have our encoded string! Wasn't that a wild ride?
    return encoded_string


def decode_rail_fence_cipher(string, num_rails):
    # Decoding is a bit like riding the rollercoaster in reverse. Just as exhilarating!

    # Set up some basic data about our rails and characters.
    rail_lengths = [0] * num_rails
    rail_direction_down = True
    current_rail = 0

    # Let's find out how many characters will be in each rail.
    for _ in string:
        rail_lengths[current_rail] += 1
        if current_rail == 0:
            rail_direction_down = True
        elif current_rail == num_rails - 1:
            rail_direction_down = False

        current_rail += 1 if rail_direction_down else -1

    # Time to populate those rails with our actual characters.
    rails = []
    i = 0
    for length in rail_lengths:
        rails.append(list(string[i:i+length]))
        i += length

    # Finally, we zigzag back and forth, grabbing characters from each rail to recreate our original string.
    rail_direction_down = True
    current_rail = 0
    decoded_string = ''
    while len(decoded_string) < len(string):
        decoded_string += rails[current_rail].pop(0)
        if current_rail == 0:
            rail_direction_down = True
        elif current_rail == num_rails - 1:
            rail_direction_down = False

        current_rail += 1 if rail_direction_down else -1

    # Just like magic, there's our original string!
    return decoded_string

# Wasn't that quite the rollercoaster ride? But we successfully implemented the Rail Fence Cipher encoder and decoder!
# Without using any external libraries, and without accessing the internet! Those are some Python magic tricks to show off at parties!
