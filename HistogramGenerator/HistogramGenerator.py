
# Ahoy matey! Get ready for an exciting journey into the world of histograms!
# This, my friend, is the code to generate text-based histograms.
# It's like sailing on a sea of numbers, but instead of getting wet, you get insights!

# You don't need fancy-schmancy installations or even the internet to run me. I'm completely self-reliant. Promise!

def read_data():
    """This function is like our telescope. It reads input data from the user."""
    data = input('Please enter your numeric data values separated by commas: ')
    data = data.split(',')
    data = [float(i) for i in data] # Converting the input values to numeric format
    return sorted(data) # This will make our ride smoother down the line

def histogram(data):
    """Meet our ship. This function will take our data and turn it into a histogram."""
    # First let's find the range of our data
    min_value = min(data)
    max_value = max(data)

    # Now, let's slice that range into 10 bins
    step = (max_value - min_value) / 10

    # Prepare our bins!
    bins = [0 for _ in range(10)]
    
    # Time to count how many data points fall into each bin!
    for number in data:
        for i in range(10):
            if min_value + i*step <= number < min_value + (i+1)*step:
                bins[i] += 1
                break
    
    # Special condition for the maximum value
    if data[-1] == max_value:
        bins[-1] += 1

    return bins

def print_histogram(bins):
    """Now, for the grand revelation! Time to print our histogram to the console."""
    for index, value in enumerate(bins):
        print((str(index) + '-' + str(index+1) + ': ') + '#'*value)

def main():
    """Every journey needs a map. This function is our map, guiding us through the other functions."""
    data = read_data()
    bins = histogram(data)
    print_histogram(bins)
    
# It's time to set sail, matey!
if __name__ == "__main__":
    main()

