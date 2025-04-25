
#-----------------------------------------
# Hey there traveller of code! 
# Here we are on an exciting adventure, where we are exploring one of the coolest data structures - The Deque!
# Deques are just like queues, but’s more chill! You can insert and remove elements from both ends, hence the name.
# You can essentially look at it as a line in your favorite fast food place but where people can join and leave from both ends! Neat, isn’t it?
# This Deque is going to be a basic one, but it would work perfectly. And remember, Great things have small beginnings!
# Buckle up, we are diving into code!
#-----------------------------------------

class Deque:
    #-----------------------------------------
    # Our Deque is born here! It's empty when it starts, but don't worry, it will hold some amazing data soon.
    #-----------------------------------------
    def __init__(self):
        self.items = []

    #-----------------------------------------
    # Is our deque lonely? This snippet checks if there are any friends (data) in our deque
    #-----------------------------------------
    def isEmpty(self):
        return self.items == []

    #-----------------------------------------
    # Let’s welcome a new friend (data) at the rear of our deque!
    # And just like a cermony, the 'append' function is doing the welcoming part.
    #-----------------------------------------
    def addRear(self, item):
        self.items.append(item)

    #-----------------------------------------
    # Well, deque also loves surprising people. So, here we are, welcoming a new guest (data) at the front of our deque!
    #-----------------------------------------
    def addFront(self, item):
        self.items.insert(0, item)

    #-----------------------------------------
    # It’s time to say goodbye :( . This code snippet let’s a friend(data) leave from the front of our deque!
    # See, deque is more flexible than we thought!
    #-----------------------------------------
    def removeFront(self):
        return self.items.pop(0)

    #-----------------------------------------
    # Our deque is flexible both ways! It can also say goodbye to a friend(data) from the rear!
    #-----------------------------------------
    def removeRear(self):
        return self.items.pop()

    #-----------------------------------------
    # Want to know how many friends (data) our deque has? This little code is our mini census for deque.
    #-----------------------------------------
    def size(self):
        return len(self.items)

#-----------------------------------------
# And voila! Our deque is ready! Skrrt Skrrt
# Now you can go on an adventure of your own with this sweet deque! 
# It will keep your data organized like a small but efficient library of Alexandria!
# Keep Coding!
#-----------------------------------------
