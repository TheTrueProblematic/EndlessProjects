
# Howdy! Here we're gonna calculate the Hamming Distance between two strings
# What's Hamming Distance you ask? well, simply put, it's the number
# of positions at which the corresponding symbols are different
# in our two input strings. 

# So if we're given two strings of equal length, say "karaoke" and "karaage"
# our job is to find the number of positions where they differ.
# In this case, that would be 2 (positions 3 and 4: 'o' vs. 'a', 'k' vs. 'a')

# So how are we gonna do this? Python, of course! All with simple and clean code!
# Let's dive in!

def hamming_distance(string1, string2):
    # The strings, they must be of equal length
    # If not, our little bot will show some attitude!
    if len(string1) != len(string2):
        return "Oh dear! Strings must be of equal length :)"

    # Hamming Distance starts at zero by default
    distance = 0

    # Now we scan both strings at the same time
    for char1, char2 in zip(string1, string2):
        # if the characters don't match, we add 1 to the distance
        if char1 != char2:
            distance += 1

    # We now return the final Hamming Distance
    return distance

# All righty, let's test out this pony!
if __name__ == "__main__":
    # Let's enter the two strings
    print('Please provide the first string:')
    string1 = input()
    
    print('Please provide the second string:')
    string2 = input()
    
    # Let's go, calculate the Hamming Distance!
    print("Calculating Hamming Distance... Yeehaw!")
    result = hamming_distance(string1, string2)
                
    print(f"The Hamming Distance is: {result}")

# Well, this was a fun ride and hope you enjoyed!
# This program will take two strings and calculate the Hamming distance for you
# No API access, no internet access, just pure Python
# So go wild, and calculate some Hamming Distances!
