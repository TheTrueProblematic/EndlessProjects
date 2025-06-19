
# Howdy! Welcome to our fun little project: the URLSlugGenerator! 
# It's just a simple, modest python script whose only job in life is to turn text into url-friendly slugs, you know, the kind that you can safely put in your browser's address bar.

# Now, you may ask, why does this exist? Well, it's because computers and the web often don't like the funny characters we humans use in our text. Spaces? Tsk tsk, not url-friendly! Accented characters? Nope, not url-friendly either! 

# So, our little URLSlugGenerator is here to help. It takes text and converts it into something that urls will happily accept, helpfully stripping out anything they don't want to see.

# Please note: this script is designed to run in the command line, and it should work beautifully in a fresh install of python on a brand spanking new computer. Heck, it doesn't even need to access the internet. Just pure, simple, python. :)

def generate_url_slug(text):
    """Generate a URL-friendly slug from the provided text."""
    
    # Aha! Here's our first bit of magic. Python's string methods are really handy, and we're about to make good use of them.
    
    # To begin, we use the lower() method to make sure everything is in lowercase. URLs tend to prefer that. After, we use the replace() method to swap any space characters with hyphens.
    # Why hyphens? Well, hyphens are url-friendly and often used in URL slugs to represent spaces. Makes things nice and easy to read!
    slug = text.lower().replace(' ', '-')
    
    # Okay, we've got our basic slug, but we're not quite done. We need to strip out any characters that URLs don't like. 
    # Python's handy dandy join() method, and the isalnum() method come to the rescue!
    slug = ''.join(e for e in slug if e.isalnum() or e == '-')
    
    # Voila! We've got ourselves a URL-friendly slug! 
    return slug

if __name__ == "__main__":
    # If we run this script directly, let's get some text from the user and turn it into a slug. 
    # This bit of code won't do anything if this script is imported as a module, which is pretty neat!
    text = input("Please enter the text to convert to a url-friendly slug: ")
    print(f'The URL friendly slug is: {generate_url_slug(text)}')

# And there we have it! A simple, easy to understand URL slug generator. Isn't python fun? 

