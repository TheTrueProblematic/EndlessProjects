
"""
Hey there, fellow code enthusiast!<chuckles>

I am your friendly neighbourhood code, NumberDivider!

What is my job you ask? Well, I run around finding all divisors of a given number. 
Yup! My life is as exciting as it sounds. 

Let's dive right in, shall we?
"""

# Importing necessary libraries so I am not all alone in this world ;)
import sys

def find_divisors(num):
  """
  This function is the brain of the operation here.
  It goes from 1 to the number and checks if its a divisor of the number. If it is, then it is added to the divisors list.
  """
  
  # Empty list to store all our heroes (divisors)
  divisors = [] 

  # Loop from 1 to 'num'
  for i in range(1, num + 1):
    # If 'num' is divisible by 'i', add 'i' to the list of divisors
    if num % i == 0: 
      divisors.append(i)

  # Return the complete list of divisors 
  return divisors 

def main(num):
  """
  The main function that pulls all the strings!
  Ties all the functionality together and displays the answer.
  """
  
  # Call to the brain function to find the divisors
  divisors = find_divisors(num)

  # We are ready! Let's print out the divisors
  print(f'The divisors of {num} are: ', divisors)

# Begin our adventure by calling the main function with command line argument as input
# Remember, only integers are allowed. I still can't process those floating points. Maybe, in future versions!
if __name__ == "__main__":
  main(int(sys.argv[1]))

"""
And that's all there is to it! 
Had fun? I certainly did! :D

Catch you up in the next code! Till then...
Ciao!
"""

