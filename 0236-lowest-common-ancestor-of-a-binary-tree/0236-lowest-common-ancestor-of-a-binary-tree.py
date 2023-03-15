# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(root):
            
            #if either p or q are found return thar root
            if root == p or root == q:
                return root
            
            #search to the left and right until u get either p or q
            left = None
            right = None
            if root.left:
                left = dfs(root.left)
                
            if root.right:
                right = dfs(root.right)
                
             # both are found and have same parent
            if left and right:
                return root
            
            #one of them has found or both aren't found
            return left or right
        
        return dfs(root)