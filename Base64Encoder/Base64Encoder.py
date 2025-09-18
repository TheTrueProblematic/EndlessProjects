
# Hey there! Welcome to the wonderful world of base64 encoding and decoding! We've got bits and bytes aplenty!
# This jolly little python script is here to help you encode and decode your text using the ever handy built-in base64 library!

import base64   # Here's our trusty friend, the base64 library!

def encode(text):
    # Let's go on an adventure and transform this text into a magical, mystical base64 encoded string!
    text_bytes = text.encode('utf-8')  # First, we'll need to convert our text into bytes.
    encoded_bytes = base64.b64encode(text_bytes)  # Next, we wave our little base64 wand to encode these bytes.
    encoded_text = encoded_bytes.decode('utf-8')  # Finally, we'll convert those bytes back into text. Et voila, base64 encoded text!
    return encoded_text

def decode(encoded_text):
    # Feeling a bit nostalgic? Want your original text back? No problemo, let's decode that base64 text!
    encoded_bytes = encoded_text.encode('utf-8')  # First, convert the base64 text into bytes.
    text_bytes = base64.b64decode(encoded_bytes)  # Then, cast our decoding spell with the base64 library.
    text = text_bytes.decode('utf-8')  # Finally, convert those bytes back into text. Just like magic, you've got your original text back!
    return text

if __name__ == "__main__":
    # This is where the real magic begins! Let's turn this script into a CLI application!
    import argparse  # Importing the argparse library to help us parse command line arguments.

    # Let's set up our script arguments in a friendly, welcoming manner!
    parser = argparse.ArgumentParser(description="Encode and decode text using base64. Just your friendly neighbourhood text manipulator!")
    parser.add_argument('--encode', help="The text you'd like to encode into base64")
    parser.add_argument('--decode', help="The base64 text you'd like to decode into plain text")

    # Time to parse those arguments!
    args = parser.parse_args()
    if args.encode:
        # If the user wants to encode some text, let's take them on a whirlwind tour of base64 encoding!
        encoded_text = encode(args.encode)
        print(f"Here's your base64 encoded text: {encoded_text}")
    elif args.decode:
        # If they want to decode some text, then step right in, the decoding extravaganza is about to begin!
        text = decode(args.decode)
        print(f"And we're back! Here's your decoded text: {text}")

