class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = {}                                
        res = []
        stack = []                              
        
        for n2 in nums2:
            while stack and n2 > stack[-1]:     
                ans[stack.pop()] = n2          
            stack.append(n2)
        
        for n1 in nums1:                        
            res.append(ans.get(n1, -1))        
                                            
        
        return res
