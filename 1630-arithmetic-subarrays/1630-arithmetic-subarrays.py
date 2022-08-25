class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        


        output = [True]*len(l)

        for i in range(len(l)):

            arr = nums[l[i]:r[i]+1]

            arr.sort()

            newarr = []
            j=0

            while j <= len(arr) -2:

                newarr.append(arr[j+1] - arr[j])
                j += 1
                
            #use set to put the diff as one value.
            #without duplicates so that it forms arithmetic  progression
            newarr = list(set(newarr))

            if len(newarr) != 1:

                output [i] = False

        return output 