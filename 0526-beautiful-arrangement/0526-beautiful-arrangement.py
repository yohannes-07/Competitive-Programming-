class Solution:
    def countArrangement(self, n: int) -> int:
        self.count = 0
        self.n = n
        
        def backtrack(idx, temp):
            if len(temp) == self.n:
                self.count += 1
                return

            for num in range(1, self.n + 1):
                if num not in temp and (num % idx == 0 or idx % num == 0):
                    
                    temp.append(num)
                    backtrack(idx+1, temp)
                    temp.pop()

        backtrack(1, [])
        return self.count