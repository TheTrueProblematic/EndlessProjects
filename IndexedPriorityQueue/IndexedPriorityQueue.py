
# Hello, pals! Welcome to the fun zone: we're implementing an Indexed Priority Queue today.
# Indexed Priority Queue? Sounds complex, right? In a nutshell, it's a super cool data structure that will allow us to decrease the keys at specific indices.
# The fun part? We're doing this using just Python. No imports, no external dependencies - just pure Python goodness! Let's dive in!

# Let's create our class for the queue
class IndexedPriorityQueue:
  # Initializing our queue with an empty list.
  def __init__(self):
    self.queue = []

  # A private helper method to swap the elements at two indices.
  # Just like a fun dance swap in a party!
  def _swap(self, i, j):
    self.queue[i], self.queue[j] = self.queue[j], self.queue[i]

  # A private helper method to help us 'bubble up' a value to its correct place in the queue after its value was decreased.
  # We keep swapping it with its parent until we find it's right place!
  def _bubble_up(self, i):
    parent = (i - 1) // 2  # Finding the parent, just your everyday family tree things
    while i > 0 and self.queue[i] < self.queue[parent]: # If the child is smaller, we swap!
      self._swap(i, parent)  # Let's swap
      i = parent  # Updating the index to the parent's index
      parent = (i - 1) // 2  # Finding the next parent

  # Decreasing the key at a specific index: the 'creme de la creme' of our Queue!
  def decrease_key(self, i, key):
    if key >= self.queue[i]:  # If new key is greater, then we do nothing! Simplicity is key (pun intended!)
      return
    self.queue[i] = key  # If the key is smaller, we update the value
    self._bubble_up(i)  # And bubble up the key to its rightful place!

  # Let you peek into the smallest element, without taking it out
  def find_min(self):
    if not self.is_empty():  # If it's not empty
      return self.queue[0]  # The smallest element is at the front
    return None  # if it's empty, we return None

  # An added functionality to check if queue is empty
  def is_empty(self):
    return len(self.queue) == 0

  # Inserting a key into the Queue - also, very straightforward, much like slipping a note into your crush's locker!
  def insert(self, key):
    self.queue.append(key)  # We add the key at the end
    present_index = len(self.queue) - 1  # And determine it's index
    self._bubble_up(present_index)  # And like before, we bubble up to make sure it's in the right place

# And there you have it! A shiny, new Indexed Priority Queue, all ready to rock and roll! Go on, take it for a spin!

