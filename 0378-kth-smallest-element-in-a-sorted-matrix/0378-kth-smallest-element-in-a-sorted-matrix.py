class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                
                arr.append(matrix[i][j])
        
        heapify(arr)
        
        for _ in range(k-1):
            heappop(arr)
            
        return arr[0]