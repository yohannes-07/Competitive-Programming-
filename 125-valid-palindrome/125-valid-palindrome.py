class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ''
        for c in s:
            if c.isnumeric() or c.isalpha():
                st += c.lower()
            
        print(st)    
        left = 0
        for i in range(len(st)-1, -1, -1):
            if st[left] != st[i]:
                return False
            left += 1
        return True