# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = 0
 
        def dfs(root):
            nonlocal ans
            
            if not root:
                return [0, 0]
      
            count = 1
            left = dfs(root.left)
            right = dfs(root.right)
            
            summ = root.val + left[1] + right[1]
            count += left[0] + right[0]
            
            if root.val == int(summ/count):
                ans += 1
          
            return [count, summ]
        
        dfs(root)
        
        return ans