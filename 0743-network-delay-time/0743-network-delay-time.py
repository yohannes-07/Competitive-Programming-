class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [None] * (n+1)
        
        for u, v, w in times:
            if graph[u]:
                graph[u].append((v, w))
                
            else:
                graph[u] = [(v, w)]
            
        distances = {node:float("inf") for node in range(1, n + 1)}
        distances[k] = 0
        visited = set()
        
        heap = [(0, k)]

        while heap:
            curr_dist, curr_node = heapq.heappop(heap)
            
            if curr_node in visited:
                continue
                
            visited.add(curr_node)
            
            if graph[curr_node]:
                for neigh, weight in graph[curr_node]:
                    distance  = curr_dist + weight

                    if distance < distances[neigh]:
                        distances[neigh] = distance
                        heapq.heappush(heap, (distance, neigh))
                        
        minimum_time =  max(distances.values())
        
        if minimum_time == float("inf"):
            return -1
        return minimum_time