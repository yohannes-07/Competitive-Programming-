class Solution(object):
    def findTheWinner(self, n, k):
        if  n == 1:
            return 1
        
        recursive_value= self.findTheWinner(n-1, k)
        ans = (recursive_value + k) % n

        if ans == 0:
            return n
        return ans
        