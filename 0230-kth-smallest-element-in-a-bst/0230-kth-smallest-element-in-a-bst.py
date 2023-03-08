# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sorted_arr = []
        def dfs(root):
            if not root:
                return 
            
            dfs(root.left)
            sorted_arr.append(root.val)
            dfs(root.right)
            
        dfs(root)
        
        return sorted_arr[k-1]