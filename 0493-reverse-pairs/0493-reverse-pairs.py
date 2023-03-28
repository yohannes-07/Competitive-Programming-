class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ans = 0
    
        def mergeSort(left, right):
            if left == right:
                return [nums[left]]
            
            mid = left + (right - left)//2

            left_half = mergeSort(left, mid)
            right_half = mergeSort(mid + 1,right)
            
            numberOfPairs(left_half, right_half)
            return merge(left_half, right_half)
        
        def numberOfPairs(left_half, right_half):
            nonlocal ans
            
            p1, p2 = 0, 0    
            while p2 < len(right_half):
                while p1 < len(left_half) and left_half[p1] <= right_half[p2] * 2  :
                    p1 += 1
                
                ans += len(left_half) - p1
                p2 += 1
                if p1 > len(left_half):
                    break
                
        
        def merge(left_half, right_half):
            
            res = []
            l = r = 0
          
            while l < len(left_half) and r < len(right_half):
                
                if left_half[l] <= right_half[r]:
                    res.append(left_half[l])
                    l += 1

                else:
                    res.append(right_half[r])
                    r += 1


            while l < len(left_half):
                res.append(left_half[l])
                l += 1
                 
            while r < len(right_half):
                res.append(right_half[r])
                r += 1
            
            return res
            
        mergeSort(0, len(nums) -1)
        return ans