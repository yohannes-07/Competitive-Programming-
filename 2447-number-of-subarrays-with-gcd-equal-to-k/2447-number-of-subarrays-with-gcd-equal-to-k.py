class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        
        # gcd distributive property
        def gcd(a, b):
            if not b:
                return a
            return gcd(b, a % b)
        
        no_of_subarrays = 0
        
        for i in range(len(nums)):
            val = nums[i]
            for j in range(i, len(nums)):
             
                #compute the gcd of the first two values and pass it as an argument with the third num
                # and continues ...variant of distibutive property
                
                val = gcd(val, nums[j])
             
                if val == k:
                    no_of_subarrays += 1
                
                elif val < k:
                    break
                    
        return no_of_subarrays
            