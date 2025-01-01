
# Hello Friendly User :) Welcome to our super-cool project which is all about implementing a stack using Python lists!
# We would not use any complex data structures, no dependencies, no API, nothing fancy but a simple list.
# So, let's dive in and start stacking!!

class Stack:
    """ Our own stack class which uses a list! """

    def __init__(self):
        """ The constructor of our class. Here, we initialize an empty list! """
        self.stack = []

    def is_empty(self):
        """ This function checks if our stack (which is actually a list) is empty. """
        return len(self.stack) == 0

    def push(self, data):
        """ This function adds an element to our stack. """
        self.stack.append(data)

    def pop(self):
        """ This function removes an element from our stack. """
        # first we check if our stack is empty or not
        if self.is_empty():
            # oh no, our stack is empty. We should let the user know about this
            print("Stack is empty!")
        else:
            # yay, our stack has some elements. Let's pop one out
            return self.stack.pop()

    def peek(self):
        """ This function lets us see the top element of our stack. """
        # just like with our pop function, we should check first if the stack is empty or not
        if self.is_empty():
            # oops, it's empty. Let's let the user know
            print("Stack is empty!")
        else:
            # it has some elements. So, we return the last added element without popping it out
            return self.stack[-1]


# That's it folks! Our Stack class is ready for action. Now you can create stacks all day long using lists.
# Remember with great power comes great responsibility. Don't forget to pop what you push into the stack!
# I hope you have as much of a blast using this code as I had writing it. Keep Stackin'! Cheers!!
