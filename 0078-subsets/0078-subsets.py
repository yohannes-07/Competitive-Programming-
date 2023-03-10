class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def backtrack(i, acc):
        
            if i >= n:
                res.append(acc[:])
                return
            
            #descion to add the curr value
            acc.append(nums[i])
            backtrack(i + 1, acc)
            acc.pop()
            
            # descion not to add the curr value
            # so call the function by passing the next value as an argument
            
            backtrack(i + 1, acc)
            
            
        backtrack(0, [])
        
        return res