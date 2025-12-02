
# "Hello fellow traveller through the realms of code :) That you have found your way here, to this humble script, brings such joy to my circuitry heart.

# Welcome to CorrelationCalculator.py, the most chilled out place in cyberspace to calculate Pearson correlation coefficients between two lists.

# No need for APIs, external libraries or an internet connection. Just you, me and pure, unadulterated Python.

# So pop the kettle on, find that list of numbers you've been meaning to correlate, and let's dive in together!"

# --- START OF CORRELATIONCALCULATOR.PY --- #

# First things first, let's define a function to calculate the mean of a list.
def calculate_mean(data_list):
    # This is super simple, just sum up all the items and divide by the number of items.
    return sum(data_list) / len(data_list)


# Next, let's define another function to calculate the standard deviation.
def calculate_std_dev(data_list):
    # First, we calculate the mean of the list.
    mean = calculate_mean(data_list)

    # Then, for each item in our list, we subtract the mean and square the result.
    variance = sum((item - mean) ** 2 for item in data_list) / len(data_list)

    # The standard deviation is just the square root of the variance.
    return variance ** 0.5


# Now, for the main event, the Pearson correlation coefficient!
def calculate_pearson_correlation(x_list, y_list):
    # We'll need the mean and standard deviation of both lists.
    x_mean = calculate_mean(x_list)
    y_mean = calculate_mean(y_list)
    x_std_dev = calculate_std_dev(x_list)
    y_std_dev = calculate_std_dev(y_list)

    # Our Pearson correlation coefficient is the sum of the product of each pair of items, minus the mean of each list, divided by the product of the standard deviations.
    correlation = sum((x - x_mean) * (y - y_mean) for x, y in zip(x_list, y_list)) / (len(x_list) * x_std_dev * y_std_dev)

    # And there we have it, our Pearson correlation coefficient!
    return correlation

# Now, let's test our function with a couple of lists.
if __name__ == "__main__":
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    y = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(calculate_pearson_correlation(x, y))

# --- END OF CORRELATIONCALCULATOR.PY --- #

# "And there, my dear friend, is how we calculate the Pearson correlation coefficient between two lists.
# I hope our journey today has been as enlightening for you as it was delightful for me.
# Until next time, happy coding!" :)
