Python
# Hey there, wonderful coder! This python script is your new friend to help you calculate
# compound interest with regular intervals. Stay tuned and let's go on this mathematical ride together!

# Firstly, we are accepting user input.
# It doesn't matter if it's coffee, weekends or user input. Anything in excess is bad
# Don't worry! We've handled it here with our try-except blocks

# Let's begin our fabulous journey of calculating compound interest!

# Wohoo, We are on the way! Let's start by getting principal amount. Hop on!

try:
    principal = float(input('Enter the principal amount: '))
except ValueError:
    print("Oops! That was not a valid number. Better luck next time!")
    exit()

# Next, we are getting the rate of interest.
# Just like gummy bears and ice cream! The moment is getting sweeter and sweeter!

try:
    rate_of_interest = float(input('Enter the rate of interest: '))
except ValueError:
    print("Oops! That was not a valid number. Better luck next time!")
    exit()
    
# Oh boy! Now let's bring in the time in years that will take us farther into our code!

try:
    time_in_years = float(input('Enter the time in years: '))
except ValueError:
    print("Oops! That was not a valid number. Better luck next time!")
    exit()

# Now, let's not forget the number of times interest applied per time period
# Yes, this can be tricky as a jellybean puzzle! But bear with me.

try:
    num_times_compounded = int(input('Enter the number of times interest is compounded per time period: '))
except ValueError:
    print("Oops! That was not a valid number. Better luck next time!")
    exit()

# Alright folks! With all the inputs in hand, we are ready to dive into our formula.
# The following line calculates compound interest. This might look like a complicated line dance step, 
# but it's as easy as pie when broken down!

compound_interest = principal * (pow((1 + rate_of_interest / (100*num_times_compounded)), num_times_compounded*time_in_years))

# Now that we've calculated the compound interest, let's reveal it to our user, just like the climax of a good movie!

print("The total compound interest is: ", round(compound_interest, 2))  # Rounding off to 2 decimal points because, well, neatness!

# And that's it folks! We've estimated the compound interest with the given inputs, 
# and it's safe to say, this has been a scintillating journey! 

# So, pat yourself on the back! You've done a wonderful job running this script!
# Until next time, happy coding!
