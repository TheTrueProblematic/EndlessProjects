
# Hello there, fellow programmer! I'm just a fun, happy Python script who enjoys sorting numbers. Have you ever heard of Shell Sort? Well, you're about to. Let's dive right in!

def shellSort(array):
    '''
    Shell Sort function:
    Shell Sort is a generalized version of insertion sort. It allows the exchange of items that are far apart. 
    The idea is to arrange the list of elements so that, starting anywhere, considering every hth element gives a sorted list. 
    Such a list is said to be h-sorted.
    Equivalently, it can be thought of, as h interleaved lists, each individually sorted.

    :param array: The array to be sorted 
    '''
    
    # Our gap sequence will reduce by a factor of 2 each time, starting at half the array size
    gap = len(array) // 2
    
    # We keep sorting smaller and smaller subsequences
    while gap > 0:
        for i in range(gap, len(array)):
            
            # We are always looking at two elements, current element and an element that is "gap" distance away from current element
            temp = array[i]
            j = i
            
            # The magic happens here. We shift elements of array[0...i-1], that are greater than key, to one position ahead of their current position
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap
            
            # Move temp to its correct location
            array[j] = temp
                
        # Decrement the gap size for next pass
        gap //= 2  
        
    # Ta-da! Your array is sorted. Isn't this fun?
    return array

# Let's test our glorious Shell Sort on an array of integers
print(shellSort([23, 29, 15, 19, 31, 7, 9, 5, 2]))

# Happy Coding! 😄😄😄

'''
Note: I do not use any graphical user interface(GUI). I'm a command-line interface(CLI) based python script.
I do not depend on any third-party libraries. I'm built with pure python, making me robust and platform agnostic. 
I do not use the internet or any APIs whatsoever. My sole purpose on this digital planet is to sort lists for you in a fun, enjoyable way!
'''

