
# Hey there! I'm so glad you're checking out my fun, little program.
# It's going to help you make sure your passwords are actually, y'know, secure.
# Let's get the party started! 💃🕺

# Not to overwhelm you, but we're importing the string library here.
# It's just for all the boring ASCII characters we're going to go through later. Yawn!
import string

# Now, onto the fun part!

# Let's start by defining how strong a password should be.
# It needs to be just the right amount of spicy. Not too hot, not too mild!
def check_password_strength(password):

    # Conditions, conditions, conditions!
    # We've got some standards, y'know. Just because it's a party, doesn't mean it's not a classy one.
    # True means it's GOOD, False means... well, False means you should try again. Fingers crossed!
    length = False
    digit = False
    symbol = False
    upper = False
    lower = False

    # First up, let's look at the length of the password.
    # It's gotta be just right. Goldilocks style. Not too short, not too long, just right.
    if len(password) >= 8:
        length = True

    # A password without a digit? Psh, that won't pass our superior standards.
    for letter in password:
        if letter.isdigit():
            digit = True

    # We love variety too! A good mix of upper and lower case letters are ideal.
    for letter in password:
        if letter.isupper():
            upper = True
        if letter.islower():
            lower = True

    # Symbol, darling! Because we love some drama and style 😏
    for letter in password:
        if letter in string.punctuation:
            symbol = True

    # Phew! That was quite a ride, wasn't it? Now, let's see if your password meets our high quality standards. Good luck!
    if length and digit and symbol and upper and lower:
        print("That password is a high security vault! Nice job.👍")
    else:
        print("Let's try again. That password could use some work.💪")

# Time to wrap up this party!
# You've been a blast, and we can't wait to see you become a password strength master.
if __name__ == "__main__":
    password = input("Enter your password: ")
    check_password_strength(password)

