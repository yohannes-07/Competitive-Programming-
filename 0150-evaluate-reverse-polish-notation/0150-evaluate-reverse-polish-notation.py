class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for char in tokens:
            if char in "+-*/":
                operand2 = stack.pop()
                operand1 = stack.pop()
                
                if char == "+":
                    res = int(operand1) + int(operand2)
                    stack.append(res)
                
                elif char == "-":
                    res = int(operand1) - int(operand2)
                    stack.append(res)
                
                elif char == "*":
                    res = int(operand1) * int(operand2)
                    stack.append(res)
                    
                else:
                    res = int(operand1) * 1.0 / int(operand2)
                    stack.append(res)
                    
            else:
                stack.append(char)
                
        return int(stack[0])
                
                
                