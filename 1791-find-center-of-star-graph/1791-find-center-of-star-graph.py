class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges)
        freq = defaultdict(int)
        
        for u, v in edges:
            
            if u in freq:
                return u
            
            if v in freq:
                return v
       
            freq[u ] += 1
            freq[v ] += 1
            
            
            
        