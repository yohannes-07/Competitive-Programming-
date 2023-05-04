class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words) 
        heap = []
        
        for key, value in freq.items():
            heapq.heappush(heap, (-value, key))
        
        heapq.heapify(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res
        
