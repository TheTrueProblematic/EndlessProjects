
# -*- coding: utf-8 -*-

# Hello, fellow Python enthusiasts! Today, we're going to have fun generating the famous Perrin Sequence. 🐍
# This tiny Python script that can toy around with a mathematical object that is the Perrin sequence!
# Isn't that super cool? 🚀 

# So, let's dive right in!

# First, let's define our function to create a Perrin Sequence. 

def generate_perrin_sequence(n):
    """
    This function generates the first N terms of the Perrin sequence.

    Args:
        n (int): The number of terms to generate.

    Returns:
        list: The first N terms of the Perrin sequence.
    """
    # Now, the Perrin sequence starts with 3, 0, 2. So let's initialize our sequence with these values.
    p = [3, 0, 2]

    # For the rest of the terms, each term is the sum of the two terms two places before it
    # and the term three places before it. How exciting is that? 🐘

    # Quick check: do our Python friends want more than three terms? If not, let's just serve them right away!
    if n <= 3:
        return p[:n]

    # Otherwise, let's use a loop to fill up our sequence.
    for i in range(3, n):
        p.append(p[i - 2] + p[i - 3])  # Each term is the sum of the two terms two places before it and the term three places before it.

    # And voila! We have our Perrin sequence! 🎉
    return p


# That's it! We've got a function to generate a Perrin sequence!
# Now, Python script is ready to rock and roll from the CLI.
# Let's put it to the test by printing out some terms of the Perrin sequence.

if __name__ == "__main__":
    N = int(input('Enter the number of terms: '))
    print(generate_perrin_sequence(N))

# Thanks for spinning through this code with me and I hope you found it fun and informative!
# Keep on Python-ing! 🐍💻🚀

