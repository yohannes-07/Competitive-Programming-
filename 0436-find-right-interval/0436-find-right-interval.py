class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        def helper(intervals, target):
            left, right = 0, len(intervals)
            best = -1
            
            while left < right:
                mid = left + (right - left) // 2

                if intervals[mid][0] >= target:
                    right = mid
                    best = indices[intervals[mid][0]]

                else:
                    left = mid + 1

            return best
        
        
        
        indices = {}
        res  = [-1] * len(intervals)
        
        for i, interval in enumerate(intervals):
            indices[interval[0]] = i
        
        intervals.sort()
        
        for interval in intervals:
            target = interval[1]
            result = helper(intervals, target)  
            index = indices[interval[0]]
            res[index] = result
            
        return res
            
            