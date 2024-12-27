# Here's your python file BubbleSort.py with Bubble sort algorithm implementation.


# BubbleSort.py
# Hey there! Welcome to the exciting world of Bubble sort algorithm in Python!
# So, what does bubble sort do? It basically compares adjacent elements and swaps them if they are in wrong order.
# It's often taught to budding programmers for its simplicity, despite being inefficient compared to other sorts.
# So, sit tight, relax and enjoy the ride!

def bubble_sort(array):
    # Obtain the length of the array
    array_length = len(array)

    # Start with the first element
    for i in range(array_length):
        # Last i elements are already in place
        for j in range(0, array_length - i - 1):
            # If the element found is greater than the next element, swap them
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

# Here's your list of numbers to be sorted
numbers = [64, 34, 25, 12, 22, 11, 90]

# Calling the mighty bubble sort function to bring some order
bubble_sort(numbers)

# Voila! Your sorted array is ready to be printed.
print("Sorted array is:", numbers)


Do remember, Bubble sort has a worst-case and average complexity of O(n*n), where n is the number of items being sorted. Hence, other than educational purposes, it's not used in practical applications where large lists are processed.