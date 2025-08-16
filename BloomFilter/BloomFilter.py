
# Well hello there, happy programmer! Today we're going to have some fun with a data structure called a Bloom Filter.
# Our bloom filter is a super simple one, with built-in hash functions. No fluff, no frills.
# If you're not familiar with Bloom filters, they're a bit like a set, but with a fun twist.
# They can tell you if an item is possibly in the set, or definitely not in the set.
# In other words, a Bloom filter trades a bit of accuracy for big savings in memory and lookup times.
# (Ever wanted to be Indiana Jones, exploring data structures? Now's your chance!)
# And because we're keen on clean, green programming, we're going all-natural... No dependencies, not even an internet connection!
# So strap on your boots... We're diving in!

class BloomFilter:
    def __init__(self, size, hash_count):
        # Here we're initializing the filter; size is the number of bits in the array, and hash_count is the number of hash functions.
        # Think of the filter as a wide-open field, ready for us to plant some data flowers. 🌸
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0]*self.size

    def add(self, item):
        # This is where we add an item to the Bloom filter.
        # We'll run our item through each hash function, get the result and set the corresponding bit to 1.
        # It's basically like we're planting a flower in our data field!
        for i in range(self.hash_count):
            index = hash("{}{}".format(item,i)) % self.size
            self.bit_array[index] = 1

    def lookup(self, item):
        # Now we want to see if a given item is in our Bloom filter. It works similarly to adding an item.
        # We run our item through the hash functions. If any bit is 0, we know for sure it's not in the set. 
        # If all are 1, it might be in the set or it could be a false positive.
        # It's like looking for a specific flower in our field. If we can't find it, it's definitely not there. If we do...
        # Well, it might be our flower, or it might be a look-alike!
        for i in range(self.hash_count):
            index = hash("{}{}".format(item,i)) % self.size
            if self.bit_array[index] == 0: 
                return False
        return True

# Alright, we're all set! Your Bloom filter is ready to rock and roll, no outside help, no internet, 
# Just pure Python awesomeness! 🐍
# You've been a great assistant on this coding adventure!
# Until next time, happy coding~ 🚀


