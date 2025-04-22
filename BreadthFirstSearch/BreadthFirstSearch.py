
# Woohoo! Let's dive straight into this fun! This python program we're gonna write is all about exploring the world of Graphs using the Breadth-First Search Algorithm a.k.a BFS! Is that not exhilarating or what?

# Okie Dokie, first things first! Let's define our Graph.

class Graph:

    # Our graph is gonna store vertices and its connections. Let's initialize an empty dictionary for that!
    def __init__(self):
        self.graph = {}  # Our beautiful Graph

    # Time to add some edges to our graph. This function does just that!

    def add_edge(self, vertex, edge):
        # This line connects a vertex to an edge. We're going places!
        self.graph[vertex] = edge

    # Now the real fun part starts! BFS Algorithm, WooHoo!

    def BFS(self, start):
        # A list to keep track of all visited nodes. Don't want to go in circles, do we? :P
        visited = [False] * len(self.graph)

        # Queue for our BFS. It's FIFO, baby! First-In-First-Out, Just like in a fair ride line!
        queue = [start]

        # Go ahead and mark the starting node as visited

        visited[start] = True

        while queue:
            # Pop a vertex from the queue to visit next
            vertex = queue.pop(0)
            print(vertex, end=" ")

            # It's time to visit all adjacent vertices of the dequeued vertex node.
            # If a adjacent has not been visited, then mark it visited and enqueue it

            for edge in self.graph[vertex]:
                if visited[edge] == False:
                    queue.append(edge)
                    visited[edge] = True

# Well that's our BFS algorithm ready to explore, Just like a happy wanderer it's eager to traverse our graph.
# Oh and remember, all the fun is in the journey (traversal), not the destination ;)
# Now, time to create our graph and start the journey. Cheers!
