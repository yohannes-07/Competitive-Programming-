class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        R, C = len(img), len(img[0])
        ans = [[0]*C for _ in img]
        
        for r in range(R):
            for c in range(C):
               
                rS = 0 if r == 0 else r-1
                rE = R-1 if r == R-1 else r+1
                # indices of starting and ending column
                cS = 0 if c == 0 else c-1
                cE = C-1 if c == C-1 else c+1
                # sum of each row
                rows_sum = [sum(row[cS:cE+1]) for row in img[rS:rE+1]]
                # sum of rows
                total = sum(rows_sum)
                # number of elements in area
                cunt = (rE-rS+1)*(cE-cS+1)
                
                ans[r][c] = int(total/cunt)
                
        return ans