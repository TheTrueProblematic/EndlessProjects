
# MostCommonChar Python file
# Yeehaw! Let's have some fun while we count characters in a string!

def MostCommonChar(input_string):
  '''
  This function determines the most common character in a given string.
  
  :param input_string: A text string to analyze
  :returns: A tuple of the most common character in the string and its frequency
  '''

  # An empty dictionary to store each character and its frequency. 
  freq_dict = {}

  # We'll use a good ol' for loop here to check every character in the string.
  for char in input_string:
    if char in freq_dict:
      # If the character has already been spotted before, we increment its count.
      freq_dict[char] += 1
    else:
      # If it's the character's first rodeo, we add it to our dictionary.
      freq_dict[char] = 1

  # Now the magic part! We use the max function to find the character with the highest count!
  most_common_char = max(freq_dict, key=freq_dict.get)
  # We fetch the frequency of the most common char too, just for good measure.
  most_common_char_freq = freq_dict[most_common_char] 

  # We return our star of the show (most common character) and the number of tickets sold (its frequency).
  return (most_common_char, most_common_char_freq)

# If the script is run directly (instead of being imported somewhere), let it do some demonstration!
if __name__ == "__main__":
  input_string = input("Enter a string to find its most common character: ")
  char, freq = MostCommonChar(input_string)
  print(f"The most common character is '{char}' and it appears {freq} times.")
  
# That's all folks! Keep having a rootin' tootin' good time with Python! Yeehaw!

