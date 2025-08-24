
"""
AStarPathfinder

Woohoo! We're going to build an A* pathfinder python script! Let's get the party started! There's no better fun than
finding the shortest path from point A to point B, right? :D

No GUI, no external libraries, no internet! Pure python, baby! That's how we like it!

OK, let's roll! (on my brand new rollerblades, of course!)
"""

# A* actually needs to be able to compare nodes, so we need a Node class that has comparison magic methods!
class Node:
    def __init__(self, x, y):
        # Let's store the x and y coordinates of our node. Easy enough!
        self.x = x
        self.y = y

        # Now we need some other properties for our A* fun-time extravaganza!
        self.g = 0  # The cost from start to this node
        self.h = 0  # The estimated cost from this node to the goal
        self.f = 0  # The total cost! g + h = f, simple math is simple!
        self.parent = None  # The parent node, so we can backtrack our path

    def __eq__(self, other):
        # Remember comparing nodes? Let's do that here!
        return self.x == other.x and self.y == other.y


# Now, onto the main event! The A* Pathfinding function itself!
def a_star_pathfinding(start, end, grid):
    """
    The Mighty A* Pathfinding Algorithm!
    Using a grid, a start and an end point, finds the optimal path from start to end!
    """

    # Step 1: We need to create the open and closed lists for our nodes.
    open_list = []  # Nodes that have been discovered but not evaluated.
    closed_list = []  # Nodes that have already been evaluated.

    # Step 2: Add the starting point to our open list. We're starting the journey at 'start'! How fitting!
    open_list.append(start)

    # Step 3: As long as there are nodes to evaluate in the open list, keep on truckin'!
    while len(open_list) > 0:
        # Get the node in the open list with the lowest f score. We're all about efficiency here!
        current_node = min(open_list, key=lambda o: o.f)

        # We're done with this node, so move it from the open list to the closed list.
        open_list.remove(current_node)
        closed_list.append(current_node)

        # Step 4: If we've reached the end... CELEBRATE! You've found the path!
        if current_node == end:
            path = []
            while current_node is not None:
                path.append(current_node)  # Build the path backwards
                current_node = current_node.parent  # Go to the next node
            return path[::-1]  # Flip it around to get it in the correct order.

        # Step 5: It's time to check out the neighbours! Let's find out where our party can go next.
        neighbours = [
            Node(current_node.x - 1, current_node.y),
            Node(current_node.x + 1, current_node.y),
            Node(current_node.x, current_node.y - 1),
            Node(current_node.x, current_node.y + 1),
        ]

        for neighbour in neighbours:
            # Step 6: If the neighbour is out of bounds or it's a wall, it's a no from me dawg!
            if neighbour.x < 0 or neighbour.y < 0 or neighbour.x >= len(grid) or neighbour.y >= len(grid[0]) or grid[neighbour.x][neighbour.y] == 1:
                continue

            # Step 7: If our friendly neighbour is already in the closed list, we don't need to evaluate it again!
            if neighbour in closed_list:
                continue

            # Step 8: Calculate the g, h and f score for the neighbour.
            neighbour.g = current_node.g + 1
            neighbour.h = abs(end.x - neighbour.x) + abs(end.y - neighbour.y)
            neighbour.f = neighbour.g + neighbour.h

            # Step 9: If the neighbour is in the open list, check if this path to the neighbour is better.
            for node in open_list:
                if neighbour == node and neighbour.g > node.g:
                    continue

            # If we're here, then this neighbour is a keeper!
            neighbour.parent = current_node
            open_list.append(neighbour)

    # If we've looked at every single node and didn't find a path, then there isn't one! Bummer.
    return None

