# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        moves = 0
        
        def dfs(root):
            nonlocal moves
            
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            moves += abs(left) + abs(right)
            
            return root.val -1 + left + right
        
        dfs(root)
        return moves