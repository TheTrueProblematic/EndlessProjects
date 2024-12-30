
# Hey there, fellow Python enthusiasts! Today we're going to take on a fun little challenge: converting infix expressions to postfix notation.
# This can be a real handy tool, especially if you're dealing with some heavy duty mathematical expressions.
# So buckle up, let's get our hands dirty with some Python code!

# We'll be needing a stack to help us with the conversion. Since Python's built-in list can act as a stack, we don't need any additional dependencies. Isn't Python neat?

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

def infixToPostfix(infixexpr):
    # Defining the precedence of operators. The larger the number, the higher the precedence.
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    # Let's create the stack that's going to help us with the conversion.
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    # Time to start the conversion!
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return " ".join(postfixList)

# And that's all folks! Here's a quick usage example.
# Just put an infix expression (like A * B + C * D) as the parameter in the infixToPostfix function!

if __name__ == "__main__":
    try:
        infix_expression = input("Enter infix expression (like A * B + C * D): ")
        print(infixToPostfix(infix_expression))
    except Exception as e:
        print("An error occurred: ", e)
