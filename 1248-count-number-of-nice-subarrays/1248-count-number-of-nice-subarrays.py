class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        cumuSum = defaultdict(int)
        cumuSum[0] = 1
        arr= []
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                arr.append(1)
            else:
                arr.append(0)
                
        ans = prefix_odd = 0
        for i in range(len(nums)):
            
            if arr[i] == 1:
                prefix_odd += 1
                
            if prefix_odd - k in cumuSum:
                ans += cumuSum[prefix_odd - k]
                
            cumuSum[prefix_odd] += 1  
                
                
                
            
            
        return ans