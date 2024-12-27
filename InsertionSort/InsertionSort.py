# Welcome to the "Insertion Sort" party, fellow coder! 🎉

# Just so you know, we're about to create an exciting 'Insertion Sort Algorithm'!

# So buckle up, and let's roll...


def insertion_sort(arr):
    # Fun Fact: Insertion sort works similar to how most people arrange a hand of poker cards! 🤯

    # We better make sure we have something to play with, so here's our range
    for i in range(1, len(arr)):

        # Let's start playing! 🃏
        key = arr[i]

        # Move elements of arr[0..i-1] that are greater 
        # than the key to one position ahead of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key


# Your array just got a mind-blowing makeover with the power of the 'Insertion Sort'

# Test it out with numbers of your choice

arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("Sorted array is:", end='\n')
for i in range(len(arr)):
    print("%d" %arr[i], end='\n')


# Wow! That was an amazing journey through the world of 'Insertion Sort'. Thanks for sticking around.

# Happy Coding! 💻