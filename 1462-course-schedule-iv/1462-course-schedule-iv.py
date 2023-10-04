class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
#         Topological Sort
         
#         graph = defaultdict(list)
#         incoming = defaultdict(int)
#         precourses = defaultdict(set)
        
#         for pre, course in prerequisites:
#             graph[pre].append(course)
#             precourses[course].add(pre)
#             incoming[course] += 1
        
#         queue = deque()
#         for node in range(n):
#             if incoming[node] == 0:
#                 queue.append(node)
                
#         while queue:
#             pre = queue.popleft()
            
#             for course in graph[pre]:
#                 precourses[course] |= precourses[pre]
                
#                 incoming[course] -= 1
                
#                 if incoming[course] == 0:
#                     queue.append(course)
            
#         ans = []
#         for pre, course in queries:
#             ans.append(pre in precourses[course])
        
#         return ans
        
#         Floyed Marshall

        isPrerequisite = [[False] * numCourses for _ in range(numCourses)]
        
        for pre, course in prerequisites:
            isPrerequisite[pre][course] = True
            
            
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    
                    if not isPrerequisite[i][j]  and (isPrerequisite[i][k] and isPrerequisite[k][j]):
                        isPrerequisite[i][j] = True
                        
                        
        res = []
        
        for pre, course in queries:
            res.append(isPrerequisite[pre][course])
            
        return res
    
    
    
    
    
    
        