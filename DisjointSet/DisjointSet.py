
# Hello! I'm your happy coder and today, we're going to have a blast implementing a disjoint-set, also known as a union-find data structure.
# Now, buckle up and let's dive right into it.

class DisjointSet:
    # Ah, the magic of initialization. Here, we're setting up our "forest". Each "tree" in the forest is one disjoint set.
    # The dictionary will map an item to its parent (or itself if it is the root of the tree)
    def __init__(self, items):
        self.parent = {}
        # Let's go on an adventure! For every item in our input, they start off as their own "tree"(or set).
        for item in items:
            self.parent[item] = item

    # Finding the root of a tree! We're climbing all the way up the tree to find the root.
    # We also do path compression here for efficiency. Once we find the root, 
    # we set the parent of the our item directly to the root.
    # This means the next time we search for the same item, we find the root in constant time! Smart, don't you think?
    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            self.parent[item] = self.find(self.parent[item])
            return self.parent[item]

    # Uniting two "forests" (or in other words, doing an union operation).
    # We take the root of each item's tree and simply set the parent of one root to the other. Voila!
    def union(self, item_1, item_2):
        root_1 = self.find(item_1)
        root_2 = self.find(item_2)
        if root_1 != root_2:
            self.parent[root_1] = root_2

# Alrighty, there we have it folks! A gleaming, efficient, and oh-so-useful disjoint-set data structure.
# No trees were harmed in the coding of this utility. :)
# Now, go forward and create exciting applications using the power of disjoint-sets! Happy coding!

