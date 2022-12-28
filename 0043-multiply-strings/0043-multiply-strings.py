class Solution:
    def toNumber(self, string):
        num = 0
        for digit in string:
            
            # convert each  string digit to number digit
            # the diffrence between ord(digit) - ord("0") yields the amount of the digit in decimal number
            num = num * 10 + ord(digit) - ord("0")
            
        return num
            
    
    def multiply(self, num1: str, num2: str) -> str:
        
       #check if one of the nums is 0
        if num1 == "0" or num2 == "0":
            return "0"
        
        product = self.toNumber(num1) * self.toNumber(num2)
        
        #change it back to string => use built-in ord and chr functions
        res = ""
        while product:
            rem = product % 10
            
            product = product // 10
            res = chr(rem + ord("0")) + res
        
        return res
            
        
        
    
    