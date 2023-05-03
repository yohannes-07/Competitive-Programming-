import sys
sys.setrecursionlimit(10000)
from collections import defaultdict
while True:
    graph = defaultdict(list)
    visited = set()


    n = int(input())
    if n == 0: break
    e = int(input())
    first = -1
    for _ in range(e):
        a, b = list(map(int, input().split()))
        graph[a].append(b)
        graph[b].append(a)
        if first == -1:
            first = a

    color = [0 for _ in range(n + 1)]
    def dfs(node):
        
        visited.add(node)
        
        
        for neighbor in graph[node]:
            if neighbor not in visited :
                visited.add(neighbor)
                
                color[neighbor] = -1 * color[node]
                
                if not dfs(neighbor): return False
                
            elif color[node] == color[neighbor]:
                return False
            
        return True
    color[first] = 1
    if not dfs(first): 
        print("NOT BICOLOURABLE.")
    else: 
        print("BICOLOURABLE.")
