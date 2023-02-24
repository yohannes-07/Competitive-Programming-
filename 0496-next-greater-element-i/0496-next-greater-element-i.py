class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        dic = {}
        mstack = []
        for num in nums2: 
            while mstack and mstack[-1] <= num:
                popped = mstack.pop()
                dic[popped] = num
            
            mstack.append(num)
            
   
        for i, num in enumerate(nums1):
            res[i] = dic.get(num, -1)
                         
        return res
            