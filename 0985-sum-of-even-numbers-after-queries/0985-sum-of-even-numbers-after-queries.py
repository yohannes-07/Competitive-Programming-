class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        ans = []
        # calculate initial sum of even values of the nums array
        summ = 0
        for num in nums:
            if  num % 2 == 0:
                summ += num
        
        for query in queries:
            value = query[0]
            idx = query[1]
            
            #4 possibilities for the num in nums and the value in each query
            #if both are odd, add their sum and append in the ans array
            if value % 2 and nums[idx] % 2:
                summ += value + nums[idx]
             
            #if num in nums is even and the value in query is odd, subtract num from the sum as it their sum
            # is odd
            elif value % 2 and nums[idx] % 2 == 0:
                summ -= nums[idx]
             
            #if both are even, add the query value....the num has already been added
            elif not value % 2 and not nums[idx] % 2:
                summ += value
           
            ans.append(summ)
            
            #update the num value in nums array as the question says
            nums[idx] = nums[idx] + value
            
        return ans
            
      