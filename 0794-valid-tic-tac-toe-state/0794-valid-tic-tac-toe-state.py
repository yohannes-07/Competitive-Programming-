class Solution:
    def canWin(sef, board,  player): 
            
        #check elements in a row
        if board[0][0] == board[0][1] == board[0][2] == player:
            return True

        if board[1][0] == board[1][1] == board[1][2] == player:
            return True

        if board[2][0] == board[2][1] == board[2][2] == player:
            return True

        #check elements in a column
        if board[0][0] == board[1][0] == board[2][0] == player:
            return True

        if board[0][1] == board[1][1] == board[2][1] == player:
            return True

        if board[0][2] == board[1][2] == board[2][2] == player:
            return True

        #check elememts diagonally
        if board[0][0] == board[1][1] == board[2][2] == player:
            return True

        if board[0][2] == board[1][1] == board[2][0] == player:
            return True

        return False

        
    def validTicTacToe(self, board):
        xMoves = 0
        oMoves = 0

        for i in range(3):
            for j in range(3):
                
                if board[i][j] == "X":
                    xMoves += 1
                    
                elif  board[i][j] == "O":
                    oMoves += 1

        if oMoves > xMoves or xMoves - oMoves > 1: 
            return False

        if xMoves > 2:
            if xMoves == oMoves and self.canWin(board, 'X'): 
                return False
            if xMoves!= oMoves and self.canWin(board, 'O'): 
                return False

        return True
        