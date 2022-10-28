class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i, num in enumerate(nums):
            if num in dic:
                if abs(i - dic[num]) <= k:
                    return True
            dic[num] = i
            
        return False