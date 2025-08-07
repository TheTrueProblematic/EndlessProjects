
# Hello Folks! Welcome to our really fun and exciting adventure through the land of Red-Black Trees! It's going to be a blast, hold on tight!

# So, what's a Red-Black Tree? You didn't ask, but I'm going to tell you anyway!
# It's a type of self-balancing binary search tree where each node stores an extra bit for denoting the color of the node, either red or black.
# We're just building the insert function today, but each insert causes a re-balance which is really where the magic happens.

# Let's gather our tools and set off on this exciting journey!

class Node:
    def __init__(self, data, parent=None, color='red', left=None, right=None):
        # We'll start with our data and parent node, then every new node will be initially colored 'red'.
        self.data = data
        self.parent = parent
        self.color = color
        self.left = left
        self.right = right

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None)
        self.root = self.NIL
    
    def left_rotate(self, node):
        # It's Rotate-o-clock!
        y = node.right
        node.right = y.left
        if y.left is not self.NIL:
            y.left.parent = node
        y.parent = node.parent
        if node.parent is None:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
        y.left = node
        node.parent = y

    def right_rotate(self, node):
        # And now we spin in the other direction! Weeeeeee!
        x = node.left
        node.left = x.right
        if x.right is not self.NIL:
            x.right.parent = node
        x.parent = node.parent
        if node.parent is None:
            self.root = x
        elif node == node.parent.right:
            node.parent.right = x
        else:
            node.parent.left = x
        x.right = node
        node.parent = x
    
    def balance_insert(self, node):
        # Now time for some fun balancing act, don't look down!
        while node.parent.color == 'red':
            if node.parent == node.parent.parent.right:
                uncle = node.parent.parent.left
            else:
                uncle = node.parent.parent.right

            if uncle.color == 'red':
                node.parent.color = uncle.color = 'black'
                node.parent.parent.color = 'red'
                node = node.parent.parent
            else:
                if node.parent == node.parent.parent.left:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.right_rotate(node.parent.parent)
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.left_rotate(node.parent.parent)
        self.root.color = 'black'

    def insert(self, data):
        # Alright, here goes our lovely new node, gently sliding into the tree. Woohoo!
        node = Node(data)
        node.parent = None
        node.data = data
        node.left = self.NIL
        node.right = self.NIL
        node.color = 'red'

        y = None
        x = self.root
        while x is not self.NIL:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        if node.parent is None:
            node.color = 'black'
            return

        if node.parent.parent is None:
            return

        self.balance_insert(node)

# That's all friends! You've now got a shiny, new, energetic Red-Black Tree on your hands. Handle with care!


