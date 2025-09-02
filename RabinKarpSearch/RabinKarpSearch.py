
# Hey there happy coders! Buckle up, because today, we're going to implement the Rabin-Karp string search algorithm.
# This is a super cool algorithm that finds a pattern in a text.
# The best part? It does it in linear time! How cool is that?!

def rabin_karp_search(pattern, text, prime):
    """
    This function creates 'hash_codes' for the 'pattern' and 'text',
    and compare these 'hash_codes' to see if the pattern exists in the text.
    """
    M = len(pattern)
    N = len(text)
    i = 0
    j = 0
    pattern_hash = 0    
    text_hash = 0    
    h = 1

    # The initial value of 'h' would be like 'pow(d, M-1)%q'
    for i in range(M - 1):
        h = (h * 256) % prime

    # Calcutate the hash value of pattern and first window of text
    for i in range(M):
        pattern_hash = (256 * pattern_hash + ord(pattern[i])) % prime
        text_hash = (256 * text_hash + ord(text[i])) % prime

    # Go through the rest windows of text
    for i in range(N - M + 1):
        # Check if hash values of current window of text and pattern are same
        if pattern_hash == text_hash:
            # Check for characters one by one
            for j in range(M):
                if text[i + j] != pattern[j]:
                    break

            j += 1
            # If all characters match, then pattern is found
            if j == M:
                print(f"Pattern found at index: {i}")

        # Calculate hash value for next window of text
        if i < N - M:
            text_hash = (256 * (text_hash - ord(text[i]) * h) + ord(text[i + M])) % prime
            # We might get negative values of 'text_hash', hence convert it to positive
            if text_hash < 0:
                text_hash += prime

# Here's a simple test to run our program
rabin_karp_search("test", "This is a test string for Rabin-Karp", 101)
# The pattern 'test' is found at index 10 of 'text'. Super cool!

# And that's it!!! A simple but elegant Rabin-Karp string search engine!
# Now, Go forth and code!
