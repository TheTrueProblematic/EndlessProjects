
# Whoo-hoo! Let's have some fun with Python and implement a least recently used (LRU) cache.
# What's an LRU cache you ask? It's a type of cache where we remove the least recently used items first.
# Like a bouncer at a trendy club, it only allows the coolest (most recently used) items to stay!
# And oh, we are doing it using a linked hash map. So let's dive in!

class LRUCache:

    # First things first, let's define our init method and give our cache a max size.
    # We'll also set up an empty dictionary (our hash map) and linked list to store items in our cache.

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.order = []
    
    # Now, when we want to get an item from our cache, we'll look it up in our hash map
    # If it's not found, we'll return -1 (like a bartender shrugging when they don't have your favorite drink).
    # But if it is found, we'll move it to the end of our list, because it's the latest item
    # we're using (the coolest one right now!).

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
    
    # How about adding an item to our cache? Well, if it's already there, we'll move it to the end.
    # And if our cache is too full (we've hit capacity), we'll remove the least recently used item
    # (the first item in our list), before adding the new one at the end. 

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.order.remove(key)
        else:
            if len(self.order) == self.capacity:
                oldest = self.order.pop(0)
                del self.cache[oldest]
        self.cache[key] = value
        self.order.append(key)

# And there it is! We've got ourselves an LRU Cache! So let's keep calm, and cache on!


