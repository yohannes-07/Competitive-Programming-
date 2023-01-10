class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1 = num1.split("+")
        num2 = num2.split("+")
        
        real = int(num1[0]) * int(num2[0])
        intemediate = int(num1[0]) * int(num2[1][:-1]) + int(num2[0]) * int(num1[1][:-1])
        
        imaginary = -1 * int(num1[1][:-1]) * int(num2[1][:-1])
        real = real + imaginary
        
        product = str(real) + "+" + str(intemediate) + "i"
        
        return product