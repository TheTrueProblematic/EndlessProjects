
# Greetings! Welcome to the fantastic world of coding! Today, we are going to treat ourselves with a magical data structure called 'Fenwick Tree' or a 'Binary Indexed Tree'.
# Fenwick tree is quite a fabulous concept, working on our mundane task of computing prefix sums with such beautiful skill and grace!

class FenwickTree:

    def __init__(self, size):
        # Hocus pocus! Let's first create an array of zeroes of a particular size.
        self.size = size
        self.tree = [0]*(size + 1)  # Remember, we Pythonistas count starting from 0!

    def update(self, index, val):
        # Abracadabra! Let's add a value to a particular index.
        # We add the value to the right elements by using bitwise operations (like magic!).

        while index <= self.size:
            self.tree[index] += val
            index += index & -index

    def prefix_sum(self, index):
        # Voila! We return the sum of the prefix with the help of the magical 'prefix_sum' function.
        # We fetch the right elements, add them up using bitwise operations till we reach 0.

        result = 0
        while index:
            result += self.tree[index]
            index -= index & -index
        
        # And here's your trick – the prefix sum!
        return result

# Now, let's take out this magical wand (or Fenwick tree, let's not mince words) for a little swirl!

# Initialize the tree to a convenient size (maybe the length of your array?)
fen_tree = FenwickTree(10)

# Time for some magic! Update our tree with values at different positions!
fen_tree.update(1, 3)
fen_tree.update(2, 4)
fen_tree.update(3, 5)
fen_tree.update(4, 6)
fen_tree.update(5, 7)

# Let's compute the prefix sum up to different indices!
print(fen_tree.prefix_sum(1))  # Poof! It's 3 (3)!
print(fen_tree.prefix_sum(2))  # Poof! It's 7 (3 + 4)!
print(fen_tree.prefix_sum(3))  # Poof! It's 12 (3 + 4 + 5)!
print(fen_tree.prefix_sum(4))  # Poof! It's 18 (3 + 4 + 5 + 6)!
print(fen_tree.prefix_sum(5))  # Poof! It's 25 (3 + 4 + 5 + 6 + 7)!

# Isn't it spellbinding when your code works exactly as planned? This is our Fenwick tree, short and sweet, making prefix sums a breeze!
# Happy Coding!


