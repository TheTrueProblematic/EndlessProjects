
# Hi there! Welcome to MinMaxTuples.py! 
# Today we're going on a fun journey to find the minimum and maximum values in a list of tuples.
# Despite being a technical task, adventure awaits!

# Importing built-in python module 'sys' for accessing system-specific parameters and functions
import sys

def main():
    # Fun stuff begins here! Now we're creating a list of tuples to work with!
    tuples_list = [(10, 20), (15, 35), (40, 50), (25, 45)]

    # Oh wow! Look at all those tuples! Now, sit back and hold your breath as we dive in to find the min and max.

    min_value, max_value = None, None

    # We're going for a ride through each tuple, hang on tight! 
    for tup in tuples_list:
        
        # Exploring each value in the tuple, never know where the adventure leads!
        for val in tup:

            # Shh! Be quiet as we discover a new minimum value!
            if min_value is None or val < min_value: 
                min_value = val 

            # Look out! Here comes a new maximum value! 
            if max_value is None or val > max_value: 
                max_value = val

    # Wow! You made it! After all that adventuring, here are the min and max values you helped discover!
    print("Minimum Value:", min_value)
    print("Maximum Value:", max_value)

if __name__ == "__main__":
    # Its time to start the adventure! 
    # The main() function is the portal to our journey! Let's dive in!
    main()


