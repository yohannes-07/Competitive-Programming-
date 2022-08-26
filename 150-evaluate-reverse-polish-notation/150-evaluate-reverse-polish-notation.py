class Solution(object):
    def evalRPN(self, tokens):
        stack=[]
        operators=["+","-","*","/"]
        
        for char in tokens:
            if char in operators:
                if char == "+":
                    last=stack.pop()
                    first= stack.pop()
                    res = first + last
                    stack.append(res)
                    
                    
                elif char == "-":

                    last = stack.pop()

                    first = stack.pop()
                    res = first - last

                    stack.append(res)
                    
                elif char == "*":
                    last = stack.pop()
                    first = stack.pop()
                    res = first * last
                    stack.append(res)
                    
                elif char == "/":
                    last = stack.pop()
                    first = stack.pop()
                    res = (first * 1.0 / last)
                    stack.append(int(res))
            else:
                stack.append(int(char))
     
        return stack[0]
        