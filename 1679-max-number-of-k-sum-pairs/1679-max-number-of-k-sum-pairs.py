class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        counter = Counter(nums)
        output = 0
        
        for num in counter:
            diff = k - num
            if diff in counter and counter[diff] > 0:
                res = 0
                
                if num == k // 2:
                    res = counter[num] // 2
                else:
                    res = min(counter[num], counter[diff])

                    
                output += res
                
                counter[diff] = counter[diff] - res
                counter[num] = counter[num] - res

        return output