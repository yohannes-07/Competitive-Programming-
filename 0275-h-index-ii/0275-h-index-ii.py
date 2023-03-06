class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        left, right = 0, len(citations) -1
        
        while left <= right:
            mid = left + (right - left)// 2
            
            if len(citations) - mid > citations[mid]:
                left = mid + 1
            
            else:
                right = mid - 1
                
        return len(citations) - left
            
        