class Solution:
    def isValidSudoku(self, board):
        # Validate each row
        for r in range(9):
            hashSet = set()
            for c in range(9):
                if board[r][c] != '.':
                    if board[r][c] in hashSet:
                        return False
                    hashSet.add(board[r][c])
        
        # Validate each column
        for c in range(9):
            hashSet = set()
            for r in range(9):
                if board[r][c] != '.':
                    if board[r][c] in hashSet:
                        return False
                    hashSet.add(board[r][c])
        
        # Validate each box
        r, c = 0, 0
        while True:
            hashSet = set()
            for i in range(r, r+3):
                for j in range(c, c+3):
                    if board[i][j] != '.':
                        if board[i][j] in hashSet:
                            return False
                        hashSet.add(board[i][j])
            c += 3
            if c == 9:
                r += 3
                # Break if we have verified all 9 boxes
                if r == 9:
                    break
                c = 0
        return True
        