# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        count = 0
        def dfs(root, prevMax):
            nonlocal count
            
            if not root:
                return 0
        
            count += 1 if root.val >= prevMax else 0
            prevMax = max(prevMax, root.val)
    
            dfs(root.left, prevMax)
            dfs(root.right, prevMax)
            
        dfs(root, float('-inf'))
        
        return count