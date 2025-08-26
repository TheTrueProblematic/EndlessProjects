
# Hello there, fellow programmer! Let's have some fun with graphs and the shortest paths in them!
# This is a Python implementation of the glorious Floyd-Warshall algorithm for finding all-pair shortest paths in a graph.
# Warning: Be sure your graph does not contain negative cycles, else, it's going to be a never-ending journey!

import sys

def floyd_warshall(graph):
    """
    function to compute all-pairs shortest paths
    """
    n = len(graph)

    # Distance list. The value of dist[i][j] will hold the shortest distance from i to j
    dist = list(map(lambda i : list(map(lambda j : j , i)) , graph))

    # Calculate shortest distances
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # We can get to i-j via updating the current path or via k (i-k-j)
                dist[i][j] = min(dist[i][j], dist[i][k]+ dist[k][j])
    
    # Print the shortest distance matrix
    print_shortest_distance(dist)


def print_shortest_distance(dist):
    """
    function to print shortest distances
    """
    n = len(dist)

    # Yippee! Lets print the shortest path matrix!
    print ("Following matrix shows the shortest distances between every pair of vertices.")
    for i in range(n):
        for j in range(n):
            if (dist[i][j] == sys.maxsize):
                # No path exists!
                print ("%7s" %("INF")),
            else:
                # Lucky us, we found a path!
                print ("%7d\t" %(dist[i][j])),
            if j == n-1:
                print ()


uffman