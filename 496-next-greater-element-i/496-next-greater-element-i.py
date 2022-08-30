class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        

        output=[]


        for num in nums1:

            num_idx=nums2.index(num)

            found= False
            for i in range(num_idx+1,len(nums2)):

                if nums2[i] > num:

                    output.append(nums2[i])
                    found=True 

                    break

            if not found:

                output.append(-1)

        return output 

                    