Python
# Hello World! I hope you're in a good mood. We are going to have fun detecting Haikus!
import re

# Handy dandy function to count syllables in a word. I know right!
def count_syllables(word):
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    # if the first letter is a vowel
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index-1] not in vowels:
            # for each vowel get a point
            count += 1
    if word.endswith("e"):
        count -= 1
    if word.endswith("le") and len(word) > 2 and word[-3] not in vowels:
        count += 1
    if count == 0:
        count += 1
    return count

# This function will divide the text into lines and check if it conforms to the 5-7-5 syllable structure
def is_haiku(text):
    lines = text.split('\n')
    if len(lines) != 3:
        return False
    line_syllable_counts = [5, 7, 5]
    for i in range(3):
        words = re.split(r'[ \t]+', lines[i])
        syllable_count = sum(count_syllables(word) for word in words)
        if syllable_count != line_syllable_counts[i]:
            return False
    return True

# Oh... Look! Our main function is here!
def main():
    print("Welcome to Haiku Detector! Insert your text:")
    text = input()
    if is_haiku(text):
        print("This is a Haiku! Outstanding!!!")
    else:
        print("This is not a Haiku! Better luck next time...")

# Time to run our main function. Hold on tight!
if __name__ == '__main__':
    main()

