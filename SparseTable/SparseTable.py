
# Hello there! I'm your friendly SparseTable Python script! Can't wait to dive into this coding adventure with you.
# This script is all about making range minimum queries easier and faster using a sparse table data structure.
# No fancy frills, no glitzy GUIs, just good old pure Python - let's go!

# Only the built-in Python modules for us! Who needs dependencies when you have Python's advanced features, right?
import math


class SparseTable:
    # Our Sparse Table class, the heart of the script. Let's get started on building our table!

    def __init__(self, arr):
        # To start off, we need to initialize our table with our array
        # We'll also create our sparse table here
        self.arr = arr
        self.table = self.build_table(arr)

    @staticmethod
    def build_table(arr):
        # Time to construct the table! This is where the magic happens.

        # First, we need to get the length of the array and calculate the size of the table
        n = len(arr)
        m = math.floor(math.log2(n)) + 1

        # Let's create our sparse table
        sparse_table = [[0] * m for _ in range(n)]

        # To build the table, we start with the smallest ranges and build up
        for i in range(n):
            sparse_table[i][0] = i

        j = 1

        # Begin building up our table, layer by layer, like making a delicious lasagna!
        while (1 << j) <= n:
            # Iterate over the array for the range starting at i and ending at i+2^j
            for i in range(n - (1 << j) + 1):
                if arr[sparse_table[i][j - 1]] <= arr[sparse_table[i + (1 << (j - 1))][j - 1]]:
                    sparse_table[i][j] = sparse_table[i][j - 1]
                else:
                    sparse_table[i][j] = sparse_table[i + (1 << (j - 1))][j - 1]

            j += 1

        # Return our freshly baked sparse table!
        return sparse_table

    def query(self, L, R):
        # Now that we have our table, we want to be able to query it!
        # This function returns the smallest element in the range from L to R in the array

        j = math.floor(math.log2(R - L + 1))

        if self.arr[self.table[L][j]] <= self.arr[self.table[R - (1 << j) + 1][j]]:
            return self.arr[self.table[L][j]]
        else:
            return self.arr[self.table[R - (1 << j) + 1][j]]


# And voila! We've cooked up a delightful Sparse Table script!
# Ready to be served on any platform, any time. Enjoy your number crunching!
