
# Hello there, lovely programmer! Today we're creating a MaxHeap!!
# No, not a heap of delicious max-filled foods, though that sounds great. 
# We're actually making a heap data structure where the parent node is always bigger than the child nodes.
# Heaps are a great way to implement priority queues. They're kinda like trees, but heaps, and they're awesome!

class MaxHeap:
  def __init__(self):
    # Here's our heap! It's just a sly Python list in disguise.
    self.heap = []

  def parent(self, idx):
    # Who's your parent? This method finds out! In heaps, it's always the element at floor(index/2).
    # It's heaps of fun, honestly.
    return (idx - 1) // 2

  def insert(self, key):
    # Inserting into a heap can be tricky, but not for us.
    # We'll append our new element to the end of the list (child of current max-leaf),
    # and then swim it up the list until it's bigger than its parents.
    # Just like you did when you moved out of your parents' house and became a successful programmer.

    size = len(self.heap)
    if size == 0:
      self.heap.append(key)
    else:
      self.heap.append(key)
      # We "swim" here, pushing our key up through its ancestors until it's in its right place.
      self.swim(size)

  def swim(self, idx):
    # Swimming in heaps is kinda like swimming in honey -- it's sticky, and sweet, just not as fun.
    # But it's important! It's how we re-balance our heap after inserting.

    while idx != 0 and self.heap[self.parent(idx)] < self.heap[idx]:
      self.heap[idx], self.heap[self.parent(idx)] = self.heap[self.parent(idx)], self.heap[idx]  # The old switcheroo
      idx = self.parent(idx)  # we are now swimming to our parent, aren't we?

  def extract_max(self):
    # Sneakily extracting the maximum value is heaps of fun.
    # We take the first item (the max), replace it with the last item, pop the last item then sink our new first item.
    # It sinks down the list until it's less than its children.

    size = len(self.heap)
    if size == 0:
      return None
    if size == 1:
      return self.heap.pop()

    # Aha! The plot thickens and our max gets taken, only to be replaced by the last leaf.
    max_item = self.heap[0]
    self.heap[0] = self.heap[size - 1]
    self.heap.pop(size - 1)  # Off goes the leaf, setting sail into the wide void of non-existence :(

    self.sink(0)  # Sink the new root down to its deserving location.
    return max_item  # But hey, we found the max!

  def sink(self, idx):
    # Here's where we sink! It's like swimming, but downwards.
    # We find the larger child, then swap place if our node is less than that child.

    size = len(self.heap)

    largest = idx
    left_child = 2 * idx + 1
    right_child = 2 * idx + 2

    # If our current king (node) is smaller than his left_child, we might need to have a revolution!
    if left_child < size and self.heap[idx] < self.heap[left_child]:
      largest = left_child

    # And hey, we might also have a revolt from the right_child too. Heap politics 101!
    if right_child < size and self.heap[largest] < self.heap[right_child]:
      largest = right_child

    # Okay, the dust has settled and now "largest" might not be our king idx anymore.
    if largest != idx:
      self.heap[largest], self.heap[idx] = self.heap[idx], self.heap[largest]  # Dethroned!
      self.sink(largest)  # Long live the king. Long live recursion.

# And voila, you have a peak at the MaxHeap implementation.
# Try it yourself! It's a heap of fun, I promise!

