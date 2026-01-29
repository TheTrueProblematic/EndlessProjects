
# Hey there! Welcome to our little Deficient Number Checker! It's the life of the party!

# In number theory, a deficient number is a number n for which the sum of its proper divisors 
# (divisors including 1 but not itself) is less than n. For example, the proper divisors of 
# 22 are 1, 2, 11, and the sum of which is 14, which is less than 22. So, 22 is a deficient number.

# Now, let's dive in and create a function that tells us whether a number is deficient or not. Here we go!

def is_deficient(n):
    # Step 1: Finding the divisors of the number
    # We'll start by initialising a list with the first proper divisor: 1
    divisors = [1]
    # Let's loop through from 2 to sqrt(n) (inclusive). Why sqrt(n)? It's just a fun mathematic trick :)
    i = 2
    while i * i <= n:
        # If 'n' is divisible by 'i', then 'i' is a divisor of 'n'
        if n % i:
            i += 1
        else:
            # If 'i' is also equals to its counterpart 'n//i', we've hit jackpot! We've found a divisor.
            if i == (n // i):
                divisors.append(i)
            else:
                # If 'i' is not equal to 'n//i', we've got two different divisors! Jackpot twice!
                divisors.append(i)
                divisors.append(n//i)
            i += 1

    # Step 2: Checking if the number is deficient
    # We've got all divisors now, so if sum of divisors is less than 'n', it's deficient!
    if sum(divisors) < n:
        return True
    return False


# Now let's make our little deficient friend interactive!
def main():
    print("Welcome to the Deficient Number Checker! Ready to have some mathematical fun?")
    while True:
        # Asking for the number
        num = int(input("Enter a number to check: "))
        if is_deficient(num):
            print(f"Woah! {num} is a deficient number!")
        else:
            print(f"Oops! {num} is not a deficient number!")
        # Giving the chance to the user to check another number or leave the script
        should_continue = input("Check another number? (yes/no): ").lower()
        if should_continue != 'yes':
            print("Okay, bye! Have a nice day!")
            break

            
if __name__ == '__main__':
    main()
