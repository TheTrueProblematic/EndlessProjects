
# Hey there happy coder! 😄
# Don't you love efficient data structures!?
# Let's jump into it by creating our own Circular Queue in Python.

class CircularQueue:

    def __init__(self, k: int):
        '''
        Initialize a circular queue data structure with fixed size 'k'
        '''
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    def enqueue(self, data):
        '''
        Add an item to the queue. 
        If the queue is full, print a friendly message! 😁
        '''
        if ((self.tail + 1) % self.k == self.head):  
            print("Circular Queue is full\n") 

        elif (self.head == -1): 
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else: 
            self.tail = (self.tail + 1) % self.k 
            self.queue[self.tail] = data

    def dequeue(self):
        '''
        Remove an item from the queue.
        If the queue is empty, print a friendly message! 😁
        '''
        if (self.head == -1): 
            print("Circular Queue is empty\n") 

        elif (self.head == self.tail): 
            temp = self.queue[self.head] 
            self.head = -1
            self.tail = -1
            return temp
        else: 
            temp = self.queue[self.head] 
            self.head = (self.head + 1) % self.k 
            return temp

    def display(self): 
        ''' 
        Nicely display the queue! 😍
        If queue is empty, let's print it out!
        '''
        if(self.head == -1): 
            print("No element in the Circular Queue") 

        elif (self.tail >= self.head): 
            for i in range(self.head, self.tail + 1): 
                print(self.queue[i], end=" ") 
        else: 
            for i in range(self.head, self.k): 
                print(self.queue[i], end=" ") 
            for i in range(0, self.tail + 1): 
                print(self.queue[i], end=" ")

# And Voila! The Circular Queue data structure is ready to use!
# Isn't that just great! Python is such a fun language, isn't it! 🙌

