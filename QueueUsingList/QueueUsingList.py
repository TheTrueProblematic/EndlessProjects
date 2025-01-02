
# Hey there happy coders! Welcome aboard on our journey to create a Queue using a simple list in python. 
# It's going to be loads of fun and at the end of it, we'll have our very own queue data structure. 
# All we need is good old python, and a penchant for data structures! So, let's dive in!

class Queue:
    def __init__(self):
        # How exciting! We're setting up our Queue. 
        # Think of this as an empty line at the start of a rock concert. 
        # Let's get the party started!
        self.queue = list()

    def enqueue(self, item):
        # Woah an enqueue operation! Sounds complicated? Don't you worry. 
        # Enqueue is just a fancy term for adding an item to our queue. 
        # It's just like a new person joining our line at the concert. Rock on!
        self.queue.append(item)

    def dequeue(self):
        # Time for the dequeue operation! Again, don't let the fancy words scare you. 
        # Dequeue is just our way of saying, "Hey, your turn to enter the concert!".
        # So we remove an item from the head of our queue.
        # But we have to make sure there actually is someone in line!
        if len(self.queue) < 1:
            # Looks like the line is empty!
            return None
        # Time for the front of the line to enter the concert! Rock on!
        return self.queue.pop(0)

    def display(self):
        # Say we want to take a look at our queue. 
        # Maybe we want to see who's next or how many people are in line
        # The display function does that as it provides a nice view of our entire queue. 
        # Let's see what we've got!
        return self.queue

    def size(self):
        # And last but not the least, size lets us know how many elements are in our Queue. 
        # Just like counting the number of people in line at our concert!
        return len(self.queue)

# And just like that, we've created a Queue data structure in python! You've been amazing and I hope you've had as much fun as I've had. Until next time, Happy Coding!

