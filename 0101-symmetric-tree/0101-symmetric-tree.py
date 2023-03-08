# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True
        
        if  root.left and root.right and root.left.val != root.right.val:
            return False
        
        if (root.left and not root.right) or (root.right and not root.left):
            return False
      
        def dfs(root1, root2):
            if not root1 and not root2:
                return True
        
            if root1 and not root2:
                return False

            elif root2 and not root1:
                return False


            left = dfs(root1.left, root2.right)
            right =  dfs(root1.right, root2.left)
            
            return left and right and  root1.val == root2.val
        
        return dfs(root.left, root.right)
        
        