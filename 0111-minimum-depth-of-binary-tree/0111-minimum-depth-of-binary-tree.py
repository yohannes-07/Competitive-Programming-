# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        res  = float("inf")
        
        def dfs(root, depth):
            nonlocal res
            
            if not root: return 
            
            if not root.left and not root.right:
                res  = min(res, depth + 1)
        
            
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
            
        
        dfs(root, 0)
        
        return res
        
                
                