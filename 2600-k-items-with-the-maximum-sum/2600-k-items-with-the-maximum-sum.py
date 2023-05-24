class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        arr = []
        summ = 0
        for _ in range(numOnes):
            arr.append(-1)
            
        for _ in range(numZeros):
            arr.append(0)
            
        for _ in range(numNegOnes):
            arr.append(1)
          
        heapify(arr)
        
        for _ in range(k):
            summ -= heappop(arr)
            
        return summ 
        
            
        