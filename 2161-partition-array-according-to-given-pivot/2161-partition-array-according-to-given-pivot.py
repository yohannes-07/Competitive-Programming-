class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        leftNums = []
        rightNums  = []
        middleNums = []
        
        for num in nums:
            if num < pivot:
                leftNums.append(num)
            
            elif num == pivot:
                middleNums.append(num)
            
            else:
                rightNums.append(num)
                
        arrangedArr =  leftNums + middleNums + rightNums
        
        return arrangedArr