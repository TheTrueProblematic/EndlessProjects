
# QuickSort.py
# --------------------------------------------------------------------------
# Hello there, happy coder! Welcome to our fun and exciting QuickSort program.
# Quicksort, as you may know, is an efficient sorting algorithm that follows
# the divide-and-conquer methodology. It works by choosing a 'pivot' element
# from the array and partitioning the other elements into two sub-arrays,
# according to whether they are less than or greater than the pivot.
# --------------------------------------------------------------------------

def quick_sort(arr):
    """
    This function takes a list of elements and sorts them in ascending order using quicksort
    """
    # If input list is of 1 or 0 elements, just return it. It's already sorted. Yay!
    if len(arr) <= 1:
        return arr
    else:
        # We're making the first element as pivot, because why not? It's fun to be first!
        pivot = arr[0]
        # This will hold elements less than pivot. They're all on team 'Less'.
        less = [x for x in arr[1:] if x <= pivot]
        # This will hold all elements greater than pivot, the 'Greater' team!
        greater = [x for x in arr[1:] if x > pivot]
        # Now, we sort both less and greater arrays and combine them with pivot in between. Partition magic!
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Test the quicksort function with a list of numbers. Change it to see the magic happen!
print(quick_sort([12,4,5,6,7,3,1,15]))
# Voila, your list is sorted. Coding is fun, isn't it? Cheers! Happy coding!!
