
# Welcome to the exciting land of Python and Morse code! Yippee!
# Here is our cheerful script called MorseEncoderDecoder. 

# Let's define our awesome morse code dictionary, this converts letters to morse.
morse_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--',
              'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
              '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
              ' ': ' ', '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.', ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
              '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
              } 

# Well It's decision time! Let's reverse this dictionary for decoding Morse code. It's like time travel, but for words.
reverse_morse_dict = {val: key for key, val in morse_dict.items()}

# Let's define the function to encode from English to Morse. 
# We'll go through each character and covert it to Morse. Easy peasy!
def encode_to_morse(message):
  morse_code = ''
  for char in message:
    if char != ' ':
      morse_code = morse_code + morse_dict[char.upper()] + ' '
    else:
      morse_code += ' '
  return morse_code

# And now, let's decode from Morse to English. 
# It's time to reveal the secrets hidden in those dots and dashes!
def decode_from_morse(morse_code):
  morse_code += ' '
  message = ''
  citext = ''
  for letter in morse_code:
    if (letter != ' '):
      i = 0
      citext += letter
    else:
      i += 1
      if i == 2 :
        message += ' '
      else:
        message += reverse_morse_dict[citext]
        citext = ''
  return message

# Finally, let's create main function to drive our script. Wroom-wroom, here we go!
if __name__ == '__main__':
  message = input("Enter the message to encode or decode: ")
  choice = input("Enter '1' to Encode or '2' to Decode the message: ")
  if choice == '1':
    result = encode_to_morse(message)
  elif choice == '2':
    result = decode_from_morse(message)
  else:
    print("Invalid choice. Please enter either '1' or '2'.")
    exit(0)
  print("The translated message is: ", result)

# This is the end of our hilarious and fun coding adventure. 
# I hope you enjoyed it as much as I did. Still, every adventure has to end somewhere. 
# But keep playing with the script, that's where the fun is. Happy coding!
