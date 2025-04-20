"""
Hey there! Welcome to the magical world of the 'DivisorsFinder'!😊
Our radiant little python script, that brings immense joy by helping you find all the divisors for a certain number.
Isn't that cool?😉
Kicking off with an active web of no internet access at all, our script is totally self-reliant like a boss! Besides, no GUI! We are keeping it all classy and vintage here!
Let's dive in, shall we?😃
"""

def find_divisors(some_number):
    """
    Awww yeah, here's our charming little function! 😃
    'find_divisors' straight away takes an integer and finds all the divisors as if by magic!🌟
    """
    # Place to store all our magnificent divisors!
    divisors_list=[1,some_number]
    
    # Let's loop through starting from 2 till some_number
    # If a number divides evenly into some_number, we add it to the list.
    for i in range(2, (some_number//2)+1):
        if (some_number % i)==0:
            if i not in divisors_list:
                divisors_list.append(i)
    
    # We return the list, sorted because we are neat people 🧹
    return sorted(divisors_list)

if __name__ == '__main__':
    """
    This is where the spotlight shines on our main function!🌟
    Here's where we take the input from the user-played of course, by a friendly console prompt!😉
    No worries, we made sure it throws an ValueError if someone enters anything that's not an integer - we got your back!😉
    """

    try:
        # Tadaaa! A prompt to get the number for which we need the divisors!
        number = int(input("Enter a number to find its divisors: "))
        
        # Calling our charismatic 'find_divisors' function to get the divisors and print it in a stylish way!😎
        print("Divisors of", number, "are", find_divisors(number))

    # Catch any error thrown because of invalid input!
    except ValueError as e:
        print("Oops!😟 Please enter a valid integer. Let's start over, shall we?😄")