"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        def dfs(root):
            
            if not root:
                return 0
            
            children = root.children
            maxDepth = 0
            
            for child in children:
                currDepth = dfs(child)
                maxDepth = max(maxDepth, currDepth )
                
            return maxDepth + 1
        
        return dfs(root)