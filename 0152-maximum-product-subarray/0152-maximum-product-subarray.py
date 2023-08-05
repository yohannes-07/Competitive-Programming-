class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = minProd = maxProd = nums[0]
        
        for n in nums[1:]:
            maxTemp = max(n * maxProd, n, n * minProd)
            minProd = min(n * minProd, n, n * maxProd)
            
            maxProd = maxTemp
            res = max(maxProd, res)
            
        return res