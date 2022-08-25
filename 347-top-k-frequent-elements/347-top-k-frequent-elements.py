class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        keys = list(count.keys())
        vals = list(count.values())
        vals1 = sorted(count.values(), reverse = True)
        
        output = []
        i = 0
        elements = []
        
        while k > 0:
            elem = vals1[i] 
            pos = vals.index(elem)
            
            output.append(keys[pos])
            keys[pos] = None
            vals[pos] = None
            i += 1
            k -= 1
        return output