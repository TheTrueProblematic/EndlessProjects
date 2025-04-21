
# Hey there, beautiful people! Time for some fun - let's do some Depth-First Search (DFS), shall we?

# Standard python libraries, just how we like it!
# Because who needs extra dependencies when python's got you sorted?

class Graph:

    # Init the whole shenanigan with some tasty nodes
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph_dict = {}

    # Just a good, ol' tool-method to add edge to our graph
    def add_edge(self, node, neighbour):
        if node not in self.graph_dict:
            self.graph_dict[node] = [neighbour]
        else:
            self.graph_dict[node].append(neighbour)

    # And here we go, the main event! Hahaha fun times...
    def dfs(self, start_vertex):
        visited = []
        stack = [start_vertex]

        # Let's loop until that poor stack's empty
        while len(stack):
            # Okay, popping the last inserted item first, because we are hipster "last in, first out!" (or just call it DFS logic!)
            node = stack.pop()
            
            if node not in visited:
                visited.append(node)
                # Initializing child nodes to the node variable, because children are the future!
                if node in self.graph_dict:
                    children = self.graph_dict[node]

                    # Okay kiddo, time to jump on the stack!
                    for child in children:
                        stack.append(child)

        # And we're done :D
        return visited

# Having a graph party down here
graph_elements = {"A": ["B", "C"],
                  "B": ["A", "D", "E"],
                  "C": ["A", "F"],
                  "D": ["B"],
                  "E": ["B", "F"],
                  "F": ["C", "E"],
                 }

g = Graph(graph_elements)

# Setting up the DFS stage with start vertex 'A'
print(g.dfs('A'))  # DFS, baby!

# You did good! Now, time for that well-earned cup of coffee, fellow coder :)
# Until next time!
