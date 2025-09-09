
#!/usr/bin/env python3

# Ahoy matey! Welcome aboard this joyous adventure to the mysterious land of TimSortMini. We'll be embarking on a journey 
# to take an unsorted list of "treasure" (numbers) and sort them in ascending order, using the principles of TimSort. 
# So strap on your coding boots, mate, it's going to be a great ride!

# Our first task is to create a function for our handy-dandy insertion sort. This little guy will sort small pieces of 
# our treasure (list).

def insertion_sort(array, left=0, right=None):
    if right is None: 
        right = len(array) - 1

    # Iterate over the array, comparing pairs of treasure.
    for i in range(left + 1, right + 1):
        # Grab a piece of the treasure.
        key_item = array[i]

        # Go through the sorted portion of the array and find a spot for our key_item.
        j = i - 1
        while j >= left and array[j] > key_item:
            # Shuffle the pieces of treasure to the right for our key_item.
            array[j + 1] = array[j]
            j -= 1

        # Found a spot! Place our key_item here.
        array[j + 1] = key_item
    return array

# Ah, the merge function! This is where we combine our sorted treasures together.

def merge(left, right):
    # If we hit an empty treasure chest(left or right is empty), return the other one.
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    # Let's do this till we've sorted all the elements.
    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        # If we've add all of the elements of one of the lists to our result.
        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result

# And finally, our leading star - timsort! This function rolls everything we've done together.

def timsort(array):
    min_run = 32
    n = len(array)

    # Sort the elements using insertion_sort.
    for i in range(0, n, min_run):
        insertion_sort(array, i, min((i + min_run - 1), n - 1))

    size = min_run
    while size < n:
        # Merge the sublists.
        for start in range(0, n, size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n-1))

            left = array[start:midpoint + 1]
            right = array[midpoint + 1:end + 1]
            array[start:start + len(left) + len(right)] = merge(left, right)

        # Double the size of the sorted sublist.
        size *= 2

    # Ta-da! We've sorted the treasure!
    return array

# Testing our superb TimSortMini with a lousy unsorted list.
unsorted_list = [85, 24, 63, 45, 17, 31, 96, 50]
print(timsort(unsorted_list))
