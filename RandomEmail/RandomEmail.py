
# Hey there, fellow happy python programmer!
# This script's joyful goal is simple but fun, to generate an email address randomly.
# It's like having a lucky dip but for emails! Best part is, you just need a fresh python install, no extra packages needed!

# Let's import what we need, nothing more, nothing less.
import string
import random

# And now comes our spiffy random email generator!
def generate_random_email():

    # Alright, first things first, let's define our email parts. We need a local part, the @ symbol and a domain.
    # Picking some generic and funny domain names!
    domains = ["happy-mail", "code-love", "py-ninja", "cli-party"]
    
    # For the email's local part, let's make it a fun combo of random letters and digits!
    # You have the power to decide how long this part will be, let's make it 10 characters!
    local_part = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(10))
    
    # Now for the domain. We'll pick a random one from our cool domains list.
    domain = f'{random.choice(domains)}.com'
    
    # Time to create our email. It's as simple as sticking the local part, the '@' symbol and the domain together!
    email = f'{local_part}@{domain}'
    
    # Let's return our shiny, brand new email!
    return email

# And voila! Now the only thing left is to run our email generator!
if __name__ == "__main__":
    email = generate_random_email()
    print(email)

# Isn't it wonderful!? Random emails in a snap!
# Thanks for joining in this fun little project! 
# Keep coding and remember to always enjoy what you're doing. Happy coding! :)

