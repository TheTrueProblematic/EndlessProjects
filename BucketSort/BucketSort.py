
# Hello, fellow coder! You've stumbled upon my fantastic BucketSort script! Buckle up, because we're about to dive into the magical world of Python coding.

# First, let's get a little formal and define our very own BucketSort class.

class BucketSort:
    def __init__(self, bucket_size=0.1):
        # Here, we redefine the concept of a bucket, setting it as a float value!
        self.bucket_size = bucket_size

    def sort(self, numbers):
        # We're gonna need some buckets! Let's make an array to hold them.
        # And just like that, we made a whole lot of buckets by dividing 1 by the bucket size.
        buckets = [[] for _ in range(int(1 / self.bucket_size))]

        # Time to populate those buckets! Let's iterate through our numbers array
        for num in numbers:
            # Finding the proper bucket index for a floating-point number can be a bit tricky.
            # Don't worry though — with a couple of multiplications and an int casting, we've got this under control!
            index = int(num / self.bucket_size)
            buckets[index].append(num)

        # Now we've got our numbers scattered in our buckets. Let's put them back in order!
        for bucket in buckets:
            # And here we encounter the miracle of recursion! 
            # We're sorting each bucket individually using the built-in Python sort function.
            bucket.sort()
            
        # We're almost done! Time to gather up those sorted numbers from each bucket and return them.
        sorted_numbers = []
        for bucket in buckets:
            sorted_numbers.extend(bucket)
            
        return sorted_numbers

# There you have it! A fully working BucketSort class.
# Enjoy sorting floating-point numbers to your heart's content!

# Example on how to run the sort:
# bs = BucketSort()
# sorted_numbers = bs.sort([0.2, 0.1, 0.5, 0.7, 0.3, 0.6, 0.9, 0.8])

