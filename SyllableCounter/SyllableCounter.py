
# Hey there fellow programmer!
# I'm thrilled to present you with our SyllableCounter program. Pretty catchy right?

# Importing the mighty Regular Expression library from python standard libraries.
import re

# The enthusiastic main function where the excitement begins!
def main():
    word = input("Enter a word to count its syllables: ") # Prompting the user to enter the word.
    print("Approximate Syllable count is:", syllable_count(word)) # Displaying the word along with its syllable count.

# The precise function to count the syllables.
def syllable_count(word):
    # Word goes into lower case
    word = word.lower()
  
    # timeless "aeiouy" check
    count = len(re.findall("[aeiouy]+", word))
  
    # This tricky one-liner finds all the syllables in each word.
    # Here's how it works:
    # '[aeiouy]+' finds sequences of vowel characters (our syllables).
    # By adding '+' at the end, we're capturing multiple vowel sequences in one go.
    # This is because we know words can have multiple syllables, and each syllable is essentially a vowel sequence.
    #
    # For instance:
    # 'sleep' has one continuous vowel sequence 'ee', thus it is one syllable.
    # 'hello' has two separate vowel sequences 'e' and 'o', hence two syllables.
    
    # subtract one syllable for words ending in 'e' or 'es' except for those ending in 'le'
    ends_in_e = len(re.findall("[^l]e$", word))
    count -= ends_in_e
  
    # Accounting for cases where 'e' or 'es' comes at the end of the word. 
    # Most of the times, they don't add to the syllable count unless the word ends with 'le'.
    # So we subtract those silent 'e's from our count.
    #
    # For instance: 'apple' and 'orange' both earns one syllable from their ending 'e'.
    # But 'make', 'nuke', they don't get that. Their 'e' is silent.
  
    # always give one syllable for words < 3 (like 'I', 'a')
    if len(word) < 3:
        count = max(count, 1)

    # Our final protective move. 
    # We make sure that no words end up having zero syllables.
    # This is kind of a catch-all to cover small words, like 'I' and 'a'. 
    return count # Returning the final count.
  
# Here we are invoking our main function to take the user on this syllable counting journey!
if __name__ == "__main__":
    main()

# And that's it! 
# I hope you enjoy tinkering with this tiny utility as much as I enjoyed writing it.
# Keep on coding and stay awesome!

