
# Hello, savvy programmers, the fun is just getting started!
# Today we're gonna whip up a basic priority queue - just in python!

# Let's kick things off by defining a class, shall we?

class PriorityQueue:
    """This class will create a new priority queue."""
    def __init__(self):
        # Here we are creating a list to hold all our queue elements.
        self.queue = []

    # Displaying elements of remaining queue  
    def display(self):
        """This will print out the current queue."""
        print("Our current queue: ", self.queue)

    # Inserting elements
    def insert(self, data):
        """This inserts the specified data at the correct point in the queue."""
        # First, we need to check if our queue is empty.
        # If it is, we'll just add this element to the queue.
        if self.size() == 0:
            self.queue.append(data)
        else:
            # If our queue isn't empty, we need to determine where to put this element.
            # To do this, we iterate through the queue until we find an element that is larger than the one we're adding.
            for x in range(0, self.size()):
                if data >= self.queue[x]:
                    # if the element in queue is greater, we insert data
                    self.queue.insert(x, data)
                    return
            # if we make it through the whole queue and the element we're adding is smaller than everything, we appened it to end
            self.queue.insert(self.size(), data)

    # Deleting an element
    def delete(self, data):
        """This deletes the specified data from the queue."""
        # First, we need to check if our queue is empty.
        # If it is, then we obviously can't delete anything!
        if self.size() == 0:
            return ("Underflow!")
        else:
            # If our queue isn't empty, then we look through it for the element we want to delete.
            for k in range(0, self.size()):
                if data == self.queue[k]:
                    self.queue.remove(data)
                    return ("Removed!")

            # if the data is not found
            return("data not found")

    def size(self):
        """This gets the size of the queue."""
        # Just returns the length of our queue list.
        return len(self.queue)

# Well, isn't that nice and simple? All this code does is create a priority queue.
# The elements with higher value are considered higher priority. So in our case,
# we insert the higher values in the beginning.

# PS: Remember, Python is happy to help and so am I!
