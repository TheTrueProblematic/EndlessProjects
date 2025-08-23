
"""
Hey buddy! Welcome to our cool little project here where we're going to compute the shortest paths
in a weighted graph using our pal, Dijkstra's algorithm. Fear not, as we've got a fun journey ahead!
Dijkstra's algorithm, you say? It's a pretty awesome algorithm for finding the shortest paths from a
single source vertex to all other vertices in a graph. Pretty neat, huh? Buckle up and let's roll!
"""

# We have our necessary imports here. Just our trusty Python Standard Library. No dependencies at all!
from collections import defaultdict, deque

def compute_dijkstra(graph, start_vertex):
    """
    Let's give Dijkstra's Algorithm a spin, shall we? You're gonna love it!
    We're taking in a graph and a start vertex. Simple as pie!
    """

    # Creating a dictionary to store the shortest paths
    shortest_paths = defaultdict(lambda: float('inf'))
    shortest_paths[start_vertex] = 0

    # This nifty little data structure helps us keep track of vertices to check
    queue = deque([start_vertex])

    while queue:
        # Pop the vertex from the front of the queue
        vertex = queue.popleft()

        # Visit each neighbour of the current node
        for neighbour, weight in graph[vertex]:
            alternate_path_dist = shortest_paths[vertex] + weight

            # Check if the alternate path distance is shorter. If so, then huzzah! We've got a shorter path!
            if alternate_path_dist < shortest_paths[neighbour]:
                shortest_paths[neighbour] = alternate_path_dist
                queue.append(neighbour)

    # All done! We return our shortest_paths dict full of shorty paths!
    return shortest_paths

# Let's test our function with an example now, shall we? I like examples, don't you?
if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 3)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 3), ('B', 2), ('D', 3)],
        'D': [('B', 5), ('C', 3)]
    }
    print(compute_dijkstra(graph, 'A'))

"""
Voila! We've done it! We took a graph and a starting vertex, and computed the shortest 
paths to every other vertex using Dijkstra's algorithm. Pretty cool, huh? I had a blast, 
I hope you did too! Cheers, mate!
"""
