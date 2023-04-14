# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, parent: TreeNode, grandParent: TreeNode):
            if not node:
                return
            
            nonlocal answer
            
            if parent and grandParent and grandParent.val % 2 == 0:
                answer += node.val
            dfs(node.left, node, parent)
            dfs(node.right, node, parent)

        answer = 0
        dfs(root, None, None)
        return answer