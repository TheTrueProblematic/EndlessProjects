
# Hey there, happy programmer! Let's go on a magical journey...
# This super cool python script generates random subsets from a given set! Spooky, right? 

# Since we're all about being self-reliant, this script doesn't need any dependencies or internet access. Just raw, unadulterated python powers.

# Let's import the random module. Don't worry, it's included in a fresh install of python on any platform.
import random

# Now to the juicy part! Let's define our function, random_subset!
def random_subset(given_set):
    # We'll start by making a copy of our given set. We don't want to mess with the original, right?
    set_copy = given_set.copy()
    
    # Now, let's decide how big our subset is going to be. It could even be the whole set or an empty set!
    subset_size = random.randint(0, len(set_copy))

    # And here's where the real magic happens. We'll use an advanced dark arts technique called "list comprehension"
    # to randomly pick elements from our set copy, creating our very own random subset!
    result = [set_copy.pop(random.randint(0, len(set_copy) - 1)) for _ in range(subset_size)]
    
    # Ta-da! We return our beautiful, unique snowflake of a subset.
    return result

# And that's it! A pretty simple little script, but one that does the job all on its own, like a hermit in the wilderness.
# Now you can use this to generate random subsets of any set you toss its way! Like a hungry, hungry hippo but for sets.
# Go forth and generate those subsets!

# Testing the function using command line args would be more fun, but for now, let's just use a static example.
if __name__ == '__main__':
    example_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    print(random_subset(example_set))
