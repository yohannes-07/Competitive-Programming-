class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s = list(s)
        n = len(s)
        nums = [0] * n
        
        for shift in shifts:
            if shift[2]:
                nums[shift[0]] += 1
                
                if shift[1] + 1 < n:
                    nums[shift[1] + 1] -= 1
                      
            else:
                
                nums[shift[0]] -= 1
                
                if shift[1] + 1 < n:
                    nums[shift[1] + 1] += 1
                    
        for i in range(1, n):
            nums[i] += nums[i-1]
            
        for i in range(n):
            s[i] = chr((((ord(s[i]) + nums[i]) - 97) % 26) + 97)
            
        return "".join(s)
                    
                
