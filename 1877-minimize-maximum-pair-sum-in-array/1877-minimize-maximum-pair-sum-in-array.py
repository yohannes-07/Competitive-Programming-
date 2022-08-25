class Solution(object):
    def minPairSum(self, nums):
        nums.sort()
        res= []
        i,j=0,len(nums)-1
        while i<=j:
            res.append([nums[i], nums[j]])
            i += 1
            j -=1
        max= res[0][0] + res[0][1]
        for k in range(1, len(res)):
            if res[k][0] + res[k][1] > max:
                max = res[k][0] + res[k][1]
                
        return max
        
        

        