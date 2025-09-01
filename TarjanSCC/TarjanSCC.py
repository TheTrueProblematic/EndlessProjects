
# Hey there sunny coder! Brace yourself for some algorithmic fun! 
# We are going to code up Tarjan's algorithm for finding strongly connected components in a graph!
# Isn't that exciting? So let's embark on this code-filled adventure with python!

class Vertex:
    def __init__(self, name):
        # Initialing the Vertex name and setting the discovery and low-link values as -1 initially
        self.name = name
        self.d = -1
        self.low = -1
        # As we haven't visited any vertices yet, we'll initialize the on_stack status of this vertex to False
        self.on_stack = False

        
class TarjanSCC:

    def __init__(self, graph):
        # Our brave little Tarjan would need a graph to traverse,
        # so we set this as an attribute and define other helper variables.
        self.graph = graph
        self.time = 0
        self.stack = []
        self.components = []

    def connect(self):
        # Here our hero Tarjan goes on a journey to find all SCCs!
        for vertex in self.graph:
            if vertex.d == -1:
                self.strongconnect(vertex)
        return self.components

    def strongconnect(self, vertex):
        # Tarjan's magical function to deeply recursively explore the graph!
        vertex.d = self.time
        vertex.low = self.time
        self.time += 1
        self.stack.append(vertex)
        vertex.on_stack = True

        for v in self.graph[vertex]:
            if v.d == -1:
                self.strongconnect(v)
                vertex.low = min(vertex.low, v.low)
            elif v.on_stack:
                vertex.low = min(vertex.low, v.d)

        if vertex.low == vertex.d:
            connected_component = []
            while True:
                v = self.stack.pop()
                v.on_stack = False
                connected_component.append(v.name)
                if v == vertex:
                    break
            self.components.append(connected_component)
        
# Aaand that's the end of the adventures of the brave Tarjan in his quest for SCCs!!
# This script neither requires an internet connection, nor uses fancy libraries
# and can be joyfully executed on the command line, thus making it a portable little program!

