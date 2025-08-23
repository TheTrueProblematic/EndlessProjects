
# Hey there, fellow Pythonista!
# This python file is called GraphAdjacencyMatrix. As the name implies, it is spiced up
# to represent a graph using an adjacency matrix, with lots of fun operations to perform. 
# So buckle up, let's have a thrilling ride!

class Graph:
    # Here's our Graph class initialization. Quite exciting, isn't it?
    def __init__(self, num_of_vertices):
        self.num_of_vertices = num_of_vertices
        self.graph = [[0 for column in range(num_of_vertices)] for row in range(num_of_vertices)]

    # Now, this little function right here is for adding edges to our graph. What's a graph without some connections, huh?
    def add_edge(self, start_vertex, end_vertex):
        # Since it's an undirected graph, we'll add the edge in both directions.
        self.graph[start_vertex][end_vertex] = 1
        self.graph[end_vertex][start_vertex] = 1

    # And here's a cute function to print our graph, because who doesn't want to see their creation?
    def print_graph(self):
        for row in self.graph:
            for value in row:
                print(value, end = ' ')
            print()

# Alright, so that's it for our graph class.
# Let's give it a spin!

# Don't blink, because this is where the magic happens.
if __name__ == "__main__":
    graph = Graph(5)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    # Let's reveal our masterpiece! Drum roll, please...
    graph.print_graph()

# And that's all, folks! 
# Thanks for accompanying me on this venture. Happy Coding!
