class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        hashSet = set()
        
        def backtrack(start, acc):
            if start >= len(nums):
                
                if tuple(acc) not in hashSet and  len(acc) >= 2:
                    res.append(acc[:])
                    hashSet.add(tuple(acc))
                    
                return
            
            if len(acc) >= 2 :
                if tuple(acc) not in hashSet:
                    res.append(acc[:])
                    hashSet.add(tuple(acc))
            
            for i in range(start, len(nums)):
              
                if not acc or  acc[-1] <= nums[i]:
                    acc.append(nums[i])
                    backtrack(i + 1,  acc)
                    
                    acc.pop()
                      
                
        backtrack(0, [])
            
        return res