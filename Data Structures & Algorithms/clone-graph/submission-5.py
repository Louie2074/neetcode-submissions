"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        def dfs(node, old_to_new):
            if node in old_to_new:
                return old_to_new[node]

            copy_node = Node(node.val)
            old_to_new[node] = copy_node
            copy_neighbors = []
            for neighbor in node.neighbors:
                copy_neighbors.append(dfs(neighbor,old_to_new))

            copy_node.neighbors = copy_neighbors
            return copy_node

        if node is None:
            return None
            
        old_to_new = {
            
        }
        
        dfs(node,old_to_new)
        return old_to_new[node]


