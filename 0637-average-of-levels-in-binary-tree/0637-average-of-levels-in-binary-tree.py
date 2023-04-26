# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        res = []
        queue = deque([root])
        
        while queue:
            length = len(queue)
            tot = 0
            
            for _ in range(length):
                curr = queue.popleft()
                tot += curr.val 
                
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
                 
                
            res.append(tot / length)
            
                
        return res