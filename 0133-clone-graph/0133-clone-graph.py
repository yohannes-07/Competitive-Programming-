"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return
        copy = {}
        
        def dfs(node):
            copy[node] = Node(node.val)

            for neighbour in node.neighbors:
                if neighbour not in copy:
                    dfs(neighbour)
                
                copy[node].neighbors.append(copy[neighbour])
                
        
        dfs(node)
        return copy[node]