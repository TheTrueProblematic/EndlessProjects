# Exciting, isn't it? We're about to see if a list is playing nice and orderly or being a rebellious mess.
# Let's have fun testing lists for orderliness!

def is_sorted(input_list):
    # first, we check if the list is ascending.
    if all(input_list[i] <= input_list[i + 1] for i in range(len(input_list) - 1)):
        return 'The list is sorted in ascending order. How orderly!'
    # if not, let's see if it's descending.
    elif all(input_list[i] >= input_list[i + 1] for i in range(len(input_list) - 1)):
        return 'The list is sorted in descending order. Still ordered, how delightful!'
    # If it's neither, then we've got a rogue list. The audacity!
    else:
        return 'This list is all over the place. What a mess...'

# Let's put our wonderful function to work!
# Call the function with your list with this line:
# print(is_sorted(['your', 'list', 'here']))

# Remember, we don't judge your lists, we just sort them out... well, sort of!
# Happy ordering!