
# Hello fellow coder, welcome to this slice of Python code making.
# We're building a Radix sort for non-negative numbers, how cool is that!

# Breathe in, breathe out. Let's start coding ...

def counting_sort(arr, exp1):

    # creating output array which will hold the sortd array 
    output = [0 for i in range(len(arr))]

    # initialize count array as 0
    count = [0 for i in range(10)]
    
    # computes individual digits 
    for i in range(len(arr)):
        index = arr[i] // exp1
        count[int((index) % 10)] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = len(arr) - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[(index % 10)] - 1] = arr[i]
        count[int((index) % 10)] -= 1
        i -= 1

    # Copying the output array to arr[], so that arr now
    # contains sorted numbers
    for i in range(len(arr)):
        arr[i] = output[i]

def radix_sort(arr):

    # Find maximum number to know number of digits
    max1 = max(arr)

    # Do counting sort for every digit. Note that
    # instead of passing digit number, exp is passed. exp
    # is 10^i where i is the current digit number
    exp = 1
    while max1 / exp > 0:
        counting_sort(arr, exp)
        exp *= 10

print("\n\n Yay! Now let's test this bad boy out. Sending in a random array [170, 45, 75, 90, 802, 24, 2, 66]")
arr = [170, 45, 75, 90, 802, 24, 2, 66]
# BOOM! Our Radix Sort is called now
radix_sort(arr)
# Let's print the successful results
for i in range(len(arr)):
    print(arr[i], end=" ")

# That's it, folks! Radix sort, right under your fingertips.
# Remember, practice makes perfect! Happy Coding! 😀

