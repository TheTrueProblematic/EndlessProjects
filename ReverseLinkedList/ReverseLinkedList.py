
# Hello my programming pals! Let's dive into our little Python adventure today, and spend some good time rearranging those famous Nodees (yeah, I'm cool enough to give nicknames to Nodes).

# But before we start teasing our brain cells, let's define our Node buddies.

class Node: # Here's our class definition!
    def __init__(self, val=None, nxt=None): # Every good adventure starts with an 'init'!
        self.val = val # Here's our piece of value. All mine! (or ours, to be exact)
        self.next = nxt # A mark to find the next stop in the journey.

 def reverse_linked_list(head): # Now the magic starts...
 
    prev_node = None # We don't have any previous stop yet, so None it is.
    current_node = head # Our start point is the head, the top honcho in our little linked list adventure.

    while current_node: # Now let's start our journey, as long as there's a place to go...
        
        next_node = current_node.next # Let's peek at the next stop before we touch anything.
        
        current_node.next = prev_node # Now here's the twist - instead of going forward, we're connecting it back to the previous stop!
        
        prev_node = current_node # The current stop will be our next "previous" stop. Talk about the pace of change!
        
        current_node = next_node # And, the next stop becomes our current stop. Hop on!
        
    return prev_node  # Ta-da! The journey doesn't end with the last stop - it BECOMES the new head. So, enjoy your hike from the end!

# Phew! Wasn't that a little mind-bending? But hey, we sorted it out, didn't we? See you on our next code-trek!


