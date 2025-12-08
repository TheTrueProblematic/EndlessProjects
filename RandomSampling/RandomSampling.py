
# Hey there, pythonic pal! Welcome to the RandomSampling.py code!
# Get ready to embark on a fun journey of data sampling, python style! :)
# And remember, always keep your coder spirit high when the chips are down. 

# Let's start by importing the 'random' module.
# It's like the secret sauce that adds a bit of spice to our dish today: data sampling!
import random

# Now, let's define our beautiful dataset.
# You can replace this with any list of elements you want to sample!
# Oh, and don't worry about the dataset size, big or small - our code is one-size-fits-all! ;)

dataset = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Here comes our main player, the 'random_sample' function!
# This function is like the lottery ticket checker. It takes your dataset and 
# a number 'n' and gives you 'n' randomly sampled elements from your dataset. 
# The best part? No replacement! Every lottery number (or dataset element) can win only once. ;)

def random_sample(dataset, n):
    # Checking if the sample size is larger than the total data set.
    # We don't want to promise more random samples than we can deliver, do we?
    if n > len(dataset):
        return "Oops! Your sample size cannot be larger than the total dataset size."

    # The 'random' module's 'sample' function comes to the rescue!
    # It's like the magic wand that does all the sampling work for us.
    # We just pass it the dataset and the number of samples we want, and voila - random samples! 
    sample = random.sample(dataset, n)

    # And now, for the final moment, let's return our random sample to the outside world!
    return sample

# Finally, let's test out our function.
# We'll try to grab 5 random samples from our dataset.
# Feel free to chance the value here! The world (of your dataset) is your oyster!
print(random_sample(dataset, 5))

# Well, that's it, my fellow coder!
# Remember, in the world of code, every problem is a new opportunity to learn and grow.
# So, keep coding, keep shining, and above all, keep enjoying the journey!
# Happy pythoning, and until next time... :)

