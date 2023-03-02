class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        # sort and reverse to get max possible permutation
        nums.sort()  
        nums, n = nums[::-1] , len(nums)
        
        #find how many times each query is repeated
        queries = [0] * (n + 1)
        for start, end in requests:
            queries[start] += 1
            queries[end + 1] -= 1
            
        #calculate the prefix sum to get how many times a query should be done
        for i in range(1, n + 1):
            queries[i] += queries[i-1]
            
        #pop the last query (just added to handle error)
        queries.pop()
        
        #match higher values of nums with more repeated queries
        queries.sort()
        queries = queries[::-1]
        
        #find the max total sum
        max_total_sum = 0
        for i in range(n):
            max_total_sum += queries[i]  * nums[i]
            
        return max_total_sum % (10 ** 9 + 7)
        
        
        
        
        