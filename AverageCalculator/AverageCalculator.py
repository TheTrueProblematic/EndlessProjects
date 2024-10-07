# Hey there, fellow coder! Welcome to the very simple, yet super useful AverageCalculator!

# What this little script does is it calculates the average of a list of numbers. It's a cinch!

# Let's dive right in, shall we? 

def calculate_average(numbers):
    # Drum roll, please! 🥁 And here we have the star of our show: `calculate_average`.
    # A function, as simple as they come, that simply calculates the average (mean) value.
    
    # First, we need to make sure we don't divide by zero - that would cause quite the catastrophe!
    if not numbers:  # If the list is empty...
        return 0  # ...we return 0. Much better than an error, wouldn't you agree?
    
    # Then we just get down to business!
    # The sum function adds up all our numbers, and len() tells us how many numbers we have in total.
    # Dividing the sum by the length gives us our average. Easy peasy lemon squeezy!
    return sum(numbers) / len(numbers)

# But hold on, what about our input? Fear not, it's all taken care of!
if __name__ == "__main__":
    # Here we make sure our script will only run if it is the main script,
    # kind of like in a movie, we don't want our stand-in showing up in the final cut by mistake.
  
    # We'll be nice and greet our user.
    print("Hello, darling! Ready to calculate some averages? Let's do it!")
  
    # get inputs from the user
    numbers = input("Please input a list of numbers, separated by commas: ")
  
    # Here, we split up the user's input based on commas, and map each piece to a float.
    # The map function is kind of like a magical multi-tool, applying the float function to all our string numbers.
    numbers = list(map(float, numbers.split(',')))
  
    # Print the average!
    print(f"The average of your numbers is {calculate_average(numbers)}")

# And that's all folks! You now have your very own average calculator!
# Go forth and calculate to your heart's content.
# Until next time, happy coding! 🚀