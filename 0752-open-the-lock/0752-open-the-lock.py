class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque([("0000" , 0)])
        visited = set(deadends)
        
        def getNeighbors(lock):
            res = []
            
            for i in range(4):
                increamented = str((int(lock[i]) + 1) % 10 )
                res.append(lock[:i] + increamented + lock[i+1:])
                
                decremented  = str((int(lock[i]) - 1 + 10) % 10 )
                res.append(lock[:i] + decremented + lock[i+1:])
                
            return res
        if "0000" in visited: return -1
        
        while queue:
            lock, turns = queue.popleft()
            if lock == target: return turns
         
            for neighbor in getNeighbors(lock):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, turns  + 1))
            
            
           
        return -1
                    
                
                
                
                
        