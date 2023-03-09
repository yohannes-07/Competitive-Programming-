# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        min_val = float('-inf')
        max_val = float('inf')
        
        def dfs(root, min_val, max_val):
            if not root:
                return True

            if root.val <= min_val or root.val >= max_val:
                return False

            left_valid = dfs(root.left, min_val, root.val)
            right_valid = dfs(root.right, root.val, max_val)

            return left_valid and right_valid

        return dfs(root, min_val, max_val)