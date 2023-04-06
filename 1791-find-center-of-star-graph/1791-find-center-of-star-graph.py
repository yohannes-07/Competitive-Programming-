class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges)
        freq = [0] * (n + 1)
        
        for u, v in edges:
            
       
            freq[u - 1] += 1
            freq[v - 1] += 1
            
        max_ = max(freq)
        
        return freq.index(max_) + 1
            