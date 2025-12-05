
# Welcome to the magical world of programming, where we make your computer go abracadabra!
# You're in for a treat today, as we code a fun and exciting feature - the Median Absolute Deviation (MAD)!
# We're keeping it simple and friendly, so even the most novice of coders or statisticians can understand.

# Since we're all about independence, this script won't rely on any external libraries, APIs or even internet access. 
# It's a standalone guy, working tirelessly in its python environment.

# The script is designed to be executed from the command line. No fancy GUIs here, just good old CLI action!
# So grab a cup of your favorite brew, and join us on this coding journey!

def compute_median(dataset):
    """
    Function to compute the median of a data set.

    Remember, the median is the 'middle' number in a sorted, ascending or descending, list of numbers.
    Like that nerdy kid sitting right in the middle of the classroom!
    """
    n = len(dataset)
    dataset.sort()

    if n % 2 == 0:
        median1 = dataset[n//2]
        median2 = dataset[n//2 - 1]
        median = (median1 + median2)/2
    else:
        median = dataset[n//2]

    # Right here, we're giving you the 'middle' guy of your data.
    return median


def compute_mad(dataset):
    """
    Function to compute the MAD of a data set.

    MAD? No, it's not what you're thinking! It's the Median Absolute Deviation, a measure of variability in your data.
    """
    # First off, we find the median of our data set.
    median = compute_median(dataset)

    # Now, we're gonna create a new data set which includes the absolute deviation of data points from the median.
    absolute_deviation = [abs(x - median) for x in dataset]

    # Finally, let's compute the median of this new data set, which will be our MAD.
    mad = compute_median(absolute_deviation)

    # Voila, there you have it – your MAD!
    return mad

# So why don't you give it a go? Input your data as a list and watch the magic happen!
# Fun, wasn't it? Smile, you're a programmer!
