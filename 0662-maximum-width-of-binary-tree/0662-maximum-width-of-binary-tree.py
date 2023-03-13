# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        res = 0
        leftMostNodesIdx = {}
        
        def dfs(root, currIdx = 0, level = 0):
            nonlocal res
            
            if not root:
                return 
            
            #only the first left most node position recorded
            if level not in leftMostNodesIdx:
                leftMostNodesIdx[level] = currIdx
                
            res = max(res, currIdx - leftMostNodesIdx[level] + 1)
            
            dfs(root.left, currIdx * 2, level + 1)
            dfs(root.right, currIdx * 2 + 1, level + 1)
            
        dfs(root, 0, 0)
        
        return res