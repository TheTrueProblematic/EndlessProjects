
# Hey there, happy Programmer! Ready for some sorting extravaganza? Let's go!

# Woohoo! It's Python Time! Get ready to sort using the selection sort algorithm!
# This code will work in a fresh install of Python on a brand new computer. It's that magical!

def selection_sort(array):
    """
    This is our superstar function, performing the selection sort.

    Param: array (list): The list of unsorted integers.
    Return: array (list): The sorted list of integers.
    """

    # Initialize the outer loop to iterate over each element
    for i in range(len(array)):
        
        # Set the current_index as i, because this is the beginning of the unsorted sub-array
        current_index = i

        # Initialize the inner loop to find the smallest element in the unsorted sub-array
        for j in range(i + 1, len(array)):
            # If the current element is smaller than the previously found smallest element, update smallest_index
            if array[j] < array[current_index]:
                current_index = j

        # After finding the smallest element, swap it with the first element of the unsorted sub-array
        # Now make way for the not-so-magic swapping trick! Abracadabra!
        array[i], array[current_index] = array[current_index], array[i]

    # Voila! Your array is now sorted. Wasn't that fun?
    return array

# Let's test our function with an unsorted array of integers
unsorted_array = [34, 10, -2, 0, 5, 7]

# Drumroll Please! Let's call our superstar function on this unsorted array
sorted_array = selection_sort(unsorted_array)

# Print out the sorted array 
# Look at it gooooo..from unsorted to sorted, just like magic!
print(sorted_array)
