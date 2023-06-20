class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # build graph using hash table for saving time
        graph = defaultdict(list)      # key is 'source', value is '(target, cost)'
        for edge in times:
            graph[edge[0]].append((edge[1], edge[2]))
        
        # Best-First-Search
        heap = [(0,k)]
        visited = set()
        
        res_cost = 0
        while heap:
            cost, node = heapq.heappop(heap)
            
            # add neighbors to heap
            if node not in visited:
                res_cost = cost     # only save the cost from node not visited
                visited.add(node)
                
                for target, edge_cost in graph[node]:    # get the edges of node
                    if target not in visited:  # ignore visited neighbor
                        heapq.heappush(heap, (cost+edge_cost, target))
                        
        
        if len(visited) < n:
            return -1
        else:
            return res_cost
