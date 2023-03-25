class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        counter = Counter(nums)
   
        return max(counter.values()) > 1
        
        