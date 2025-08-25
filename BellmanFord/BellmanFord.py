
# Hello, adventurer! Welcome on board. Let's take a thrilling journey through the mystical realm of Bellman Ford, together.
# Chances are, you're looking at this file because you need a handy guide to find the shortest path, even allowing negative weights, in a graph.

# So let's get started. Buckle up!

# Start by defining the magic function, the BellmanFord algorithm.
def BellmanFord(graph, V, E, src):

    # Initializing distance from the source to all other vertices as INFINITE
    # Won't that be fun? It's like the universe. Infinite. Unfathomable.
    dis = [float("Inf")] * V
    dis[src] = 0

    # Maybe this part will feel like math class all over again. But trust me, it's even cooler.
    # For every vertex, apply relaxation for all the edges in a loop.
    for i in range(V - 1):
        for j in range(E):
            if dis[graph[j][0]] != float("Inf") and dis[graph[j][0]] + graph[j][2] < dis[graph[j][1]]:
                dis[graph[j][1]] = dis[graph[j][0]] + graph[j][2]

    # Now, this is where we handle negative weight cycles (those nasty surprises lurking in the shadow).
    # Further relaxation of the edges
    for i in range(E):
        x = graph[i][0]
        y = graph[i][1]
        weight = graph[i][2]
        if dis[x] != float("Inf") and dis[x] + weight < dis[y]:
            print("Graph contains negative weight cycle!")
            return

    # Huzzah! If you've made it this far, good job! You've braved the wilderness and found your treasure.
    # Let's see what you've won, shortest path from the source!
    print("Vertex Distance from Source:")
    for i in range(V):
        print(f"{i}\t\t{dis[i]}")

# Okay, now that the magic is ready, let's conjure up a graph for you to navigate.
# This is your quest! You're the hero. Your treasure's waiting.
# Note: Every edge has three values (u, v, w) where the edge is from vertex u to v. 
# And the weight of the edge is w.

graph = [[0, 1, -1], [0, 2, 4], [1, 2, 3], [1, 3, 2], [1, 4, 2], [3, 2, 5], [3, 1, 1], [4, 3, -3]]
V = 5  # Total number of vertices in the graph
E = 8  # Total number of edges in the graph

# Kick off the party with the source vertex as 0 (you've gotta start somewhere, right?)
src = 0

# Embark on your adventure. BellmanFord ho!
BellmanFord(graph, V, E, src)

# Whew! You made it! You're pretty awesome.
# Pat yourself on the back, then come back again anytime you need to travel with the BellmanFord.

