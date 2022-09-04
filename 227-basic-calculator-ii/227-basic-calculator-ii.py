class Solution(object):
    def calculate(self, s):
        if not s:
            return "0"
        else:
            stack, num, sign = [], 0, "+"

            for i in range(len(s)):

                if s[i].isdigit():
                    num = num*10+ord(s[i])-ord("0")

                if (not s[i].isdigit() and not s[i].isspace()) or i == len(s)-1:
                    if sign == "-":
                        stack.append(-num)

                    elif sign == "+":
                        stack.append(num)

                    elif sign == "*":
                        stack.append(stack.pop()*num)

                    else: 
                        tmp = stack.pop()
                        tmp = abs(tmp)//num if tmp >= 0 else -(abs(tmp)//num)
                        stack.append(tmp)

                    sign = s[i]
                    num = 0

            output = 0

            for j in range(len(stack)):
                 output += stack[j]

            return output 


