
# Hey there fellow programmer,
# Let's dive into creating a Binary Search Tree (BST), a special kind of tree data structure.
# BST is great, because you can retrieve, insert and delete data in a pretty quick way (O(log n)).
# How cool is that, right?

class Node:
    def __init__(self, key):
        # Each node has a key and pointers to its left and right children.
        self.left = None
        self.right = None
        self.value = key

class BinarySearchTree:
    def __init__(self):
        # Our BST starts with a root Node, which is initially empty.
        self.root = None

    # Now, let's write a method to add nodes into the tree
    # Adding a value to the BST is a breeze, just follow the rules of BST.
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    # Helper Method
    def _insert(self, value, current_node):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert(value, current_node.left)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert(value, current_node.right)
        else:
            # No duplicates, please!
            print("Value already in tree!")

    # Traversal methods are coming up. It's like taking a fun walk in your BST.
    
    # Let's start with In-Order Traversal
    def in_order_traversal(self, start, traversal):
        """Left -> Root -> Right"""
        if start:
            traversal = self.in_order_traversal(start.left, traversal)
            traversal += (str(start.value) + " ")
            traversal = self.in_order_traversal(start.right, traversal)
        return traversal

    # Next, Pre-Order Traversal
    def pre_order_traversal(self, start, traversal):
        """Root -> Left ->Right"""
        if start:
            traversal += (str(start.value) + " ") 
            traversal = self.pre_order_traversal(start.left, traversal)
            traversal = self.pre_order_traversal(start.right, traversal)
        return traversal

    # Finally, Post-Order Traversal
    def post_order_traversal(self, start, traversal):
        """Left -> Right -> Root"""
        if start:
            traversal = self.post_order_traversal(start.left, traversal)
            traversal = self.post_order_traversal(start.right, traversal)
            traversal += (str(start.value) + " ")
        return traversal 

    # Phew, we're done!
    # Now you have a beautiful BST with traversal methods at hand. 
    # Give yourself a pat on the back!
    
# Now, Time to test-drive our neat little Binary Search Tree

# bst = BinarySearchTree()
# numbers = [6, 4, 8, 7, 9, 2, 1, 3, 5]
# for num in numbers:
#     bst.insert(num)

# print("In-Order Traversal: ", bst.in_order_traversal(bst.root, ""))
# print("Pre-Order Traversal: ", bst.pre_order_traversal(bst.root, ""))
# print("Post-Order Traversal: ", bst.post_order_traversal(bst.root, ""))

