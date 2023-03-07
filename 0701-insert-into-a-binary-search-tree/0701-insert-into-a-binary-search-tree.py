# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        dummy = root
        
        if not root:
            dummy = TreeNode(val)
            return dummy
        
        def helper(root, parent = None):
            if not root:
                
                if val < parent.val:
                    parent.left = TreeNode(val)
                else:
                    
                    parent.right = TreeNode(val)
        
                return 

            if val < root.val:
                 helper(root.left, root)

            else:
                helper(root.right, root)
        helper(root)
        return dummy 