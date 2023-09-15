class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphaNumericString = ""
        
        for char in s:
            if char.isnumeric() or char.isalpha():
                alphaNumericString += char.lower()
                
        left, right = 0, len(alphaNumericString) - 1
        
        while left <= right:
            if alphaNumericString[left] != alphaNumericString[right]:
                return False
            
            left += 1
            right -= 1
            
        return True
        