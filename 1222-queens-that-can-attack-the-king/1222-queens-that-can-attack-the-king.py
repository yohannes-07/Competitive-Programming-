class Solution:
    def attackerChecker(self, xKing,yKing, direction, queens, res):
        if xKing < 0 or xKing >= 8 or yKing <0 or yKing >= 8:
            return
    
        if [xKing, yKing] in queens:
            res.append([xKing, yKing])
            return 
    
        return self.attackerChecker(xKing + direction[0], yKing + direction[1], direction, queens, res)
    
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        res = []
        
        
        xKing,yKing = king
    
        directions = [[0,1], [0,-1], [1, 0], [-1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]
        for direction in directions:
            self.attackerChecker(xKing,yKing,direction, queens, res)            
        
        return res