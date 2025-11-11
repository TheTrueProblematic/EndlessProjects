Python
# Greetings! Welcome to this amazing Python project!🎉🔥
# We're about to generate a wonderful random undirected graph with a given number of vertices and edges.
# So buckle up partner, let's take you for a ride!🚀
# Let's start by importing the libraries we need. Oh, wait! We can't have any.
# So let's write all the logic ourselves, because who doesn't love a good ol' challenge, right?😜

import random

class Graph:
    # Let's Unforget the amazing Graph class👇
    # Its purpose in life is to create our random graph representation!

    def __init__(self, num_vertices):
        # When creating a beautiful new Graph object,
        # we'll need the number of vertices🌐

        # We keep track of the vertices count
        self.num_vertices = num_vertices
        # And create our graph representation as a simple adjacency list.
        # Just the way a Graph should be stored! No fuss at all✌️
        self.adj_list = {}
        for i in range(num_vertices):
            self.adj_list[i] = []

    def generate_edges(self, num_edges):
        # We've got a graph, now it's time to make connections!🌉

        # Generating random edges
        while num_edges > 0:
            vertex1 = random.randint(0, self.num_vertices - 1)
            vertex2 = random.randint(0, self.num_vertices - 1)

            # If the edge doesn't already exist and it isn't going from a vertex to itself
            if vertex1 != vertex2 and vertex2 not in self.adj_list[vertex1]:
                # Add edge to both vertex1 and vertex2 (since this graph is undirected)
                self.adj_list[vertex1].append(vertex2)
                self.adj_list[vertex2].append(vertex1)
                num_edges -= 1

    def print_graph(self):
        # Oh😲, our graph has been created, now let's print it out!

        for vertex in self.adj_list:
            print(f"Vertex {vertex} is connected to {self.adj_list[vertex]}")
            # Let's print out each vertex and its connections! How wonderful💐

def main():
    # Grab your popcorn, folks! Lights, camera, action!🎥
    # Graph time! Let's generate a graph with 5 vertices and 7 edges.
    graph = Graph(5)
    graph.generate_edges(7)
    graph.print_graph()

# We made it🎊, what a wild programmer's ride. Fasten your seatbelt for the next time we meet.
# Remember to be good, and keep writing code full of delight!

if __name__ == "__main__":
    main()
