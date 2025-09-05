
# Hello there, happy coder! Ready to dive into a exciting sorting adventure? Buckle up! 
# Today, we'll be implementing the Bitonic Sort Algorithm in pure Python, no distractions or dependencies, just fun all the way!

# First of all, Bitonic sort is one of those 'cool' algorithms, you know? It sorts in a binary order: half of the array will go up and the other goes down.

# Lets' start together on this fun journey, Get your fingers ready on the keyboard, and let's rock!

# The first thing we need to do is create the compare function.
def compare(arr, i, j, dir):
    """Compare and swaps elements if required.
    
    Args:
        arr : input array
        i : first index
        j : second index
        dir : direction, can be 0 or 1
    """
    # Here, we do a playful little inspection: if the direction matches the elements' relationship, let's swap 'em!
    if (arr[i] > arr[j]) == dir:
        arr[i], arr[j] = arr[j], arr[i]  # Just switching places, really!

# Now we'll write the bitonic_merge function.
def bitonic_merge(arr, low, cnt, dir):
    """Performs bitonic merge.
    
    Args:
        arr : input array
        low : starting index
        cnt : count
        dir : direction
    """
    # Do you know what they say about too small? Yeah, it isn't worth the effort.
    if cnt > 1:
        # Find the middle point, splitting is fun! 
        k = int(cnt/2)
        for i in range(low, low+k):
            # Comparing the elements, a casual check-up, you could say.
            compare(arr, i, i+k, dir)
        # Recurse for the first and second halves
        bitonic_merge(arr, low, k, dir)
        bitonic_merge(arr, low+k, k, dir)

# Let's write the bitonic_sort function.
def bitonic_sort(arr, low, cnt, dir):
    """Performs bitonic sort by recursively calling itself and bitonic_merge.
    
    Args:
        arr : input array
        low : starting index
        cnt : count
        dir : direction
    """
    # Again, count mustn't be too small! 
    if cnt > 1:
        # Find middle point.
        mid = int(cnt/2)
        # Recursively sort the first half, sending it upwards! 
        bitonic_sort(arr, low, mid, 1)
        # And, the second half goes down the hill.
        bitonic_sort(arr, low+mid, mid, 0)
        # And now, my friend, it’s merging time. 
        bitonic_merge(arr, low, cnt, dir)

# Finally, let's write main_sort function that starts it all off.
def main_sort(arr, n, up):
    """Starts off the sorting process.
    
    Args:
        arr : input array
        n : length of the array
        up : direction
    """
    # Call the main bitonic_sort function.
    bitonic_sort(arr, 0, n, up)

# Alright, we've done it! Let's take our brand new shiny algorithm out for a spin!

# We're just testing it here with a random array. Feel free to update this with any array you like!
data = [3, 7, 4, 8, 6, 2, 1, 5]
n = len(data)
up = 1

# We'll start the sorting process. Get ready! 
main_sort(data, n, up)
# And let's print the sorted data because hey, it’s always nice to see your work paying off, isn’t it?
print ("%s" %' '.join(map(str, data)))
# Order is restored! Beautiful, isn't it? Hope you enjoyed this just as much as I did! Keep coding and stay happy!

