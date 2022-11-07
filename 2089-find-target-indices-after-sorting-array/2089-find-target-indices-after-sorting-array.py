class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i, v in enumerate(sorted(nums)):
            if v == target:
                res.append(i)
                
        return res