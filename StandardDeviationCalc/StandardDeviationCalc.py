
# Hey there, Future Developer! Having a great day, I guess?!
# Now you must be wondering what this little piece of code does.
# We are going to have a fun journey calculating the standard deviation of a set of numbers!
# Let's dive in, shall we?

# Python helps us to do the job in a simple way!
# But before we get there, let's understand what the Standard Deviation is.
# It's a measure of the amount of variation or dispersion of a set of values.

# Now, Python does not have any dependencies and this script won't need any either.

# To calculate the standard deviation, we divide our task into sequencial steps:
# 1 - Calculate the Mean (Average)
# 2 - For each data point, find the square of its distance to the mean (squared differences)
# 3 - Take the average of those squared differences. (This is Variance)
# 4 - Take the square root of that and we get the standard deviation!

def calculate_mean(dataset):
    # Raw blissful calculations for the mean (average)
    return sum(dataset) / len(dataset)

def calculate_squared_differences(dataset, mean):
    # Let's find the square of the difference from the mean for each datapoint.
    return [(data - mean) ** 2 for data in dataset]

def calculate_standard_deviation(squared_diffs):
    # The finale! We take the square root of the average of the squared differences
    # Let's calculate using the function we implemented above (DRY is the key, remember?)
    variance = sum(squared_diffs) / len(squared_diffs)
    return variance ** 0.5

def standard_deviation(dataset):
    # Pulling it all together and getting Standard Deviation
    mean = calculate_mean(dataset)
    squared_diffs = calculate_squared_differences(dataset, mean)
    std_dev = calculate_standard_deviation(squared_diffs)
    return std_dev

# Test it out!
def main():
    dataset = [2, 4, 4, 4, 5, 5, 7, 9] # You can put any dataset you want to calculate the standard deviation of it here!
    print("Standard Deviation: ", standard_deviation(dataset))

if __name__ == "__main__":
    main()

# You did great! Now you can calculate standard deviations like a PRO! Keep coding, and having fun!

