# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        def dfs(root, level):
            
            if not root:
                return 
            
            #check if ther is empty array inside res
            # to put new  values with the same level
            if len(res) < level:
                res.append([])

            res[level -1].append(root.val)
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
        
        dfs(root, 1)
        
        ans = []
        for num in res:
            ans.append(num[-1])
            
        return ans