class Solution:
    def average(self, salaries: List[int]) -> float:
        min_value = float("inf")
        max_value = float("-inf")
        n = len(salaries)
        
        for salary in salaries:
            min_value = min(min_value, salary)
            max_value = max(max_value, salary)
            
        print(min_value, max_value)
        
        summ = 0
        for salary in salaries:
            if salary == min_value or salary == max_value:
                continue
            else:
                summ += salary
        
        return summ/(n-2)