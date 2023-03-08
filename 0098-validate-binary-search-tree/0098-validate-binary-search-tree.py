# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        sorted_arr = []
        def dfs(root):
            if not root:
                return 
            
            dfs(root.left)
            sorted_arr.append(root.val)
            dfs(root.right)
            
        dfs(root)
        
        for i in range(1, len(sorted_arr)):
            if sorted_arr[i] <= sorted_arr[i-1]:
                return False
            
        return True
            
            
            