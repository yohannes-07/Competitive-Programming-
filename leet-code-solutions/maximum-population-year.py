class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        prefix = [0] * 101
        
        for birth, death in logs:
            prefix[birth - 1950] += 1
            prefix[death - 1950] -= 1
            
        for i in range(1, len(prefix)):
            prefix[i] += prefix[i-1]
            
        year = None
        max_pop = float("-inf")
        
        for i in range(len(prefix)):
            if prefix[i] > max_pop:
                max_pop = prefix[i]
                year = i + 1950
                
        return year
        