# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        # O(3n) solution
        # uses the same concept from validate if a tree is bst
        i = 0
        n = len(preorder)
        
        def dfs(nums, upperBound):
            nonlocal n, i
 
        
            if i == n or nums[i] > upperBound:
                return 
            
            
            root = TreeNode(nums[i])
            i += 1
            
            root.left = dfs(nums, nums[i -1])
            root.right = dfs(nums,  upperBound)
        
            return root
        
        return dfs(preorder, float("inf"))
        
        