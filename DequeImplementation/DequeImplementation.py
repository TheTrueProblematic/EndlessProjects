
# Hey there, fellow coder! Get ready to dive into some cool Python magic.
# We're about to implement our very own Deque, a.k.a Double-Ended Queue!

# Let's get started!

class Deque:
    
    # We'll start by initializing our Deque. At this point, it's just an empty list.
    def __init__(self):
        '''Initialize an empty Deque.'''
        self.items = []

    # Let's add some functionality to our Deque. First up: adding items to the front!
    def add_front(self, item):
        '''Add an item to the front of the Deque.'''
        self.items.append(item)

    # Now, let's add an item to the back of the Deque.
    def add_rear(self, item):
        '''Add an item to the rear of the Deque.'''
        self.items.insert(0, item)

    # Making a Deque is no fun if we can't remove items as well. Let's remove from the front...
    def remove_front(self):
        '''Remove an item from the front of the Deque.'''
        if self.isEmpty():
            return None
        else:
            return self.items.pop()

    # ...and also from the rear. Double the ends, double the fun!
    def remove_rear(self):
        '''Remove an item from the rear of the Deque.'''
        if self.isEmpty():
            return None
        else:
            return self.items.pop(0)

    # Sometimes, it's useful to know if our Deque is lonely (empty). So let's add that functionality as well.
    def isEmpty(self):
        '''Check if the Deque is empty.'''
        return self.items == []

    # And of course, it's always good to know how big our Deque is. Let's make that possible.
    def size(self):
        '''Return the size of the Deque.'''
        return len(self.items)

# That's it! We're done here. You now have a fully functional Deque at your disposal. 
# Keep on coding and have a great day! Cheers!


