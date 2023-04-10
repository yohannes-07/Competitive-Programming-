class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        res  = 0
        
        def dfs(i):
            
            for j in range(len(isConnected[i])):
                if isConnected[i][j] and j not in visited:
                    
                    visited.add(j)
                    dfs(j)
        res = 0        
        for i in range(n):
            
            if i not in visited:
                visited.add(i)
                dfs(i)
                res += 1
            
        return res
        
                
                