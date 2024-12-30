
# Hey hey! Welcome to our fun little project called "EvaluatePostfix".
# What we're aiming to do here is compute the value of an expression given in postfix format.
# If you're wondering, "What in the world is POSTFIX?", here it is in a nutshell:
# It's an alternate way of writing down expressions, eliminating the need for parentheses to indicate priority of operations.
# For instance, the expression "2 3 1 * + 9 -" is the postfix expression for "2 + 3 * 1 - 9"
# Now onward to the coding part!

def evaluate_postfix(expression):
    # Python's built-in data structures come to our rescue!
    # We'll use a stack to keep track of the operands.
    stack = []
    
    # Did you know? Python makes it easy for us to handle each character in a string one at a time.
    # So let's loop through each symbol in the postfix expression.
    for symbol in expression.split():
        # Python can tell if a string represents a number. Neat, huh?
        if symbol.isdigit():
            # If it's a number, we're going to push it into our stack. But wait!
            # Python wants us to convert it to integer first. Here we go!
            stack.append(int(symbol))
        
        else:
            # If it's not a number, it must be an operator (*, /, +, -).
            # And we're going to perform the operation on the last two elements in our stack—you know, postfix style ;)
            operand2 = stack.pop()
            operand1 = stack.pop()
            
            # Finally, we're going to do the math!
            # And of course, push the result back into the stack.
            if symbol == '*':
                stack.append(operand1 * operand2)
            elif symbol == '/':
                stack.append(operand1 / operand2)
            elif symbol == '+':
                stack.append(operand1 + operand2)
            else: # symbol must be '-'
                stack.append(operand1 - operand2)
    
    # If all went well, our stack should now hold exactly one item: the result of our expression!
    # And that's exactly what we're going to return. Simple and beautiful, isn't it?  
    return stack.pop()


# Now, let's put our shiny new function to the test!
if __name__ == "__main__":
    # Our test expression: "2 3 1 * + 9 -". What's it supposed to evaluate to? Why, it should give you -4, of course!
    test_expression = "2 3 1 * + 9 -"
    print(evaluate_postfix(test_expression))
    
# And we're done! We've just written a neat little Python script to evaluate postfix expressions.
# So next time you encounter a postfix expression, just remember: Python's got your back!
# Happy coding!

