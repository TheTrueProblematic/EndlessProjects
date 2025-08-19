
# Hey there happy programmers! Today we're creating a class for something super exciting - segment trees, yep!
# Segment Trees are the perfect data structure to solve various range query problems in logarithmic time, pretty awesome huh?
class SegmentTree:
    def __init__(self, data):
        # We're setting up our tree. To make the tree construction easier, we're gonna use a Python list
        # Let's initialise it with a size of 4 times the length of the data array.
        self.tree = [0] * (4 * len(data))
        self.data = data
        self.build_tree(0, 0, len(data) - 1)

    def build_tree(self, node, start, end):
        # This is where the fun begins! We're building our tree here.
        if start == end:
            # In case of leaf node, copy the array content
            self.tree[node] = self.data[start]
        else:
            # Find mid point and recursively build tree for the two halves
            mid = (start + end) // 2
            self.build_tree(2 * node + 1, start, mid)
            self.build_tree(2 * node + 2, mid + 1, end)
            # Assign data to the parent node (generally a function of the child data)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query(self, node, start, end, l, r):
        # Now we're setting up to handle those pesky range queries!
        if r < start or end < l:
            # If range is completely outside the node's range, return appropriate value (for sum it would be 0)
            return 0
        elif l <= start and end <= r:
            # If range is within the node's range, return the node's value
            return self.tree[node]
        else:
            # If neither, meaning the range partially overlaps, we compute for both halves.
            mid = (start + end) // 2
            p1 = self.query(2 * node + 1, start, mid, l, r)
            p2 = self.query(2 * node + 2, mid + 1, end, l, r)
            return p1 + p2
 
   