
# Greetings my fellow Python lovers! Let's go on a little adventure to find strongly connected components in a graph using Kosaraju's Algorithm.
# Buckle up and keep those seatbelts fastened because this is going to be a fun ride!

class Graph:
    def __init__(self, vertices):
        self.V = vertices # Here's where we store number of vertices. Good to keep track, isn't it?
        self.graph = [[] for _ in range(vertices)] # An empty list for every vertex

    def addEdge(self, u, v):
        self.graph[u].append(v) # Add v to u’s list, join the adventure!

    def DFSLoop(self, graph, visited, stack):
        for i in range(self.V): # Let's keep going on the adventure till we've visited them all!
            if visited[i] == False:
                self.DFS(graph, i, visited, stack)

    def DFS(self, graph, v, visited, stack):
        # Visit the node!
        visited[v] = True

        # Go to all vertices adjacent to this
        for i in graph[v]:
            if visited[i] == False:
                self.DFS(graph, i, visited, stack)

        stack = stack.append(v)  # Push current vertex to stack which stores the result

    def reverse(self):
        # Oh no! We got lost, let's just take a u-turn and keep the adventure going!
        gr = Graph(self.V)

        for v in range(self.V):
            for i in self.graph[v]:
                gr.addEdge(i, v)

        return gr

    def printSCCs(self):
        stack = []
        visited =[False]*self.V

        self.DFSLoop(self.graph, visited, stack)  # Fill vertices in stack 

        gr = self.reverse()  # Create a reversed graph

        visited =[False]*self.V  # Mark all the vertices as not visited 

        while stack:
            v = stack.pop()

            if visited[v] == False:
                gr.DFS(gr.graph, v, visited, [])
                print()

# Ok folks! That's it for our Python adventure of the day. I hope you had fun and maybe learned a thing or two!
# Remember, keep coding and stay Pythonic! ;)

