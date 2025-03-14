

# Hello fellow coder! I hope you're having a great day. This is the start of our fun adventure together as we build an exciting Queue data structure. Yay, right? 

# So first, the Queue, what is it? It's a linear structure which follows a particular order in which the operations are performed.
# The order is First In First Out (FIFO). A good example is any queue of consumers for a resource where the consumer that came first is served first.

# Let's dive in, shall we?

class Queue:
    # Here we go! This is the start of our merry Queue class.

    def __init__(self):
        # Time to initialize. We're gonna use a list to hold our queue values.
        self.queue = []

    def enqueue(self, val):
        # Ah! Now we're getting to the fun part. The enqueue operation!
        # We just add (or append) the given value at the end of the queue.
        self.queue.append(val)

    def dequeue(self):
        # Time to let the first one out! The dequeue operation.
        # But first, let's check if the queue is empty. We don't want to remove something that isn't there.
        if not self.isEmpty():
            return self.queue.pop(0)
        else:
            raise IndexError("Hey careful! The queue is empty.")

    def size(self):
        # Just returning the length of the queue. Pretty straightforward, right?
        return len(self.queue)

    def isEmpty(self):
        # Checking if the queue is empty, by comparing the size.
        return self.size() == 0

    def peek(self):
        # This is like saying "who's next in line?".
        # But again, we should check if anyone is in the line.
        if not self.isEmpty():
            return self.queue[0]
        else:
            raise IndexError("Hey there! The queue is empty.")

if __name__ == '__main__':
    # Ah! The main function. This is where we do the actual magic with our marvelous Queue class.

    my_queue = Queue()  # Instantiate the Queue class.
    my_queue.enqueue('Apple')  # Add some fruits to the queue.
    my_queue.enqueue('Banana')
    my_queue.enqueue('Mango')

    print(f"Size of the queue: {my_queue.size()}")
    print(f"First element in queue: {my_queue.peek()}")

# And that's the end of our incredible python journey together. I really hope you had as much fun as I did.
# Happy Coding ;)!


