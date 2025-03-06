
# Hiya, Pythonistas! Welcome to our fun little project 'LongestCommonPrefix'.
# The aim of this game? To find the longest common prefix string amongst an array of strings.
# Who doesn't love a good word puzzle, right?
# So without further ado, let’s get stringing!

# Oh, and don't worry: there's no GUI, no dependencies, and definitely no internet access required.
# Just you, me, and the cozy Python command line. Sweetness!

def longestCommonPrefix(strs):
    """
    Function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, the function returns an empty string "".
    """

    # Edge case check: If the array is empty, return an empty string
    if not strs: return ""

    # Let's select a "shortest string". By default, shortest string can be the first string in the array
    shortest_str = min(strs, key=len)

    # Now, we’re going to loop through this ‘shortest string’ character by character
    for i, character in enumerate(shortest_str):
        for other in strs:
            # If the character is not present in positions of other string exactly as in 'shortest_str', break the loop
            if other[i] != character:
                # So our common prefix is from start of 'shortest_str' to 'i'
                return shortest_str[:i]

    # If no mismatch was found, the 'shortest_str' is our common prefix 
    return shortest_str

# Testing time! Can our code solve the mystery of the common prefix? Drumroll, please...
print(longestCommonPrefix(["flower","flow","flight"]))  # It should return "fl"

# Hope you filled your pockets full of Python fun!
# Keep coding, stay awesome! Good luck with your next Python adventure!
