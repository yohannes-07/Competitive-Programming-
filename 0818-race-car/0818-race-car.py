class Solution:
    def racecar(self, target: int) -> int:
        # moves, position and speed
        queue = deque([(0, 0, 1)])
        visited = set()
        
        while queue:
            moves, pos, speed = queue.popleft()
            if pos == target: return moves
            
            if (pos, speed) not in visited:
                visited.add((pos, speed))
                queue.append((moves + 1, pos + speed, speed * 2))
                
                if pos + speed > target and speed > 0:
                    speed = -1
                    queue.append((moves + 1, pos, speed))
                    
                elif pos + speed < target and speed < 0:
                    speed = 1
                    queue.append((moves + 1, pos, speed))
                    
                    
                    