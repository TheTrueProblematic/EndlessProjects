
# KMPStringSearch.py
# Yay! We're going to implement the legendary Knuth-Morris-Pratt (KMP) algorithm in this awesome python file!
# KMP is a clever algorithm for searching a substring in a text in linear time, and who doesn't love efficiency?
# Alright, let's start coding!

def compute_kmp_table(pattern):
    """Compute the KMP table (also known as 'failure function')"""
    # We start by initializing the table with zeroes
    kmp_table = [0]*len(pattern)
    # Let's keep track of the length of the longest prefix suffix!
    len_longest_prefix_suffix = 0
    # The loop starts from index 1, since the value at index 0 is always zero
    i = 1
    while i < len(pattern):
        # This is where the magic of KMP starts. We check if the character matches the length of longest prefix suffix
        if pattern[i] == pattern[len_longest_prefix_suffix]:
            # If so, we increment the length of longest prefix suffix and save it in the kmp_table at current index
            len_longest_prefix_suffix += 1
            kmp_table[i] = len_longest_prefix_suffix
            i += 1
        else:
            # If the current character doesn't match, but length of longest prefix suffix is greater than zero
            if len_longest_prefix_suffix != 0:
                # Go to the 'previous' longest prefix suffix length
                len_longest_prefix_suffix = kmp_table[len_longest_prefix_suffix-1]
            else:
                # If there aren't any matching characters, we set kmp_table[i] to zero and increment the current index
                kmp_table[i] = 0
                i += 1
    # voila! We have computed the kmp_table
    return kmp_table

def kmp_string_search(pattern, text):
    """Knuth-Morris-Pratt string search algorithm"""
    # Let's compute the KMP table for our pattern
    kmp_table = compute_kmp_table(pattern)
    # Initialize the indicies for pattern and text, let the search begin!
    i = j = 0
    # While there's text left, keep searching
    while i < len(text):
        # If the current characters of pattern and text match
        if pattern[j] == text[i]:
            # Yeah, they matched, let's increment both pointers
            i += 1
            j += 1
            # So, if we have matched the entire pattern, then it means we have found it in the text!
            if j == len(pattern):
                return (i - j)
                # Yeppie! We've got a match! Let's start searching again from the 'next' longest prefix suffix length
                j = kmp_table[j-1]
        # If the characters don't match
        else:
            # If we haven't started matching the pattern, we simply move to the next character in the text
            if j == 0:
                i += 1
            # If we had started matching, we need to use our trusty kmp_table to move to the 'next' longest prefix suffix length
            else:
                j = kmp_table[j-1]
    # Oh no, we didn't find the pattern in the text :(
    return -1

# Alright! We've implemented the KMP algorithm, wasn't it a fun ride?
# Now you can use this file to efficiently search for patterns in text from the command line. Enjoy!
