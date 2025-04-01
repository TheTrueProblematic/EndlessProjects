
# Hello, beautiful people! 😄 Let's get started on an exciting journey of code.
# This script is something you'd love to use if you need to merge overlapping intervals in a list of intervals.

# I am written in Python, no GUIs, no APIs, no dependencies, and no internet access.
# Just pure, simple, and elegant Python. Whip me out anywhere, anytime; I am cross-platform compatible.
# Onward, to infinity and beyond! 🚀

def merge_intervals(arr):
    # Step 1: We sort the array, so overlapping intervals become neighbors
    arr.sort(key = lambda i: i[0])

    # Step 2: Initialize merged list with first interval from the sorted array
    merged = [arr[0]]

    # Step 3: Traverse through the rest of the sorted array, making magic happen
    for current in arr:
        # If the current interval in the sorted array overlaps with the last interval in the merged list
        # we merge them, creating a bigger interval. Now, that's higher-level thinking! 😉
        if current[0] <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], current[1]))
        else:
            # Else, there's no scope for merging; we add the current interval to the merged list
            merged.append(current)

    # Voila! Return the merged list of intervals! 🎉
    return merged

def main():
    # Let's test this on a list of intervals: feel free to change the array as per your need!
    arr = [(1, 4), (2, 5), (7, 9), (8, 10)]

    # Intervals before merging
    print("Intervals before merging: ", arr)

    # Merge those intervals!
    merged = merge_intervals(arr)

    # And... here's the result!
    print("Intervals after merging: ", merged)

# Run the main function when this script is run
if __name__ == '__main__':
    main()

# And with this, we bid adieu! Thanks for accompanying me on this fantastic journey of code.
# Until next time, sayonara! 🖐😊
