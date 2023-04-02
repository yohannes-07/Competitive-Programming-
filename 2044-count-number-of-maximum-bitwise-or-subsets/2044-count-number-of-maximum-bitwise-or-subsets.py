class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        subsets = []
        max_ = 1
        
        def backtrack(i, acc):
            nonlocal max_, subsets
            
            if i >= len(nums):
                if not acc:
                    return
                
                res = acc[0]
                for j in range(1, len(acc)):
                    res |= acc[j]
         
                if res > max_:
                    subsets = [acc[:]]
                    max_ = res

                elif res == max_:
                    subsets.append(acc[:])
                
            
                return

       
            acc.append(nums[i]) 
            
            backtrack(i + 1, acc)
            
            acc.pop()
    
            backtrack(i + 1, acc)
            
            
        backtrack(0, []) 
        return len(subsets)
            
       
            