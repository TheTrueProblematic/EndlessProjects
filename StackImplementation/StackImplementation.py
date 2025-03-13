
# Hey there future coders/ code enthusiasts! This is a fun little project which implements a classic data structure - The Stack!
# It's going to be a blast working on it. So, let's jump right in!

# No extra libraries are needed, we will be using only the builtin functionalities of python

class Stack:
    """
    Stack Class represents a stack data structure in Python
    """

    # Constructor for the class
    def __init__(self):
        """
        Constructor for the stack class
        """
        # Let's initialize our stack as an empty list. Who said lists can't be stacks?
        self.stack = []

    def push(self, item):
        """
        Function to add an item to the stack.
        The item gets added to the end of the list.
        """
        self.stack.append(item)

    def pop(self):
        """
        Function to remove an item from the stack.
        The last item of the list, which represents the top of stack, gets removed.
        """
        if len(self.stack) < 1:
            # Oh no, we can't pop from an empty stack. Let's return None in that case
            return None
        return self.stack.pop()

    def peek(self):
        """
        Function to see the top item of the stack.
        It will return the last item from the list without removing it from stack.
        """
        if not self.stack:
            # Uh-uh, the stack is empty. Nothing to see here, move along!
            return None
        return self.stack[-1]

    def size(self):
        """
        Function to get the size of the stack.
        It returns the number of items currently in the stack.
        """
        return len(self.stack)

    def is_empty(self):
        """
        Function to check if stack is empty or not.
        It will return True if stack is empty, otherwise False
        """
        # Quick pythonic way to check if a list is empty or not
        return not self.stack

# And there you go, we now have our own little stack data structure, all built from scratch, pretty cool, huh?

# Remember, it doesn't matter which data structure you use, as long as it suits your needs. And as always, Happy Coding!

