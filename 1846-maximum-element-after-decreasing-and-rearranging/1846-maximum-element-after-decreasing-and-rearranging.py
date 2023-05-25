class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        count = 0
        for curr in sorted(arr):
            if curr > count:
                count += 1
                
        return count