"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        seen = set()
        q = deque([])

        if not node:
            return None
        old_to_new = {
            node: Node(node.val)
        }
        q.append(node)

        while len(q) > 0:
            curr_node = q.popleft()
            copy_node = copy_node = old_to_new[curr_node]
            copy_neighbors = []

            for neighbor in curr_node.neighbors:
                if neighbor in old_to_new:
                    copy_neighbors.append(old_to_new[neighbor])
                else:
                    copy_neighbor_node = Node(neighbor.val)
                    old_to_new[neighbor] = copy_neighbor_node
                    copy_neighbors.append(copy_neighbor_node)

                if neighbor not in seen:
                    q.append(neighbor)
                    seen.add(neighbor)
            
            copy_node.neighbors = copy_neighbors            

        return old_to_new[node]




