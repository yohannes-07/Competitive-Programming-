class Solution:
    MIN_INT = - (2 ** 31)
    MAX_INT = 2 ** 31
    
    def reverse(self, x: int) -> int:
        if x == 0 : return 0
        a = False
        if x < 0:
            a = True
    
        x = str(x)
        x = list(x[::-1])
        
        for char in x:
            if char == '-':
                x.remove(char)
        
        ans = ""
        
        for char in x:
            ans += char
        
        ans = int(ans)  
        if a: ans *= -1
        
        if ans not in range(self.MIN_INT, self.MAX_INT) : return 0
        else : return int(ans)