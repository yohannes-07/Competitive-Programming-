class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        mini = 0
        summ = 0
        for i in nums:
            summ += i
            mini = min(mini, summ)
        return -mini + 1