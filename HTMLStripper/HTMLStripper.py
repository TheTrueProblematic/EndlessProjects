
# Hey there, lovely coder! 
# Today, we have a fun mission: To strip out pesky HTML tags from any string you toss at us
# What's even better? We can do this in any platform, as we're an ultra-portable Python script!

# No GUI? No Problem! We are a CLI warrior!
# Also, we don't need to access the internet, and we certainly don't need any additional dependencies.
# We are sufficient unto ourselves!

import re  # We only need a basic re module, nothing fancy!

def strip_html_tags(raw_html):
    """Our superhero function to strip out those pesky HTML tags."""
    
    # Let's go ahead and compile a regex pattern to find HTML tags in any string.
    # We look for anything that starts with < and ends with > essentially.
    # It's like playing hide and seek with tags!
    html_tag_pattern = re.compile('<.*?>')

    # Applying the powerful 'sub' method of our pattern!
    # It will find all the patterns defined (aka HTML tags) and replace them with an empty string.
    # It's like tag cleansing magic!
    clean_text = re.sub(html_tag_pattern, '', raw_html)
    
    return clean_text  # Et voila! clean_text is devoid of HTML tags!

# Okay, lovely coder! Now we'll need to interact with our command-line user.
# Buckle up and let's start the show!
if __name__ == "__main__":
    
    print("Hello, dear user! Please input your string filled with annoying HTML tags that you want to clean:")  # Friendly greeting!
    user_input = input()  # Collect the string from the user.
    
    # Now, let's pass this string to our superhero function and watch the magic show!
    no_tags_string = strip_html_tags(user_input)
    
    # Tada! Now let's show the user their nice, clean string!
    print("Here is your string after our magic cleaning:\n" + no_tags_string)

# That's it, my lovely coding comrade!
# This Python script will be your secret weapon when it comes to getting rid of nasty HTML tags!
# Happy Coding and we'll meet you at our next Pythonical adventure!
