
# Hey there, fellow code enthusiast! I'm just chilling here, helping you find the middle of a LinkedList.
# Isn't life with Python just grand? 
# Let's say goodbye to the backaches that come from heavy lifting and let Python's simplicity carry the load.

# Okie dokie, let's get started on our little project.

# Firstly, I'll start with creating a node with the class name 'Node'
class Node:
    # In the constructor, I'll define 'data', for holding its data, and 'next', for pointing to the next Node
    def __init__(self, data):
        self.data = data
        self.next = None

# Now, we'll define the LinkedList class 
class LinkedList:
    # Here's our friendly LinkedList constructor. At first, it doesn't contain anything, 
    # so the head is initialized as None
    def __init__(self):
        self.head = None

    # This function is for adding new nodes at the end of the LinkedList
    def append(self, data):
        # Just in case the LinkedList is empty, we point its head to a new node 
        if not self.head:
            self.head = Node(data)
        else:
            # And when it is not empty, we make our way to the end node and add the new node there.
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    # Now, to the most exciting part! Finding the middle of a LinkedList.
    def find_middle(self):
        # We'll be running two pointers. The 'slow' one advances one node at a time,
        # while the 'fast' one advances two nodes at a time. 
        # When the 'fast' pointer reaches the end, the 'slow' pointer will be at the middle!
        slow_ptr = self.head
        fast_ptr = self.head

        # We need to make sure that the LinkedList is not empty and that the 'fast' pointer 
        # isn't pointing at None or a last node.
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        # Once it has stopped, guess where our 'slow' pointer would be?
        # Yep, you guessed it right: smack dab in the middle!
        return slow_ptr.data

# You can create a LinkedList and populate it with data as follows:
# my_list = LinkedList()
# my_list.append('data1')
# my_list.append('data2')
# Then you can find the middle by calling 'find_middle'
# print(my_list.find_middle())

