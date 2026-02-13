
# Hey there, happy coder! Ready to dive into some fun with numbers?
# This program is called PalindromePrimeChecker and it'll help you find out if a prime number is a palindrome!

# Alright, let's get to coding!

# This function checks if a number is prime.
def is_prime(num):
    # A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    # If our number is less than 2, it's not prime, buddy.
    if num < 2:
        return False
    # If our number is 2, it's definitely prime!
    elif num == 2:
        return True
    # Here we rule out all the even numbers except 2, they can't be prime.
    elif num % 2 == 0:
        return False
    # If none of the conditions above have been met, we loop through odd numbers up to the square root of our number.
    # If we find a number that divides our number evenly, then it's not a prime.
    else:
        for n in range(3, int(num**0.5)+1, 2):
            if num % n == 0:
                return False
        return True

# Now let's check if it's a palindrome. You know, reads the same forward and backward!
def is_palindrome(num):
    return str(num) == str(num)[::-1]

# Alright buddy, let's put these two together in our main function, PalindromePrimeChecker.
def PalindromePrimeChecker(num):
    # If our number is prime and a palindrome, we'll cheer out loud (in code language)!
    if is_prime(num) and is_palindrome(num):
        print(str(num) + " is a prime number and a palindrome! How cool is that?")
    else:
        print("Unfortunately, " + str(num) + " is not both a prime number and a palindrome!")

# Let's give our program a test run
PalindromePrimeChecker(131)  # The output should be "131 is a prime number and a palindrome! How cool is that?"

# Hope you had fun going through this code. Happy coding, buddy!
