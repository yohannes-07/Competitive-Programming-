from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, v: int, adj: List[List[int]]) -> bool:
	    
		color = [0 for i in range(v)]
        
        def topSort(node, parent):
            
            if color[node] == 1:
                return False
            
            color[node] = 1
            for neighbor in adj[node]:
                if color[neighbor] == 2 or neighbor == parent:
                    continue
                
                if not topSort(neighbor, node):
                    return False
            
            color[node] = 2 
            
            return True
            

        for node in range(v ):
            if color[node] != 0:
                continue
            
            if not topSort(node, float("-inf")):
                return 1
                
        return 0
           
       
		


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends
