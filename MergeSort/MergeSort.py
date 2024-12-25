
# Hello, fellow adventurers of code! This script is all about implementing the classic Merge Sort algorithm.
# Buckle up because we are about to embark on a journey of dividing, conquering, and fundamentally, sorting!

def merge_sort(array):
    """Function to sort an array using merge sort algorithm"""
    # If the array length is 1 or empty, we can't really sort it any more than it's already sorted
    # So, we just return the original array
    if len(array) <= 1:
        return array

    # We need a middle point to effectively split our array into two halves
    # So, we divide it the simple way, no magic needed!
    midpoint = len(array) // 2

    # Recursively sort both splits of the array
    # Yes, it's a function calling itself. So, we're getting a bit inception-y here.
    # But recursion is the soul of this algorithm, so let's just roll with it!
    left_half = merge_sort(array[:midpoint])
    right_half = merge_sort(array[midpoint:])

    # Now that we have nice, sorted halves, it's time to merge them back
    # And that's why it's called merge sort. Who would have thought?
    return merge(left_half, right_half)


def merge(left, right):
    """Function to merge two arrays"""
    # Ah, the heart of our trip! At this very station, we are merging sorted arrays back into a single sorted one.
    result = []
    left_pointer = right_pointer = 0  # We're starting from the very beginning

    # This loop handles most elements, getting added to our result one by one,
    # So, step by step we're building our perfectly sorted array
    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        else:
            result.append(right[right_pointer])
            right_pointer += 1

    # Once that's done, we still might have some elements left in either "left" or "right"
    # So, we just add all of them to the end of our result.
    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])

    return result

# Let's put our Merge Sort to the test with a list of numbers
# Make sure to replace this with your own array to see how well our algorithm performs
print(merge_sort([34, 19, 47, 542, 200, 99, 53, 8, 287, 1]))

# Have fun sorting, explorers!

