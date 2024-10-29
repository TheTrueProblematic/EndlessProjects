
# Hey there, happy programmer!
# Time to play detective with a python script! Our mission? Validate a password!
# Isn't that just exciting?

def validate_password(password):
    # So we have a few rules for our passwords, right?
    # Can't be too easy or our system might explode! Or worse, some naughty hacker might get in.
    
    # Rule 1: Length; because size DOES matter. 
    # Jokes aside, short passwords are just too easy to guess!
    if len(password) < 8:
        return False     # See what I did there? Elegant yet graceful. Also, no go if password is short!
    
    # Rule 2: Numbers, because who doesn't love a good mathematical cat and mouse chase?
    if not any(ch.isdigit() for ch in password):
        return False     # No number, no pass. Bummer.

    # Rule 3: Uppercase letters. A little caps lock never hurt anyone, right?
    if not any(ch.isupper() for ch in password):
        return False     # Unfortunate, but necessary. Just how the cookie crumbles.
        
    # Rule 4: Lowercase letters, because we're not yelling here!
    if not any(ch.islower() for ch in password):
        return False     # Devastating, but we can't have passwords screaming at us in all caps all day.
    
    # Rule 5: Non-alphanumeric characters. Aka the wildcard of our little game.
    #         It could be anything! That's what makes it so exciting!
    # And yes, we could've used a regex for all of this, but we're trying to keep things manageable, remember?
    if not any(not ch.isalnum() for ch in password):
        return False     # If no wildcard is present, we fold our hand. 
    
    # If we've passed all these checks, we're genius-level password creators!
    # Time to celebrate in true programmer fashion: with a lovely return True statement!
    return True

#Time to test our detective skills!
def main():
    password = input("Enter your password: ")
    if validate_password(password):
        print("Awesome sauce! Your password passes all the checks! 🎉🕺💃")
    else:
        print("Bummer! Your password doesn't pass the validation checks. Better luck next time! 💔")

# Aaaaaaaaaaaaaaand, roll 'em!
if __name__ == "__main__":
    main()

