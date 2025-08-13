
# Let's have some fun creating a Python Graph Adjacency List!

# First, let's lay some groundwork - We're going to be working with the oh-so-ever-fabulous Graphs!
# Graphs are an exciting collection of objects, where some pairs of the objects are connected by links.
# They are pretty nifty tools, and you can use them to model many types of relationships and processes in physical, biological, social and information systems in a super neat way!

class Graph:
    # Our Graph is going to use an Adjacency List, which is a way to represent a graph as a map from nodes to lists of edges.
    def __init__(self):
        self.graph = {}
        
    # Now, let's create an add_edge function, which can take two nodes and add an edge between them in our graph.
    def add_edge(self, node1, node2):
        # If node1 isn't in the graph, we'll need to add an empty list for it
        if node1 not in self.graph:
            self.graph[node1] = []
        
        # And the same goes for node2
        if node2 not in self.graph:
            self.graph[node2] = []
        
        # Now that we're sure we have lists to add to, let's add the edge!
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)
        
    # And now we need a way to display our graph
    def display(self):
        # Let's just go ahead and print out each node and its connections
        for node in self.graph:
            print(f"{node} connected to {self.graph[node]}")
        

# And that's it! We've got a Graph that can handle adding edges and displaying the graph.
# Pretty cool, right?

if __name__ == "__main__":
    # Let's test it out!
    graph = Graph()
    
    # We can add some edges!
    graph.add_edge('A', 'B')
    graph.add_edge('B', 'C')
    graph.add_edge('C', 'D')
    graph.add_edge('D', 'E')
    graph.add_edge('E', 'F')
    graph.add_edge('B', 'D')
    graph.add_edge('D', 'F')

    # And then display the graph!
    graph.display()
