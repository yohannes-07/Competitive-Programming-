class Solution(object):
    def shortestSubarray(self, nums, k):
       
  #cumulative sum of nums
        cumulatives =[0]
        for num in nums:

            cumulatives.append(cumulatives[-1] + num)

        deq = deque()
        output = len(cumulatives)# output may be changed
        
#access each cumulative sum with its index

        for i, cumul in enumerate(cumulatives):

            while deq and cumul - cumulatives[deq[0]] >= k:

                output = min(output, i - deq.popleft())

            while deq and cumul < cumulatives[deq[-1]]:

                deq.pop()

            deq.append(i)

        if output < len(cumulatives):

            return output

        return -1
        
        
        