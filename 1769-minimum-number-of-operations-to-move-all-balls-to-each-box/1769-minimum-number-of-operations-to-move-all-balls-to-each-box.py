class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0] * n
      
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                else:
                    if boxes[j] == "1":
                        ans[i] += abs(i-j)
                    
        return ans
            