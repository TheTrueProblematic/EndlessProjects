
# Hey there, terrific programmer! If you're here, it means you too are interested in the magic of Doubly Linked Lists. Cool Beans!
# So, let's get ready to dive right into it. We're going to implement a DoublyLinkedList that will help you store values and navigate them back and forth. Yes, just like time travel!

# First things first, we will start with creating our Node class.

class Node:
    def __init__(self, data=None):
        # Each node has a value, and pointers to the next and the previous node.
        self.data = data
        self.next = None
        self.prev = None

# Now that we're done with Node, let's move on to the big boss, our DoublyLinkedList!

class DoublyLinkedList:
    def __init__(self):
        # A DoublyLinkedList starts with a sentinel or 'head' Node that does not contain any data.
        self.head = Node()

    # Let's create a method to add elements to our list. We like our data, don't we?
    def append(self, data):
        # Step 1: Create a new node with data
        new_node = Node(data)
        # Step 2: Pointers' magic time! We start at the head.
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
        # Make current last node point to this new node and vice versa
        cur_node.next = new_node
        new_node.prev = cur_node

    # But we are flexible and we should be able to remove some data too. So, let's create a method to remove a node.
    def delete(self, data):
        # Once again, we start at the head.
        cur_node = self.head
        while cur_node.next is not None:
            # If we found the node we are looking for, let's bypass it in our list.
            if cur_node.next.data == data:
                cur_node.next = cur_node.next.next
                cur_node.next.prev = cur_node
            cur_node = cur_node.next

    # Now, wouldn't it be nice to visualize our list? Let's make a function that prints our list beautifully.
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

# And voila! You've got yourself a neat doubly linked list. Hooray for data structures! Go out there and have fun with it!

