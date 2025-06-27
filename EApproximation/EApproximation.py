
# EApproximation.py

# Yippee! We're going on a delightful grand adventure to approximate Euler’s number e using a series expansion!
# I mean, who doesn't love a good challenge, right! So sit tight, buckle up, get a hot drink and enjoy the ride!

# It's also important to note that we're going to be doing this entirely within the comfort of our command line interface (CLI), no GUI distractions at all. And yes, no dependencies either - we're going on this adventure alone. 

# And finally, let's start on this series expansion journey ☺

def factorial(n):
    # Factorial fun! Recursively calculating factorial of any number.
    return 1 if n==0 else n*factorial(n-1)

def calculate_e_approximation(n):
    # Let's bring in the big guns. The math!
    # We're going to add up the reciprocals of all the factorials up to n. Sounds funky, doesn't it?
    e_approximation = sum([1/factorial(i) for i in range(0, n+1)])

    # Amazing! We've done it. We have our approximate e value.
    return e_approximation

# Now we need to figure out to which order we want to calculate this e approximation.
# Let's say we take 10 as an example, but you can replace with any integer value you desire!
order = 10

# And off we go! Let's call the function and print out the result - our approximation of e! Exciting stuff!
print(calculate_e_approximation(order))

# And that's it, my friend! We're done. We did it. And wasn't it a great quest?
# Thanks for joining me, fellow coder. Until the next adventure!

