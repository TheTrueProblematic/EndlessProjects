
# RandomPasswordDiceware.py
# Hip hip hooray! We are making a password generator using the Diceware method!
# Diceware is an easy peasy lemon squeezy method for creating passwords.
# It uses a list of words, each given a unique five-digit number where each digit is between 1 and 6.
# A five-dice roll determines each word in the password.
# So let's roll (pun intended)!

import secrets
import os

# Just a small part of dice ware list in tuples
DICELIST = {
    "11111": "a", "11112": "a&p", "11113": "a's", "11114": "aa", "11115": "aaa", "11116": "aaaa", "11121": "aaron",
    "11122": "ab", "11123": "aba", "11124": "ababa", "11125": "aback", "11126": "abase", "11131": "abash", "11132": "abate",
    "11133": "abbas", "11134": "abbe", "11135": "abbey", "11136": "abbot", "11141": "abbott", "11142": "abc",
}

# Woohoo! Function time!
def diceware_password(num_of_words):
    """Takes an integer and returns a Diceware password with that many words."""

    # Let's make a list of passwords. Making lists is fun! Like shopping, but for security.
    password = []

    # For each word we need...
    for _ in range(num_of_words):
        # Now the magic happens! We generate a five-digit Diceware number...
        diceware_num = ''.join(str(secrets.randbelow(6) + 1) for _ in range(5))  # remember, each digit is from 1 to 6.

        # And grab the word that matches that number.
        password.append(DICELIST.get(diceware_num, ""))  # in case the random number is not in DICELIST, default to "".

    # Now let's join all our words together with a space. Spaces are friendly. They give words room to breathe.
    return ' '.join(password)

# Let's try it out! How about... 6 words?
if __name__ == '__main__':
    print(diceware_password(6))

# That’s all folks!
# Remember, password security is no laughing matter. Except when it's this easy. Then it's a little funny.

