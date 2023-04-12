# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        path = []
        
        def dfs(root):
         
            path.append(str(root.val))
            
            if root.left:
                path.append("(")
                dfs(root.left)
                path.append(")")
            
            if root.right and not root.left:
                path.append("()")
                
            if root.right:
                path.append("(")
                dfs(root.right)
                path.append(")")
                
            
        dfs(root)
        return "".join(path)