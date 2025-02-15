
# Hello there, fellow coder! Today we embark on a fun journey of creating a VowelCount script. 
# Oh boy, isn't it going to be fun!

# Python, in its beauty, allows us to accomplish this task without any external libraries!
# So, let's buckle up and get started.

def count_vowels(input_string):
    """
    This whizbang function takes an input string and counts the occurrence of each vowel! 
    """
    # These are our freeze pops (also known as vowels)! 
    vowels = "aeiou"

    # Cool tool known as a dictionary to keep count of each vowel.
    vowel_count = {}.fromkeys(vowels, 0)

    # Let's convert our input string into lower case, because we don't discriminate between upper and lower case!
    input_string = input_string.lower()

    # Time for some magic! We count each vowel and update our dictionary! Abracadabra!
    for char in input_string:
        if char in vowels:
            vowel_count[char] += 1

    # Woohoo! We are done! We return our magic dictionary!
    return vowel_count


# Let's get the party started!
if __name__ == "__main__":
    # We ask our lovely user for an input string.
    string = input("Please enter a string: ")

    # We feed the string into our magic function and voila! We get the count of each vowel!
    result = count_vowels(string)

    # Let's showcase our magic trick to the user!
    for vowel in result:
        print("The count of {} in the input string is: {}".format(vowel, result[vowel]))

# Oh ho! What a journey it was! We successfully created a VowelCount script! We are off to party now! :D 

