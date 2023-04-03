class Solution:
    def minSteps(self, n: int) -> int:
        count = 0
        i = 2
        while n != 1:
            if n%i == 0:
                n //= i
                count += i
                i = 2
            else:
                i += 1
        return count