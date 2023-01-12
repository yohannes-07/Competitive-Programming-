class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        m = len(strs)
        n = len(strs[0])
        
        for col in range(n):
            for row in range(m - 1):
                
                if strs[row][col]  > strs[row + 1][col]:
                    res += 1
                    break
        return res