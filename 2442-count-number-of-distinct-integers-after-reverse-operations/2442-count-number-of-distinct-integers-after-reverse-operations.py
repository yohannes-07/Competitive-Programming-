class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        distinict_nums = set(nums)
        for num in nums:
            reversed_digit = int(str(num)[::-1])
            distinict_nums.add(reversed_digit)
            
            
        return len(distinict_nums)
