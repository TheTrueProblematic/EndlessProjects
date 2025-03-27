
# Hey there, happy programmer! Today, we are diving into a fun adventure: implementing a singly linked list in Python. 
# No worries though, as it's simpler than it sounds. So, let's buckle up and start our journey!

# First, let's define our Node class. This will represent an individual item in our linked list.
# Each node will hold some data and also keep track of the next node in the list. 
# If there's no next node, it means this node is the last one in the list!
class Node:
    def __init__(self, data=None):
        self.data = data  # Let's store our data here
        self.next = None  # And keep the pointer to the next node here. None indicates the end of the list! 


# Alright, Node class is set! Now, it's time for the main act: Our LinkedList class!
class LinkedList:
    def __init__(self):
        self.head = None  # When created, our list is empty, so head is None!

    # Alright, our linked list is pretty lonely, so let's add method to add nodes!
    def append(self, data):
        if not self.head:  # If list is empty
            self.head = Node(data)  # Create a new node and set it as the head
        else:  # If list is not empty
            current = self.head  # Start at head
            while current.next:  # Traverse to the end of the list
                current = current.next
            current.next = Node(data)  # Create a new node and set it as the next of the last node

    # I know you're having fun, but let's add some functionality to remove nodes as well!
    def remove(self, data):
        if self.head is None:  # If list is empty, nothing to remove
            return
        if self.head.data == data:  # If the head node is the one to be removed
            self.head = self.head.next  # Just change head pointer to the next node
            return
        else:  # If the node to be removed is not the head
            current = self.head
            while current.next:  # Traverse the list
                if current.next.data == data:  # Found the node we're looking for!
                    current.next = current.next.next  # Modify the pointer to skip the unwanted node
                    return 
                current = current.next  # Move on to the next node

    # And, of course, we want to see our creation! So, let's add a method to print the entire list.
    def print_list(self):
        node = self.head
        while node:  # Traverse the list
            print(node.data)  # Print the data of each node
            node = node.next  # Move on to the next node

# Woohoo! All done! You've successfully implemented a basic singly linked list in python!
# Now you can go create, append and remove nodes to your heart's content.
# Great job, keep coding and have fun!


