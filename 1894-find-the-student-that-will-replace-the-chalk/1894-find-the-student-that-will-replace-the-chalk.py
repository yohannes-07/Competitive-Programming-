class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        prefix = []
        prefix.append(chalk[0])
        
        for i in range(1, len(chalk)):
            prefix.append(prefix[-1] + chalk[i])
        rem = k % prefix[-1]
        left = 0
        right = len(prefix) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if rem == prefix[mid]:
                return mid + 1
            
            elif rem < prefix[mid]:
                right = mid - 1
                
            else:
                left = mid + 1
        return left 