class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        myGraph = defaultdict(list)
        n = len(graph) - 1
        
        for i, neighbours in enumerate(graph):
            myGraph[i].extend(neighbours)
            
        def dfs(node, path):
            
            if node == n:
                res.append(path[:])
                return
            
            for neigbhour in myGraph[node]:
                
                dfs(neigbhour,path + [neigbhour])
        
        for node in myGraph[0]:
            dfs(node, [0, node])
            
            
        return res