# Let's put on our programming hats and dive into the fun world of Collatz sequences! 
# Remember, even the most complex problems are just simple problems in disguise.

def collatz_cycle_length(n):
    """
    This little gem calculates the cycle length of a number in a Collatz sequence.
    Simple and hypnotically mesmerizing.
    """
    # Our beautiful cycle length starts its life as a humble 1.
    length = 1
    while n != 1:
        # If n is even, we divide it by 2,
        if n % 2 == 0:
            n = n // 2
        # But oh! If n is odd, things get a bit spicy.
        # It gets multiplied by 3, and has 1 added.
        else:
            n = 3 * n + 1
        # And hey, let's not forget to increase our cycle length.
        length += 1
    return length

def collatz_within_range(start, end):
    """
    Accepts a range of numbers (start and end, inclusive) and 
    finds the number with the longest Collatz cycle within this range.
    And remember folks, it's not always about the destination,
    sometimes it's about the fun of the journey.
    """
    # Set the stage with a maximum cycle length of 0
    max_cycle_len = 0
    number_with_max_cycle = 0
    
    # And we're off! Watch as we gracefully run through our range of numbers.
    for i in range(start, end + 1):
        # Get the cycle length for the current number
        current_cycle_len = collatz_cycle_length(i)
        # Is this cycle length the longest we've seen yet?
        if current_cycle_len > max_cycle_len:
            # Well hot diggity dog, we have a new record!
            max_cycle_len = current_cycle_len
            number_with_max_cycle = i
            
    # Drumroll please... it's time to announce the number with the max cycle.
    return number_with_max_cycle, max_cycle_len

# And there you have it, folks! A simple little program, with a complex little job.
# Who knew math could be so entertaining?