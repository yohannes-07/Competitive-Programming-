class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        next_greater = {}
        min_stack = []
        
        for num in nums2: 
            while min_stack and min_stack[-1] <= num:
                popped = min_stack.pop()
                next_greater[popped] = num
            
            min_stack.append(num)
            
   
        for num in nums1:
            res.append(next_greater.get(num, -1))
                         
        return res
            