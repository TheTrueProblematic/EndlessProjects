
# Hello! Welcome to my Z Algorithm Python script! It's pattern matching galore in here! 

# First things first, I'm going to define a special function for generating the Z array.
# We'll use this z array to find all occurrences of our pattern in a text.
def get_z_array(s):
    """Create Z array to use in Z algorithm."""
    # The Z array is actually quite neat!
    # It stores the length of the segment which is both prefix and suffix
    indices = len(s)
    z = [0] * indices
    # I love the left and right pointers, they help in avoiding unnecessary comparisons
    left, right = 0, 0

    for i in range(1, indices):
        # Don't you love it when you can use pre-computed data? It saves a lot of time!
        if i > right:
            left = right = i
            # A neat trick here is comparing characters until they don't match anymore
            while right < indices and s[right - left] == s[right]:
                right += 1
            z[i] = right - left
            right -= 1
        else:
            k = i - left
            # Woohoo! We saved a substring match! Using the earlier matched substring :D
            if z[k] < right - i + 1:
                z[i] = z[k]
            else:
                left = i
                while right < indices and s[right - left] == s[right]:
                    right += 1
                z[i] = right - left
                right -= 1

    return z  # As promised, the freshly baked Z array is ready! 



# Alright! Now, let's create a function to implement the Z algorithm.
# Our magical function will be responsible for pattern matching. It's where the real magic happens!
def search(text, pattern):
    """Implement Z Algorithm for pattern searching."""
    # Here, we concatenate pattern, separator, and text
    # Why? So that the pattern doesn't match the text within the separator itself
    concat = pattern + "$" + text
    # Getting Z array for the concatenated string
    z = get_z_array(concat)
    
    # Oh my! We found a match!
    for i in range(len(z)):
        if z[i] == len(pattern):
            # Hurray! Pattern found at index %d
            print(f'Pattern found at index {i - len(pattern) - 1}')


# And that's it, my friend! This is the end of the script. Quite neat, isn't it?
# Feel free to use it and let the power of pattern matching be with you!

