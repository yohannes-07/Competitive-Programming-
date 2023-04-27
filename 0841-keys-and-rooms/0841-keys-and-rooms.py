class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([0])
        visited = set()
        
        while queue:
            curr = queue.popleft()
            
            if curr not in visited:
                visited.add(curr)
                
                for key in rooms[curr]:
                    queue.append(key)
                        
        
        return len(visited) == len(rooms)