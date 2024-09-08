# For our adventure today, we'll be spinning into the world of cryptography! Specifically, we're going to tackle the Caesar cipher; a time tested method of scramblin' your messages to confound any unwelcome snoops.


def caesar_encrypt(text, shift):
    """
    Our brave encryption function.
    Takes in a message and a shift value, then scrambles the message based on the shift value.
    Returns the scrambled message- a perfectly encrypted text!
    """
    result = ""
    for char in text:
        if char.isalpha():  # We're only scrambling letters, numbers or special characters remain the same
            ascii_val = ord(char)  # Get the ASCII value of the character
            ascii_offset = ord('a') if char.islower() else ord('A')  # Lowercase characters start from 'a', uppercase start from 'A'
            # Subtract the starting ASCII value, add the shift then modulo by 26 (no. of alphabets) gives us new character after shift
            new_char = chr((ascii_val - ascii_offset + shift) % 26 + ascii_offset)
            result += new_char
        else:
            result += char  # if it's not a letter, leave it be
    return result


def caesar_decrypt(text, shift):
    """
    Our dependable decryption function.
    And, look, it's all too simple, we're just going to shift in the opposite direction!
    Takes in an encrypted message and a shift value, then reverts the message to its original form.
    Returns the deciphered message- your original text!
    """
    return caesar_encrypt(text, -shift)  # To decrypt, we simply reverse the shift by negating it!


def main():
    """
    The mighty main function.
    To run our little program from the command line and interact with user.
    """
    print("Enter the text to be encoded or decoded:")  # We ask politely for the text to be scrambled or unscrambled
    text = input()
    print("Enter the shift value:")  # We'll also need the shift value
    shift = int(input())
    print("Would you like to encode or decode the text? [E/D]")  # Let's ask our user what they want to do!
    choice = input()
    if choice.lower() == 'e':  # Encode if user selects 'E' or 'e'
        print("Scrambling text...")
        result = caesar_encrypt(text, shift)
    elif choice.lower() == 'd':  # Decode if user selects 'D' or 'd'
        print("Unscrambling text...")
        result = caesar_decrypt(text, shift)
    else:
        print("Unrecognized option! Please enter either 'E' for encode or 'D' for decode.")  # Just in case!
        return
    print("Here's the result:")
    print(result)  # Finally, we proudly present them with their scrambled/unscrambled text


if __name__ == "__main__":  # For the ambitious folks running this from the command line
    main()  # start the adventure at the main function!

# Voila! Enjoy your encrypted adventures with Caesar, explorer!