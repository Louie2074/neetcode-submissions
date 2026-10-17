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
        old_to_new = {}
        adj_list = []
        seen = set()
        q = deque([])
        if not node:
            return None
        
        q.append(node)
        while len(q) > 0:
            curr_node = q.popleft()
            copy_node = Node(curr_node.val)
            if curr_node in old_to_new:
                copy_node = old_to_new[curr_node]
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
            adj_list.append(copy_node)
            

        return adj_list[0]




