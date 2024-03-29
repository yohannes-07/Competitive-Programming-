class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        color = [0 for i in range(len(graph))]
        order = []
        
        # add a node to the order arr if you're not going to find a cyvle 
        # starting from that node
        def topSort(node):
            
            # make it fast(pruning)
            if color[node] == 2:
                return True
            
            if color[node] == 1:
                return False
            
            color[node] = 1
            for neighbor in graph[node]:
               
                if not topSort(neighbor):
                    return False
            
            color[node] = 2       
            return True
            

        for node in range(len(graph)):
 
            if topSort(node):
                order.append(node)
           
        order.sort()
        return order