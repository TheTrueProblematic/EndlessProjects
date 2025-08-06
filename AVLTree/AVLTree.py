
# Hello everyone! Let's build an awesome AVL Tree in Python because coding is fun, isn't it? 
# This will be our own self-balancing binary search tree. Excited? Let's dive in!

class Node:
    """Hey, what's a tree without some nodes, right?"""
    def __init__(self, key):
        self.key  = key
        self.left   = None
        self.right  = None
        self.height = 1

class AVLTree:
    """This is our main AVLTree class."""
    def insert_node(self, root, key):
        """Okies, time to insert nodes into our AVL Tree."""
        # Normal BST insertion.
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert_node(root.left, key)
        else:
            root.right = self.insert_node(root.right, key)

        # Let's update the height of the ancestor node.
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # Wohoo! We've inserted the node. Let's check if it turned our tree unbalanced.
        balance = self.getBalance(root)

        # Too far left. Let's make a right rotation.
        if balance > 1:
            if key < root.left.key:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        # Too far right. Make a left rotation
        if balance < -1:
            if key > root.right.key:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root

    def leftRotate(self, z):
        """Time for a left rotation!"""
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def rightRotate(self, z):
        """And now for a right rotation!"""
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def getHeight(self, root):
        """Get the height of the node."""
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        """Check if the tree is balanced."""
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def preOrder(self, root):
        """Wow, we did it! Now, let's display our AVL tree in PreOrder traversal."""
        if not root:
            return
        print("{0} ".format(root.key), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

# Cheers! Let's put our AVL tree to use.
avl_tree = AVLTree()
root = None

# Let's all shout numbers! Yeah, we're adding numbers.
nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]

for num in nums:
    root = avl_tree.insert_node(root, num)

# Time to show off our beautiful tree! 
print("Preorder Traversal of constructed AVL tree is")
avl_tree.preOrder(root)
print()

# There you go! Aren't AVL trees fascinating?
