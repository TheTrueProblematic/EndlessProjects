
# Welcome, future coder! You've landed on a neat little script that, like a magical cardboard box, 
# transforms hexadecimal color codes into RGB values! Amazing, isn't it? 
# So, buckle up as we dive into this magical Python ride.

def hex_to_RGB(hex_code):
    # Woah, hold on there! 
    # A hexadecimal color code, as you know, is a six-digit code in hexadecimal (base 16) notation
    # Each two digits represent the Red, Green, and Blue components. Sound much like RGB? Yes, it does!
    # We just need to convert them to decimal values. Python has a sweet, built-in function for that.

    rgb = [int(hex_code[i:i+2], 16) for i in range(0, 6, 2)]
    # Ahem! Did we just do something super cool in that line?
    # Yes, indeed, Kiddo! We used List comprehension.
    # We split our hex code into three parts (That's why 2 there in i:i+2)
    # String was converted to int with base 16 (our hex, remember?). 
    # The loop happened three times, giving us red first, green next, and blue last.

    return tuple(rgb) # tuples, cute aren't they? Returning our RGB as a tuple

if __name__ == "__main__":
    # So, Mr. Python himself decided to be our script-running DJ today. 
    # When you run the script directly, it treats the name as "__main__". Cool, isn't it?

    hex_code = input('Enter Hexadecimal code: ') # Listening for the hex code. Let's be polite and ask for it.
    # Shhh! Don't whisper it loudly, remember, no # here. Just the six magical characters.

    # We don't like unwanted guests, do we? Strictly six characters, dear!
    if len(hex_code) != 6:
        print('Invalid Hex Code. Hex Code should be 6 characters long without hash (#) symbol')
    else:
      rgb = hex_to_RGB(hex_code) # Let magic happen!
      print('RGB:', rgb) # Tadaa! Your RGB is awaiting you.

# On a serious note, I hope this was somewhat helpful in your coding journey.
# There are more complex programs out there, and I can't wait for you to dive deeper. Happy Coding!
