
# KDTree.py
# Hey there, fellow Pythonista! I'm Mr.KDTree, your friendly neighborhood k-d tree.
# You're here because you need a simple 2-D k-d tree for nearest neighbor, am I right?
# Well you've come to the right place!

class Node:
    # Nodes: The heart of our k-d tree!
    def __init__(self, point, left=None, right=None):
        self.point = point
        self.left = left
        self.right = right


class KDTree:
    # The k-d tree itself!

    def __init__(self):
        # A fresh and spiffy k-d tree needs an empty root!
        self.root = None

    def insert(self, point):
        # I love me some new points! Let's add 'em in!
        self.root = self._insert(self.root, point)

    def _insert(self, root, point, depth=0):
        # The real engine room where all the insert magic happens

        # Hit the tree bottom? Time to create a new node!
        if root is None:
            return Node(point)

        # Calculating dimension based on depth.
        # Since we are 2-D, we alternate between 0 and 1.
        dim = depth % 2

        # If point to be inserted is less than root node - go left,
        # otherwise go right.
        if point[dim] < root.point[dim]:
            root.left = self._insert(root.left, point, depth + 1)
        else:
            root.right = self._insert(root.right, point, depth + 1)

        return root

    def nearest(self, point):
        # The nearest neighbour, how exciting!
        return self._nearest(self.root, point)[1]

    def _nearest(self, root, point, depth=0, best=None):
        # The search party for the nearest neighbour!

        if root is None:
            return best

        # If we don't have a best, then the current root is the best!
        # If we DO have a best, then we check - is the root better.
        if best is None or self.distance(point, best[1].point) > self.distance(point, root.point):
            best = (self.distance(point, root.point), root)

        # Calculating dimension based on depth
        dim = depth % 2

        # Depending on dimension choose where to go.
        if point[dim] < root.point[dim]:
            best = self._nearest(root.left, point, depth+1, best)
            if best[0] > abs(root.point[dim] - point[dim]):
                best = self._nearest(root.right, point, depth+1, best)
        else:
            best = self._nearest(root.right, point, depth+1, best)
            if best[0] > abs(root.point[dim] - point[dim]):
                best = self._nearest(root.left, point, depth+1, best)
                
        return best

    def distance(self, point1, point2):
        # Distance? Just some Pythagorean magic! 
        return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5


# And there you have it folks, a delightful 2-D k-d tree for all your nearest neighbour needs!
# Remember, absolutely no feeding after midnight!