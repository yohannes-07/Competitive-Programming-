class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        dic = {}
        mstack = []
        
        for num in nums2: 
            while mstack and mstack[-1] <= num:
                popped = mstack.pop()
                dic[popped] = num
            
            mstack.append(num)
            
   
        for num in nums1:
            res.append(dic.get(num, -1))
                         
        return res
            