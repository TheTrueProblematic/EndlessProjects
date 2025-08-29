
# Hello there, wonderful people of the world! Let's embark on a fun journey of understanding graphs and how to sort them topologically.
# Tighten up your nerd glasses and let's dive in! (And don't worry, we'll make sure not to drown in the sea of nodes and edges).

# Anywho, Topological what now? Topological sorting, right.
# It's a linear ordering of vertices in a directed acyclic graph (DAG) that, for every directed edge uv from vertex u to vertex v,
# u comes before v in the ordering. 

def topological_sort(graph):
    # Starting off, we initialize an empty list that will contain our sorted elements
    topo_ordered = []

    # A set that holds all nodes with no incoming edge
    incoming_e_less_nodes = set([node for node in graph if not graph[node]])

    while incoming_e_less_nodes:
        # We take a node from the set, say 'bye bye' to it and then append it in our list
        node = incoming_e_less_nodes.pop()
        topo_ordered.append(node)

        to_remove = []  # List to place the nodes we're gonna remove. Why? You'll see! Patience, my friend.
        for successor, edges in graph.items():
            # Good old graph traversal
            if node in edges:
                edges.remove(node) # We're removing edges of our chosen node. Edges, begone!

                # Check if we completely removed a node's edges. If yes, next stop: incoming_e_less_nodes set.
                if not edges:
                    to_remove.append(successor)

        for node in to_remove:
            # We formally say 'hasta la vista' to the node and make it join the incoming_e_less_nodes set
            graph.pop(node)
            incoming_e_less_nodes.add(node)

    # Now, we have to check if we still have edges in the graph. 
    # If we do, then we've found ourselves a cycle which is a big no-no for our topological sort
    if any(edges for edges in graph.values()):
        return None  # Returning nothing, zip, nada in that case.

    return topo_ordered  # Otherwise, tadaa! There you have your topologically sorted list!

if __name__ == "__main__":
    # And, of course, you need a DAG, right? Let's define a graph for illustration.
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    # Call our super-duper topological sort function!
    r = topological_sort(graph)

    # Drum roll, please!
    print("The topological order of the nodes is: ", r if r is not None else "This graph has a cycle!")

