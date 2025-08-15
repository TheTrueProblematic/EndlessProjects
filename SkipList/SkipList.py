
# Woah-ho-ho, look at you mystery adventurer! You've stumbled upon a magical artifact called "SkipList".
# It's a fascinating construction, allowing rapid-fire searches (`O(log n)` time complexity, if you ask) in a list.
# It maintains multiple 'layers' of the list, with each layer skipping a few elements in-between.
# Brace yourself for a ride through SkipList land, without any dependencies on horses (or external packages), or the need for any enchantments (internet or API access)!

import random 

class Node:
    # Here lies our brave Node, the fundamental soldier of the SkipList army!
    def __init__(self, height = 0, elem = None):
       self.neighbors = [None]*height # Who are the node's comrades in arms on each level?
       self.elem = elem # The symbol of its tribe, or the actual element

class SkipList:
    # Behold, the magnificent SkipList kingdom, where the nodes find their purpose!
    def __init__(self):
        self.head = Node() # The head of the kingdom, leading the way
        self.len = 0 # Kingdom's strength, no. of elements in the list
        self.maxHeight = 0 # Maximum structural height
        
    def __len__(self):
        # Someone asked about the strength of our kingdom? 
        return self.len 

    def find(self, elem, update = None):
        # Time for a recon mission to find a node! 
        if update == None:
            update = self.updateList(elem)
        if len(update) > 0:
            candidate = update[0].neighbors[0]
            if candidate != None and candidate.elem == elem:
                return candidate
        return None
        
    def contains(self, elem, update = None):
        # Is one of our nodes carrying this symbol? 
        return self.find(elem, update) != None

    def randomHeight(self):
        # Conjure a random height for a node who's about to join the SkipList kingdom!
        height = 1
        while random.randint(1, 2) != 1:
            height += 1
        return height

    def updateList(self, elem):
        # Let's figure out where to place a new warrior node. 
        update = [None]*self.maxHeight
        x = self.head
        for i in reversed(range(self.maxHeight)):
            while x.neighbors[i] != None and x.neighbors[i].elem < elem:
                x = x.neighbors[i]
            update[i] = x
        return update
        
    def insert(self, elem):
        # Sound the horns! A node is joining our SkipList kingdom!
        _node = Node(self.randomHeight(), elem)
        
        self.maxHeight = max(self.maxHeight, len(_node.neighbors))
        while len(self.head.neighbors) < len(_node.neighbors):
            self.head.neighbors.append(None)
            
        update = self.updateList(elem)            
        if self.find(elem, update) == None:
            for i in range(len(_node.neighbors)):
                _node.neighbors[i] = update[i].neighbors[i]
                update[i].neighbors[i] = _node
            self.len += 1

    def remove(self, elem):
        # A moment's silence please, a node is leaving the kingdom.
        update = self.updateList(elem)
        x = self.find(elem, update)
        if x != None:
            for i in reversed(range(len(x.neighbors))):
                update[i].neighbors[i] = x.neighbors[i]
                if self.head.neighbors[i] == x:
                    self.head.neighbors[i] = None
            self.len -= 1

# And it's done! Magic of SkipList unleashed! Off you go to explore and play around with it, dear adventurer!

