class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        
        m = min(len(nums1), k)
        n = min(len(nums2), k)
        
        for i in range(m):
            for j in range(n):
                currSum = nums1[i] + nums2[j]
                
                if len(heap) < k:
                    heappush(heap, (-currSum, [nums1[i], nums2[j]]))
                    
                elif currSum < -heap[0][0]:
                    heappop(heap)
                    heappush(heap, (-currSum, [nums1[i], nums2[j]]))
                    
                else:
                    break
                    
        return [pair[1] for pair in heap]