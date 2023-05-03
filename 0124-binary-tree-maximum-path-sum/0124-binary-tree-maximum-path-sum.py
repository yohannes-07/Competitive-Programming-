# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        maxPathSum = float("-inf")
        
        def dfs(root):
            nonlocal maxPathSum 
            
            if not root: return 0
            
            leftPathSum = max(dfs(root.left), 0)
            rightPathSum = max(dfs(root.right), 0)
            
            maxPathSum = max(maxPathSum, leftPathSum + rightPathSum + root.val)
            
            return max(leftPathSum + root.val, rightPathSum + root.val)
        
        dfs(root)
        
        return maxPathSum
        