class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        original_number = x
        num = ""
        while x > 0:
            rem = x % 10
            num += str(rem)
            x = x // 10
        
        if int(num) == original_number:
            return True
        return False

            
