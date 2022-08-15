class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sortedNums = sorted(nums)
        output = []
        for i, j in enumerate(sortedNums):
            if j == target:
                output.append(i)
        return output