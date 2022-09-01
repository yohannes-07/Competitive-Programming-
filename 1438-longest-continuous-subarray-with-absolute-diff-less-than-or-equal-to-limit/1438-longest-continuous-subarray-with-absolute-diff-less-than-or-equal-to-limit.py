class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxQueue = deque()
        minQueue = deque()
      
        output = 0
        start = 0
        i = 0
        while i < (len(nums)):
            
            while minQueue and minQueue[-1] > nums[i]:
                minQueue.pop()
                
            minQueue.append(nums[i])  
            
            while maxQueue and maxQueue[-1] < nums[i]:
                maxQueue.pop()
                   
            maxQueue.append(nums[i])
            
            if maxQueue[0] - minQueue[0] <= limit :
                output = max (output , i - start + 1 )
            else :
                if maxQueue [0] == nums [start] :
                    del maxQueue[0]
                    
                if minQueue [0] == nums [start] :
                    del minQueue[0]
                    
                start += 1
                
            i += 1         
        return output
        