# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
     
        res = 0
        def dfs(root, num):
            nonlocal res
            
            if not root:
                return
            
            num += str(root.val)
            
            left = dfs(root.left, num )
            right = dfs(root.right, num)
            
            if not left and not right:
                res += int(num)
               
            return root
            
       
        dfs(root, "")
        
        return res
    