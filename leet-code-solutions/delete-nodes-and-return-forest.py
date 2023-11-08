# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        ans = []
        
        def dfs(root):
            if not root: return 
            
            root.left = dfs(root.left)
            root.right = dfs(root.right)
            
            if root.val in to_delete:
                
                if root.left:
                    ans.append(root.left)
                
                if root.right:
                    ans.append(root.right)
                    
                return None 
            
            return root
        
        root1 = dfs(root)
        
        if root1:
            ans.append(root1)
            
        return ans
            