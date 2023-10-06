class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        
        graph = defaultdict(list)
        
        for i, (a, b) in enumerate(edges):
            graph[a].append([b, succProb[i]])
            graph[b].append([a, succProb[i]])
               
        probabilities = {i: float("inf") for i in range(n)}
        probabilities[start] = 1
        visited = set()
        
        heap = [(-1, start)]
        
        while heap:
            curr_prob, curr = heappop(heap)
            
            if (curr, curr_prob) in visited:
                continue
                
            visited.add((curr, curr_prob))
            
            for neigh, probability in graph[curr]:
                totalProb = curr_prob * probability
                
                if totalProb < probabilities[neigh]:
                    probabilities[neigh] = totalProb
                    heappush(heap, (totalProb, neigh))
        
        if probabilities[end] == float("inf"):
            return 0
        
        return -probabilities[end]
            
        