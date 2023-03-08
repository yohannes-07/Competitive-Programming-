# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        min_val = min(p.val, q.val)
        max_val = max(p.val, q.val)
        
        def dfs(node):
            if min_val <= node.val and node.val <= max_val:
                return node
            
            elif min_val < max_val < node.val:
                return dfs(node.left)
            
            else:
                return dfs(node.right)
            
        return dfs(root)