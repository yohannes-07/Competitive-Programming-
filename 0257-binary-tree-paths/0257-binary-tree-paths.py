# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        res = []
        def backtrack(root, path):
            

            if path:
                path += "->" + str(root.val)
            else:
                path += str(root.val)
            
            if not root.left and not root.right:
                res.append(path)
                 
            if root.left:
                backtrack(root.left, path)
                
            if root.right:
                
                backtrack(root.right, path)
            
        backtrack(root, "")
        
        return res