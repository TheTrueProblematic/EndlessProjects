
# BoxPlotStats.py
# Welcome to BoxPlotStats! It's time for some fun with stats! Who said statistics can't be a barrel of laughs?

# I'm a totally self-contained script that runs from the CLI, 
# like a ninja in the shadow, silent but very effective. I don't need anything but a plain python install to work. 
# No dependencies, no APIs, no internet access and definitely, no GUI needed! I'm multi-platform and am very happy to run wherever you want to use me.

# Let's dive right in into the deep waters of computing statistics for a box-plot, but don't worry, I'll be there holding your hand along the way.

def compute_boxplot_stats(numbers):
    """
    Compute box-plot statistics for a given list of numbers.
    """

    # First, let's sort the numbers because, well, order is good in life, and also in statistics.
    sorted_numbers = sorted(numbers)

    # Now, let's compute our quartiles. Yes, those fancy terms that make us sound smart in parties.
    # Quartiles divide the data into four segments, you know like north, south, east and west, but for numbers.
    n = len(sorted_numbers)
  
    # Getting the median. Right in the heart of our data!
    median = sorted_numbers[n//2]

    # Getting the lower and upper quartiles. Always comforting to know the bounds, right?
    lower_quartile = sorted_numbers[n//4]
    upper_quartile = sorted_numbers[3 * n//4]
    
    # Now, let's define what we call outliers. They're these odd ones out who didn't know when to quit. 
    # We define them as those that are more than 1.5 times the IQR away from the upper or lower quartile.
    iqr = upper_quartile - lower_quartile
    lower_bound = lower_quartile - 1.5 * iqr
    upper_bound = upper_quartile + 1.5 * iqr

    # Catching those straying too far from the pack.
    outliers = [number for number in numbers if number < lower_bound or number > upper_bound]
    
    # Now, let's package all these sweet data into a nice little dictionary to take away.
    stats = {
        'lower_quartile': lower_quartile,
        'median': median,
        'upper_quartile': upper_quartile,
        'iqr': iqr,
        'lower_bound': lower_bound,
        'upper_bound': upper_bound,
        'outliers': outliers,
    }
    
    return stats

# And that's all folks! You've braved the stormy seas of box plot statistics computing.
# You now know how to find quartiles, inter quartile range and outliers, aren't you a rockstar!

