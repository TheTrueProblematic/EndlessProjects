
# -*- coding: utf-8 -*-
"""
VarianceCalc.py

Hi there! Welcome to this fun python script that calculates the variance of a dataset.

It's a bit like being a math detective, as we'll be branching out and averaging out the numbers.
And just like your favorite detective novel, there won't be any libraries or external dependencies involved. Just pure, raw Python!

Our goal here is to come up with a number that gets the general feeling of how spread out our mystery (data) is.
So get ready to play the part of a statistician and dive into some number-crunching action!

This script will run on the CLI, so no GUI magic will be involved. Also, it's a standalone Python file. 
So no worries about installing or importing anything. It's as pure as you can get! 
"""

# first things first, let's get our data
data = input("Please enter your dataset, separated by commas. E.g., 1,2,3,4,5: ")

# now to do a little parsing magic to get our data into a list of integers
data = list(map(int, data.split(',')))

# Let's calculate the mean (average) of our data
def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

# Great, now we have our mean! Time to calculate the variance!
def calculate_variance(numbers):
    mean = calculate_mean(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return variance

# That's all the hard part done. Now, to print the variance!
print(f"The variance of your dataset is: {calculate_variance(data)}")

"""
Hope you had a great time with this script!

Remember, statistics doesn't have to be scary.
All you have to do is take it one number at a time,
and before you know it, you've got yourself a statistical analysis worthy of a professional statistician.
"""

