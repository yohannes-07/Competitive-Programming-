# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        duplicateSubtrees = []
        subtrees = defaultdict(int)
        
        def dfs(root, path):
            if not root:
                return "#"
        
            left = dfs(root.left, path)
            right = dfs(root.right, path)
            
            path += str(root.val) + "," + left + "," + right
            
            subtrees[path] += 1
            if subtrees[path] == 2:
                duplicateSubtrees.append(root)
            
            return path
            
        dfs(root, "")
       
        return duplicateSubtrees