
# Hey there! Let's conduct a counting sort on integer arrays!
# It's a fun way to sort arrays with only non-negative integer values. Why? Because it's super efficient!
# Let's dive in and code it together, shall we?

def counting_sort(arr):
    # Woah there! Let's create a zero-filled list which will be the same length as our input array.
    # It's will be our magic box that's going to store the sorted elements!
    output = [0 for _ in range(len(arr))]

    # We'll also need another magic box! This one's going to hold the count of individual numbers present in our input array.
    count = [0 for _ in range(256)] 
    
    # Let's take a joy ride through our input array and update our magic box (count array) accordingly!
    for num in arr:
        count[num] += 1

    # Now that we're done with our joy ride. Let's do some magic with our count array.
    # We'll modify the count array such that each element at each index stores the sum of previous counts. 
    for i in range(1, 256):
        count[i] += count[i - 1]

    # Hurray! We're now ready to place our numbers in the output array in a sorted manner!
    # What's more fun than going backwards through our array? That's right! Nothing! Let's do it!
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    # We're almost there! Let's copy our sorted array (output) into our input array so it gets sorted!
    for i in range(len(arr)):
        arr[i] = output[i]

    # Why are we returning you ask? Oh, just for the fun of it!
    return arr

# And that's a wrap folks! We've implemented the counting sort algorithm!
# Please, please, PLEASE don't forget to bring some non-negative integers to the party when you run this function!
# Happy sorting!

