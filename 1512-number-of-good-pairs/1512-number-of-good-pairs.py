class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        #similar to #2506 Count Pairs of similar strings
        dic = {}
        res = 0
        
        # put the frequency of each num in dic
        for num in nums:
            if num in dic:
                dic[num] += 1
                
            else:
                dic[num] = 1
                
        # iterate through the dic value and find no of pairs of similar strings
        # use combination rule to find no of pairs => c(n, p) = n!/((n-p)! * p!)
        #p is 2 in this problem ....the combination rule satisfies i < j rule

        for value in dic.values():
            if value == 1:
                continue
                
            else:
                comb = (math.factorial(value))/(math.factorial(value - 2) * 2)
                res += int(comb)
                
        return res