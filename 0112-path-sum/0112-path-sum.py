# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(root, targetSum):
     
            if not root:
                return False
            
            if not root.left and not root.right and root.val == targetSum:
                return True
            
            left = dfs(root.left, targetSum - root.val)
            right = dfs(root.right, targetSum - root.val)
            
            return left or right

            
        return dfs(root, targetSum)
        