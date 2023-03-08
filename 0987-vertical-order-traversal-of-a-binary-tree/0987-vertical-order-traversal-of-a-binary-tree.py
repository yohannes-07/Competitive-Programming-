# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        dic = defaultdict(list)
        min_col = float('inf')
        max_col = float('-inf')
        
        def dfs(root, col, row):
            nonlocal min_col, max_col
            
            if not root:
                return
            
            dic[col].append((row, root.val))
            
            min_col = min(min_col, col)
            max_col = max(max_col, col)
            
            dfs(root.left, col - 1, row + 1)
            dfs(root.right, col + 1, row + 1)
            
        dfs(root, 0, 0)

        res = []
        for i in range(min_col, max_col + 1):
            dic[i].sort()
            
            res.append(list(map(lambda x: x[1], dic[i])))
            
        return res
            
        