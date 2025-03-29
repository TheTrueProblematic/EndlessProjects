
# QueueWithStacks.py
# Hello Happy Coders! Get ready to dive into a fascinating journey where we implement a queue with two stacks.
# Sounds adventurous, right? Buckle up, we're about to embark on this fun expedition! Yay!


class QueueWithStacks:
    # Our two stacks. One for the push operation and the other for the pop and peek operations.
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # Fun Time! Let's start with pushing an element to our queue. It's as simple as adding an element to our first stack.
    def push(self, x):
        self.stack1.append(x)

    # Now, let's jump onto something a bit trickier- 'Pop' operation. But don't worry, I've got your back!
    def pop(self):
        # We need to check if our second stack is empty. If it is, we pop all elements from the first stack and push them on to the second.
        # This way, the last element added to the first stack (which should be the first to go), comes on top of the second stack.
        # If our second stack is not empty, we simply pop from the stack.
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    # Woohoo...we're halfway through! Next stop - Peek operation. It's very similar to Pop, just that we don't remove the element from the second stack.
    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    # Finally, let's define an operation to check if our queue is empty. If both our stacks are empty, then our queue is empty.
    def empty(self):
        return not bool(self.stack1) and not bool(self.stack2)


# Congratulations!!! You've successfully implemented a Queue using Stacks! Such a rockstar, you are! Remember, with Python, you can always have fun while coding. Happy Programming!
