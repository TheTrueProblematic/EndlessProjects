
# Hello fellow Python enthusiasts! Let's dive into an exciting journey of Pythagorean triplets. Isn't that cool?
# We are going to generate Pythagorean triplets up to a certain limit. Fasten your seatbelt, it's going to be fun, Yay!

# First of all, let's import our speed booster, 'sys' module, for command-line arguments.
import sys

def generate_pythagorean_triplets(limit):
    """A function to generate Pythagorean triplets"""
    # This list will hold our discovered triplets.
    triplets = []
    
    # Triple for loop, sounds fun right? This will guarantee we check every possible triplet combination.
    for a in range(1, limit):
        for b in range(a, limit):
            for c in range(b, limit):
                # If the triplet is a Pythagorean triplet (a^2 + b^2 = c^2), add it to the list of triplets!
                if a*a + b*b == c*c:
                    triplets.append((a, b, c))

    # Return the list of triplets we discovered.
    return triplets
    

def main():
    """The main program"""
    # Let's take the limit from the command-line argument, sounds geeky right?
    if len(sys.argv) > 1:
        limit = int(sys.argv[1])
    else:
        # If no argument is provided, let's use a default value of 100, awesome!
        limit = 100

    # Now, let's generate those elusive Pythagorean triplets.
    print('Generating Pythagorean triplets up to {}'.format(limit))
    triplets = generate_pythagorean_triplets(limit)
    
    # Time to reveal the magic! Print out what we've discovered.
    for triplet in triplets:
        print('Found triplet: {}'.format(triplet))

    print('Exiting Program. Bye-bye!')

# Do not forget to call the main program, otherwise, nothing would work, Sssh! Don't tell anyone.
if __name__ == "__main__":
    main()

# Cool, isn't it? It's time to generate Pythagorean triplets and amaze everyone. You are a Python magician!

