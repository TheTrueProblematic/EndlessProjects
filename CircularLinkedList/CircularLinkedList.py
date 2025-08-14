
# Ahoy there, fellow programmers! Let's dive into python and swim across the circular linked list sea together!

class Node:
    # This is our brave little Node class. Each one full of hope and a pointer to the next node.
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    # On to the main vessel, the CircularLinkedList ship. Where each node is a brave sailor, and the last one always points to the first.

    def __init__(self):
        self.head = None # What's a ship without a Captain(head)? Empty initially, but not for long.

    def append(self, data):
        # This handy little mate is used to add a new sailor(node) to the ship.

        if not self.head:
            # If the ship is empty, the new node will be the captain.
            self.head = Node(data)
            self.head.next = self.head
        else:
            # And if not, it just becomes one of the crew.
            new_node = Node(data)
            curr_node = self.head
            while curr_node.next != self.head:
                curr_node = curr_node.next
            curr_node.next = new_node
            new_node.next = self.head

    def print_list(self):
        # This function is the ships spyglass. It helps to look through all the sailors in the ship.

        curr_node = self.head

        while True: # Time to go around the ship!
            print(curr_node.data)
            curr_node = curr_node.next
            if curr_node == self.head:
                break

# Code ahoy! Let's put our ship in the water.

clr = CircularLinkedList()
clr.append('Sailor 1') # Adding our first sailor
clr.append('Sailor 2') # Adding second sailor
clr.append('Sailor 3') # And a third!

clr.print_list() # Time to meet the crew!

# Have fun sailing through the circular linked list seas!
# And remember to keep coding!

