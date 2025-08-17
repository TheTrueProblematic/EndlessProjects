
# Welcome fellow code buffs!
# Today, we're embarking on a magical journey to create a PriorityQueue based on binary heap implementation.
# Exciting, right? So grab a cup of coffee, buckle up, and let's dive right into this Python adventure.

class PriorityQueue(object):
    def __init__(self):
        # Initializing our binary heap as an empty list
        self.heap = []

    def push(self, d):
        # Adding an element to our binary heap (It's like inviting a new friend to our party 🎉)
        self.heap.append(d)
        self.__float(len(self.heap) - 1)

    def pop(self):
        # Removing the element with the highest priority (aka lowest value). Well, someone has to go home first 🎈
        if self.heap:
            self.__swap(0, len(self.heap) - 1)  # swap the first and the last element
            max_value = self.heap.pop()  # pop the last element as it is now the max value
            self.__bubble(0)
            return max_value
        else:
            return None

    def __swap(self, i, j):
        # A little switcheroo! Swapping two elements in our binary heap.
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __float(self, index):
        # Boom! 💥 Floating the element at the index to its appropriate spot!
        parent_index = (index - 1) // 2
        if index <= 0 or self.heap[parent_index] <= self.heap[index]:
            return
        else:
            self.__swap(parent_index, index)
            self.__float(parent_index)  # recursive call to keep floating up

    def __bubble(self, index):
        # And bubble! Making sure our element sinks down to its rightful place! 🏊‍
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        min_value_index = index
        if left_child_index < len(self.heap):
            if self.heap[left_child_index] < self.heap[min_value_index]:
                min_value_index = left_child_index

        if right_child_index < len(self.heap):
            if self.heap[right_child_index] < self.heap[min_value_index]:
                min_value_index = right_child_index


        if min_value_index != index:
            self.__swap(index, min_value_index)
            self.__bubble(min_value_index)  # recursive call to keep sinking down

    def is_empty(self):
        # Checking if the party is over 😢
        return not bool(self.heap)


# And voila! You've made it to the end of our Python scripting journey. By now, you have a PriorityQueue that uses a binary heap.
# Now you can invite elements to your party and have them leave in an orderly manner.
# Well done, fellow Pythonista! 🐍

