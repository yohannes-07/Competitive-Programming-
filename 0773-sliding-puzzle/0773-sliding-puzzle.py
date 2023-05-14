class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        self.possibleMoves = {0:[1,3], 1:[0,2,4], 2:[1,5], 3:[0,4], 4:[1,3,5], 5:[2,4]}  
        
        start =  ''.join(map(str, [element for sublist in board for element in sublist]))
        goal = "123450"
        
        queue = deque([(start, 0)])
        visited = set()
        
        while queue:
            
            curr , moves = queue.popleft()
            if curr == goal: return moves
            
            visited.add(curr)
            
            for neigh in self.getNeighbors(curr):
                if neigh not in visited:
                    queue.append((neigh, moves + 1))
            
        
        return -1
        
    def getNeighbors(self, curr):
        zeroIdx = curr.find("0")
        neighbors = []
        
        for i in self.possibleMoves[zeroIdx]:
            temp = list(curr)
         
            temp[i], temp[zeroIdx] = temp[zeroIdx], temp[i]
       
            neighbors.append("".join(temp))
            
        return neighbors