#User function Template for python3
from collections import defaultdict, deque
class Solution:
    def findOrder(self,alien_dict, N, K):
        
        order = []
        graph = defaultdict(list)
        
        for i in range(N-1):
            
            curr=alien_dict[i]
            nxt=alien_dict[i+1]
            
            for j in range(min(len(curr), len(nxt))):
                if curr[j] != nxt[j]:
                    
                    graph[ord(curr[j]) - ord("a")].append(ord(nxt[j]) - ord("a"))
                    break
  
        incoming = defaultdict(int)
        queue = deque()
        
        for node in graph:
            
            for neigh in graph[node]:
                incoming[neigh] += 1
          
        for node in range(k):
            if incoming[node] == 0:
                queue.append(node)
  
        while queue:
            curr = queue.popleft()
            order.append(curr)
            
            for neighbor in graph[curr]:
                 incoming[neighbor] -= 1
                   
                 if incoming[neighbor] == 0:
                    queue.append(neighbor)

        for i, num in enumerate(order):
            order[i] = chr(num + ord("a"))
            
        return order

                
        
            
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends
