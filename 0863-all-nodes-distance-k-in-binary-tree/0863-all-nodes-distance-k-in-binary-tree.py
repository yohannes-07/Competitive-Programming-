# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        
        def dfs(curr, parent):
            if not curr: return 
            
            if parent: graph[curr.val].append(parent.val)
            
            if curr.left: 
                graph[curr.val].append(curr.left.val)
                dfs(curr.left, curr)
                
            if curr.right: 
                graph[curr.val].append(curr.right.val)
                dfs(curr.right, curr)
                
        dfs(root, None)
        
        queue = deque([(target.val, 0)])
        res, visited = [], set()
        
        while queue:
            curr, dist = queue.popleft()
            visited.add(curr)
            
            if dist == k:
                res.append(curr)
                
            elif dist < k:
                
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        queue.append((neighbor, dist + 1))
                    
        
        return res