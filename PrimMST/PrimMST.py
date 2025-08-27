
# Woohoo! Get ready for a chilling trip through Prim's Algorithm! 
# Using this algorithm we're going to find the Minimum Spanning Tree of a graph.
# We will be using python's built-in structures to keep things simple.
# No libraries, APIs or GUI! Just pure python goodness!
# Remember, handling trees is not a "prim"-itive task, hang on!

import sys  # Only system level operations.

# Graph as an adjacency matrix.
# We'll create a graph and fill it with '0's initially.
# The nodes have a connection between them if their corresponding cell in the matrix is 1.

def create_graph(vertices):
    graph = [[0 for column in range(vertices)] for row in range(vertices)]
    return graph

# A utility function to find the vertex with minimum distance value.
def minKey(key, mstSet, vertices):
    min_value = sys.maxsize  # Initially set to infinite.
    
    for v in range(vertices):
        # Find unvisited vertex with smallest known distance to any vertex in MST.
        if key[v] < min_value and mstSet[v] == False:
            min_value = key[v]
            min_index = v
    
    return min_index

# Finally, the main function that builds the MST using adjacency matrix representation of graph.
def primMST(graph, vertices):
    key = [sys.maxsize] * vertices  # Values used to pick minimum weight edge in cut.
    parent = [None] * vertices  # Array to store constructed MST. 
    key[0] = 0  # Make key 0 so that this vertex is picked as first vertex.
    mstSet = [False] * vertices  # To represent set of vertices included in MST.

    parent[0] = -1  # First node is always the root of MST.

    for cout in range(vertices):
        u = minKey(key, mstSet, vertices)
        mstSet[u] = True  # Add the picked vertex to the MST Set.

        # Update key value and parent index of the adjacent vertices of
        # the picked vertex. Consider only those vertices which are not
        # yet included in MST.
        for v in range(vertices):

            # Update the key only if graph[u][v] is smaller than key[v].
            if 0 < graph[u][v] < key[v] and mstSet[v] == False:
                key[v] = graph[u][v]
                parent[v] = u
                
    printMST(parent, graph, vertices)  # Print the constructed MST.

# A function to print the constructed MST.
def printMST(parent, graph, vertices):
    print("Edge \tWeight")
    for i in range(1, vertices):
        print(parent[i], "-", i, "\t", graph[i][parent[i]])

# That's all folks! Have fun building MSTs with Prim!
# Remember to keep your trees well "prim"-ed!
