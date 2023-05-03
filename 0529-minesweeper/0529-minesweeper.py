class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        m, n = len(board), len(board[0])
        directions = [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)]
        
        def inBound(row, col):
            return 0<= row < m and 0 <= col < n
   
        
        def dfs(row, col):
            
            if not inBound(row, col) or board[row][col] != "E":
                return
             
            mines = 0
            for dr, dc in directions:
                r1, c1 = row + dr, col + dc
                
                if inBound(r1, c1) and board[r1][c1] == "M":
                    mines += 1
                    
            if mines:
                board[row][col] = str(mines)
                return 
                  
            else:
                board[row][col] = "B"
                
            for dr, dc in directions:
                r, c = row + dr, col + dc

                if inBound(r, c):
                    dfs(r, c)


           
        
   
        if board[click[0]][click[1]] == 'M':
                board[click[0]][click[1]] = 'X'
                return board
            
        dfs(click[0], click[1])
        return board
                