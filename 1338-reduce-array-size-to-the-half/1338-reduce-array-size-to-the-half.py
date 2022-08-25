class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        vals = sorted(count.values(), reverse = True)
        n = len(arr)
        half_size ,output = n// 2, 0
        
        for i in vals:
            half_size -= i
            output += 1
            
            if half_size <= 0:
                return output
        return output