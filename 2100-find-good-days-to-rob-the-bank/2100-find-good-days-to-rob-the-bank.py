class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        postfix =  [0] * n
        prefix = [0]  * n
        for i in range(1, n):
             prefix[i] = prefix[i-1] + 1 if security[i] <= security[i-1] else  0
                  
        for i in range(n-2, 0, -1):
            postfix[i] = postfix[i+1] + 1 if security[i+1] >= security[i] else 0
                
        ans = []
        for i in range(n):
            if prefix[i] >= time and postfix[i] >= time:
                ans.append(i)
        return ans