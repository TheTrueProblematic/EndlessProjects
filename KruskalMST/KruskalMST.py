
# Well hello, dear programmer!
# Ready for another exciting Python adventure? Buckle up, because today we're going to find the Minimum Spanning Tree (MST) of a graph using the legendary Kruskal's Algorithm! No GUIs, no dependencies, no Internet access - just pure, beautiful Python code with your truly honest companion – the command line! Let's get to it!

# First, let's start off by defining our thrilling Graph class, packed with wondrous methods and mysterious attributes! 
class Graph: 
    def __init__(self,vertices): 
        self.V= vertices 
        self.graph = [] 
   
    # Our trusty method to add an edge to the graph
    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w]) 

    # We’ll be using exciting union-find techniques throughout this journey
    # And here’s a method to find set of an element i!
    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 

    # Our amazing method for union of two sets of x and y!
    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 

        # Well, we have a case - Attaching smaller rank tree under root of high rank tree!
        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot 

        # So, it’s a tie… But worry not! We make one as root and increment its rank by one
        else :
            parent[yroot] = xroot 
            rank[xroot] += 1

    # And for the main highlight! Our fearless Kruskal’s algorithm method!
    def KruskalMST(self): 
        result =[]
        i,e = 0,0 #An index variable, used for sorted edges 

        # We didn’t forget. Let’s sort all the edges in ascending order
        self.graph = sorted(self.graph,key=lambda item: item[2]) 

        parent, rank = [], [] 

        # Create V subsets with single elements 
        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 

        # And let the action begin! Number of edges to be taken is equals V-1 
        while e < self.V -1 : 
            u,v,w =  self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent ,v) 

            # If it doesn't cause a cycle, include it in result and increment the index of result for next edge
            if x != y: 
                e = e + 1     
                result.append([u,v,w]) 
                self.union(parent, rank, x, y)            

        # Let's print the contents of result[] to display the built MST 
        print("Following are the edges in the constructed MST")
        for u,v,weight  in result: 
            print ("%d -- %d == %d" %(u,v,weight)) 

# And there you have it! Let’s test it out with an MST, shall we?
g = Graph(4) 
g.addEdge(0, 1, 10) 
g.addEdge(0, 2, 6) 
g.addEdge(0, 3, 5) 
g.addEdge(1, 3, 15) 
g.addEdge(2, 3, 4) 
g.KruskalMST() 

# And that, my dear friend, is how you use Kruskal’s algorithm to find the MST of a graph in Python! 
# Go on and conquer the world with your newfound powers!!

