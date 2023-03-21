# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        res = 0
        dic = {0:1}
        
        def dfs(root, acc):
            nonlocal res
            
            if not root:
                return 
            
            acc += root.val
            res += dic.get(acc - targetSum, 0 )
            
            
            dic[acc] = dic.get(acc, 0) + 1
            
            dfs(root.left, acc)
            dfs(root.right, acc)
            
            if acc in dic:
                dic[acc] -= 1
            
        dfs(root, 0)
        return res