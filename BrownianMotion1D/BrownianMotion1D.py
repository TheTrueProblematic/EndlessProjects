
# Woohoo! Hello to all you coding champs! 
# Our mission, if we choose to accept it, is an awesome adventure into the world of stochastics.
# We're going to simulate a classic and fun mathematical playground - the 1D Brownian Motion!

# Drumrolls please......We are going to do that without using any external library!
# Pure vanilla Python - that's what we're made of, right?!

# Let's begin our epic adventure!

# Start with creating a function to generate a random step
def generate_random_step():
    """
    Function to generate a random step: either +1 or -1
    """
    import random
    step = random.choice([-1, 1])
    
    return step

# Now, the journey of a thousand miles (or maybe just a few steps for our Brownian motion)
# Let's define our main function that simulates the Brownian motion
def simulate_brownian_motion(num_steps):
    """
    Function to simulate a 1D Brownian motion
    """
    # Let's get our feet wet. First step might as well be the most interesting random one!
    path = [ generate_random_step() ]
    
    # For every step in our path,
    for _ in range(num_steps - 1):
        # We add our next step to our last step
        next_step = path[-1] + generate_random_step()
        path.append(next_step) # we add this step to our memory, or path
    
    # And we're done! That's our walk! Let's print it and see how well we've done
    for step in path:
        print(step)

# Alright, time for the Big Crunch. We need to get things moving.
# Let's ask the user how long they want their Brownian motion path to be
def main():
    num_steps = int(input("How many steps do you want in your Brownian motion path? "))
    
    # Don't forget to call your simultaneously beloved and dreaded function
    # That's got your back every time and spews out the most mesmerizing Brownian paths!
    simulate_brownian_motion(num_steps)

# Ready to run? I can hear your heart drumming with excitement...
# Yes, YOU ARE READY! Call the MIGHTY main() and behold the spectacle.
if __name__ == "__main__":
    main()

# Woohoo! You've made it! So proud of you! You've simulated a Brownian motion in 1D!
# Things can get shaky and uncertain in life, just like our Brownian paths,
# but remember just as we embraced and found fun in the little randomness we created today,
# we can find joy and learning in the little uncertainties life throws back!
# Till next time, my coding champs...happy coding!

