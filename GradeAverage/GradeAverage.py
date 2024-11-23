
# Hello! Here's a fun Python script I've written called 'GradeAverage'.
# We're going to calculate the average grades from a list of scores.
# Everything should be super simple and no-frills, we're not using any GUI, external libraries, or funky stuff at all here.
# Cool, let's get started!

# Here's the function to do all the hard work!
def calculate_average(scores):
    # We just take the sum of all the scores (total_points) and divide by how 
    # many there are (number_of_scores). Easy-peasy!
    total_points = sum(scores)
    number_of_scores = len(scores)
    return total_points / number_of_scores

# Now the fun part! We need some scores to calculate the average of.
# These will be the scores we'll use for this particular example.
# You can replace this with your own, if you'd like!
scores = [85, 89, 91, 95, 97]

# And finally, we'll print out the average score.
# The result will be displayed as a decimal number.
# You'll need to manually run this script from your favorite command line interface.
# I hope you have as much fun running this as I did writing, cheers!
print(calculate_average(scores))

