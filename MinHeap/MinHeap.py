
# Hey there! Buckle up because we're going on a thrilling journey,
# where we're gonna build one of the most exciting data structures, a Min-Heap!

# A Min Heap is a complete binary tree in which the value in each internal node
# is smaller than or equal to the values in the children of that node.

# Here's our shiny Min-Heap class!
class MinHeap:

    # Our intrepid constructor, building our heap from scratch.
    def __init__(self):
        self.heap = []
  
    # This gem of a function takes us on a magical ride through
    # all the nodes above a given index until we find our place in the world.
    def heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index < 1:
            return
        elif self.heap[parent_index] > self.heap[index]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index] # Swap 'em!
            self.heapify_up(parent_index) # Let's continue our adventure up the heap!
  
    # Brave explorer, your quest is to find the smallest value through the children nodes.
    def heapify_down(self, index):
        left_child_index = (index * 2) + 1
        right_child_index = (index * 2) + 2

        # Let's find out who's the smallest of them all.
        smallest = index
        if len(self.heap) > left_child_index and self.heap[smallest] > self.heap[left_child_index]:
            smallest = left_child_index
        if len(self.heap) > right_child_index and self.heap[smallest] > self.heap[right_child_index]:
            smallest = right_child_index

        # Unless we're already the smallest, let's go deeper into the rabbit hole.
        if smallest != index:
            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            self.heapify_down(smallest)
  
    # Whoosh! Add new elements to the min heap and let the magic of heapify do the heavy lifting!
    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)
  
    # Extract the minimum value from the heap. Don't worry, we've got a system!
    def extract_min(self):
        if len(self.heap) > 1:
            min_val = self.heap[0]
            self.heap[0] = self.heap[-1]
            min_value = self.heap.pop()
            self.heapify_down(0)
            return min_val
        elif len(self.heap) == 1:
            min_value = self.heap.pop()
            return min_value
        else:
            return None
  
# Isn't that just one nice exploration? Python and data structures, 
# it doesn't get much better than this... Until next time, fun coding!
