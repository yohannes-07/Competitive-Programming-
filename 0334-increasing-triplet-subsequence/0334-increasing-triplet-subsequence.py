class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float("inf")
        
        for num in nums:
            if num > second: return True
            
            elif num > first:
                second = min(second, num)
                
            else:
                first = num
                
        return False
        
        