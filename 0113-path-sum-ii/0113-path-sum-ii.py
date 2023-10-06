# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        
        def dfs(root, path, currSum):
     
            if not root:
                return 
            
            if not root.left and not root.right and (root.val + currSum) == targetSum:
                path.append(root.val)
                res.append(path.copy())
                return 
            
            
            dfs(root.left, path+[root.val], currSum + root.val)
            dfs(root.right, path+[root.val],  currSum + root.val)
            

        dfs(root, [], 0)
                                                     
        return res