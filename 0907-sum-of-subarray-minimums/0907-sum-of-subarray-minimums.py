class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        res = 0
        arr.append(0)
        
        for currIdx, val in enumerate(arr):
            
            # it pops the previous min elem
            # find the no of subarrays to the left the value has been minimum(including its index)
            # find the no of subarrays  to the right it's been minimum until new min elem is found
            # multiplies them to get total subarrays it's has been minimum
            
            while stack and val < stack[-1][1] :
                index, value = stack.pop()
                leftMostIdx = stack[-1][0] if stack else -1
                
                res += (index - leftMostIdx) * (currIdx - index ) * arr[index]
            
        
            stack.append((currIdx, val))
        
        return res % (10 ** 9 + 7)