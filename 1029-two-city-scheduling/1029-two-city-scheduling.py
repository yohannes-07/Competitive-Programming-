class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        temp = [(costs[i][0] - costs[i][1], i) for i in range(len(costs))]
        temp.sort()
        
        summ = 0
        cityA = 0
        
        for diff, idx in temp:
            if cityA < n//2:
                summ += costs[idx][0]
                
            else:
                summ += costs[idx][1]
                
            cityA += 1
                
        return summ