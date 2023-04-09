"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        importance = defaultdict(int)
        subordinates = defaultdict(list)
        
        for employee in employees:
            importance[employee.id] = employee.importance
            subordinates[employee.id] = employee.subordinates
        
        def dfs(id):
            res = importance[id]
            
            for subordinate in subordinates[id]:
                res += dfs(subordinate)
                
            return res
            
        return dfs(id)
            