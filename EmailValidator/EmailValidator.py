
# Hehe, hiya, fun-loving code reader! Welcome to a shiny new Python project, named EmailValidator.
# This little tinker checks if a string is following the format of a valid email address. Pretty cool, huh?

# Okay, okay, let's take a deep dive in!

import re


def validate_email(email):
    """It's not just a function, it's THE function! It's the one that checks
    to see if an input string looks like a valid email. Don't you wonder how it works?"""

    # Now let's get busy with regex! 🚀
    email_regex = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$"

    # We'll create a match object by comparing our given email with our email_regex!
    match = re.match(email_regex, email)

    # If we find a match, it means our email is valid! Woohoo!
    # If there's no match, it means our email doesn't match (🥁 drum roll 🥁) our criteria and is invalid. 😐 
    # So, we just return True if there is a match, False otherwise.
    
    return bool(match)


# Now let's test this shiny beauty. But how? Well, I've come prepared with some test cases, sit back and watch!
# 😎
def run_tests():
    """It's test time! Because even though we're fun-loving, we're also responsible, yeah?"""

    # Imagine, below are some totally random emails. Trust me, they're just random! 😅
    test_emails = {
        "hello.world@example.com": True,
        "nogood@": False,
        "thisone@.extension": False,
        "@noLocalPart.com": False,
        "dotless@domain": False,
        "@": False,
        "": False,
    }

    # We'll iterate over each email and compare what our function thinks to what we think.
    # Hopefully, there won't be any disagreements! 😅
    
    for email, expected_result in test_emails.items():
        assert validate_email(email) == expected_result, f"Failed for: {email}"


# Time to put our lovely little function into action, we're calling the tests here. Fingers crossed! 🤞

if __name__ == "__main__":
    run_tests()
    print("Everything passed")

# Aaaaaand, we're done here, folks! Wasn't that a fun little ride? Until next time, happy coding! 🚀
