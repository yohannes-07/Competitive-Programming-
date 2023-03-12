# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        duplicate_elems = []
        def dfs(root):
            if not root:
                return 
            
            dfs(root.left)
            duplicate_elems.append(root.val)
            dfs(root.right)
            
        dfs(root)
        
        counter = Counter(duplicate_elems)
        most_freq = max(counter.values())
        mode = []
        
        for key, value in counter.items():
            if value == most_freq:
                mode.append(key)
                
        return mode