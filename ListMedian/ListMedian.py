"""
Hey there! This is your Pythonista friend who loves to keep things neat and clean.
And guess what I am going to do today? Yes, I am here to help you find the median of a list of numbers.
Isn't it exciting? So, let's get on with it, shall we?

"""     

def calculate_median(number_list):
    """
    This piece of art, also known as a function, receives a list full of numbers as input.
    Then it finds the middle man, the median. Oh and it's multi-platform capable. How cool!
    """
    
    # First, we sort the list. Got to keep things tidy, you know!
    number_list.sort()
    
    # Finding out if the list length is even or odd. Yeah, I like to keep it inclusive for all lengths, haha!
    if len(number_list) % 2 == 0:
        # Even case: the median is the average of the two middle numbers. Easy peasy lemon squeezy!
        # We take the average of the two middle numbers.
        median1 = number_list[len(number_list)//2]
        median2 = number_list[len(number_list)//2 - 1]
        median = (median1 + median2)/2
    else:
        # Odd case: the median is the middle number. Just like the cream in an Oreo!
        median = number_list[len(number_list)//2]

    # Return our proud median!
    return median

"""
And voila! We're done! This function is ready to find medians of lists.
And remember: in stats, as in life, always look for the balance point ;)
"""

# Ok! Let's test this out with some quick test. Don't worry, you can remove it afterwards. Just remember to feed it with a list of numbers!
#print(calculate_median([1, 2, 3, 4, 5]))  # Uncomment to test
