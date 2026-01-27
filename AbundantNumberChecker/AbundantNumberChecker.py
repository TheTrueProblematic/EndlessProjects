
# Hello there, wonderful person! ☀️
# Ready for a trip into the fun, magical world of Abundant Numbers? 🎩 🐰
# Well, buckle up, because that's exactly where this Python script is taking you! 🚀

# So... what's an 'abundant' number, you ask?
# In number theory, an abundant number is a number that is smaller than the sum of its proper divisors.
# The proper divisors of a number are all divisors the number has, except for the number itself.

def find_divisors(n):
  """ This function takes an integer n and finds all its divisors excluding the number itself. """
  divisors = [i for i in range(1, n) if not n % i]
  return divisors

def is_abundant(n):
  """ This function checks if a number is abundant. """
  # First, we find all divisors
  divisors = find_divisors(n)

  # If the sum of divisors is greater than n, then voila! It's an abundant number 🎉
  if sum(divisors) > n:
    return True
  else:
    return False

# Now let's make a fun little game out of this! 🎮
# We'll ask the user to provide a number, and our script will tell them if it's an abundant number

def main():
  print("Welcome! Let's check if your number is abundant!")
  number = int(input("Enter a number: "))
  
  if is_abundant(number):
    print(str(number)+" is an abundant number! 🎉💃🕺")
  else:
    print(str(number)+" is not an abundant number. 😕👎")

# The best way to predict the future is to create it, so let's start the program now! 🚀
if __name__ == "__main__":
  main()

