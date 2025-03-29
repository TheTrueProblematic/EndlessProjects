# First of all, let's make sure that we have our happy programmer mode on! 😎
# Importing the Queue module to help with our job of creating the stack☀️
from queue import Queue 

# And here we go, let's define our classy class "StackWithQueues" 🚀
class StackWithQueues:
    def __init__(self):
        """
        Here we initialize our "StackWithQueues" class.
        We use two different queues "_queue" and "temp" to create our stack
        """ 
        self._queue = Queue()
        self._temp = Queue()

    # Let's add an element to our stack now
    def push(self, item):
        """
        A function to add an element(item) to our Stack.
        For each insert operation, we empty the main queue and push everything into the temp queue,
        Then we add the new item into the main queue and return everything back from the temp queue.
        Preety smart, huh? 😁
        """
        while not self._queue.empty():
            self._temp.put(self._queue.get())
        
        self._queue.put(item)

        while not self._temp.empty():
            self._queue.put(self._temp.get())

    # Now it's time to implement a function to remove an element from top of the stack... tada 🥳
    def pop(self):
        """
        A function to remove an element from our Stack.
        Again the main idea is to dequeue an item from the main queue, just like a normal queue operation.
        """
        if self._queue.empty():
            return "Oh, oh! It seems our Stack is empty!"
        return self._queue.get()

    # Lastly a peek function to see what's at the top of our awesome stack! 😇
    def peek(self):
        """
        A function to get the top item of the Stack.
        Hey, but we don't wanna remove it yet!
        """
        if not self._queue.empty():
            return self._queue.queue[0]
        return "Oh, oh! It seems our Stack is empty!"

    # And of course we should know when our stack is empty. 😬
    def empty(self):
        """
        A function to check if our Stack is empty or not.
        Returns True if empty, False otherwise.
        """
        return self._queue.empty()

# Oh well, that's it for now! Using two queues we have created our wonderful stack! 🎉
# Isn't programming fun? Keep coding, keep smiling! 😊