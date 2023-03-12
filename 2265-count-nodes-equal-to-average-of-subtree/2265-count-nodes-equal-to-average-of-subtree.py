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
            leftCount = dfs(root.left)
            rightCount = dfs(root.right)
            
            summ = root.val + leftCount[1] + rightCount[1]
            count += leftCount[0] + rightCount[0]
            
            if root.val == int(summ/count):
                ans += 1
          
            return [count, summ]
        
        dfs(root)
        
        return ans