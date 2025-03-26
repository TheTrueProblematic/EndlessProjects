
# Hey there, Python adventurers! Welcome on board to a fun-filled amusement park ride!
# I'd like you to buckle up as we take a headlong dive into simulating random dice rolls and printing a histogram of the results!

# But first, allow me to introduce you to our in-house power tool - the 'random' library. 
# This is the magic wand that will conjure up our random dice roll numbers!
import random

# First up, let's define our dice-rolling capacity.
# Y'know, just how in video-games, you punch the air a few times to warm up? 
# That's exactly what we're doing here. ;)
def roll_dice():
    return random.randint(1,6)

# Our magical journey ahead involves a thousand dice rolls.
# We're gonna roll 'em, again and again, till we get to the golden number of 1000.
# Strap in tight and let the journey begin!
def thousand_dice_rolls():
    return [roll_dice() for _ in range(1000)] 

# Now that we've stoked up a storm, let's take a step back and capture our flurry into six distinct bins.
# Picture this: Six crates all lined up, waiting to catch your dice rolls, right from 1 to 6!
def build_histogram(roll_results):
    return {i: roll_results.count(i) for i in range(1, 7)}

# In the quiet aftermath of our dice-storm, let's organize our captures from the six crates and lay them out in a neat, tidy histogram.
def display_histogram(histogram):
    for k, v in histogram.items():
        print(f"{k}: {'#' * v}")

# And now, for the grand finale!
# We'll chain all our circus acts together to give you an eye-popping, jaw-dropping spectacle!
def main():
    results = thousand_dice_rolls()
    histogram = build_histogram(results)
    display_histogram(histogram)

# Show's over folks! You can unbuckle your seatbelts now. 
# But remember, the park is open 24x7 for adventurers seeking thrills! So, see ya soon!
if __name__ == "__main__":
    main()
