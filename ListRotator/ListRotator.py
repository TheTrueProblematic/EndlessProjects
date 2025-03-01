
# Hey, this is your happy programmer friend!
# What you're looking at is a fun python script that helps you rotate a list left or right by a certain number of positions.
# We absolutely LOVE clean and easy code, so we've made sure this runs entirely on the command line, oh, and the best part? NO additional dependencies are required! Whoohoo!

# So, let's get this party started!

def rotate_list(items, direction, amount):
    """Rotate a list either 'left' or 'right' by a certain amount.

    items: the list to rotate.
    direction: the direction to rotate, 'left' or 'right'.
    amount: the number of positions to rotate.
    """

    # Hurray if no rotation is needed, we just return the list how it is!
    if amount == 0:
        return items

    # Now let's rotate this list!
    # Oh and did you know? A positive rotation is to the right, 
    # and a negative rotation is to the left. Cool, huh?

    # Let's set the rotation direction.
    # We're going to keep it really simple: -amount for left, amount for right.
    rotation = -amount if direction == 'left' else amount

    # Now comes the most exciting part... The actual rotating!! 
    # Python makes it super easy for us with list slicing.
    return items[rotation:] + items[:rotation]

# Alright, to run this fantastic rotator, just call it in the main function 
# with your preferred parameters. So simple!

if __name__ == '__main__':
    # Here we go! Your very own list to rotate.
    my_list = [1, 2, 3, 4, 5]

    # Feel free to change the direction and amount to your liking.
    direction = 'left'
    amount = 1

    # So let's do this! Start the rotation!
    print(rotate_list(my_list, direction, amount))
    # And voilà, you’ve got your list magically rotated! Have some fun with it!

# You've made it to the end of the script! Congrats, and happy rotating!
