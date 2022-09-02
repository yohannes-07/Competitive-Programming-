sign= "+"
i = 0
while i < len(s):
​
if s[i].isdigit():
​
num=num*10+int(s[i])
​
operators = '+-*/'
​
if s[i] in operators or i==len(s)-1:
​
if sign=='+':
​
stack.append(num)
​
elif sign=='-':
​
stack.append(-num)
​
elif sign=='*':
​
stack.append(stack.pop()*num)
​
elif sign=='/':
​
stack.append(int(stack.pop()/num))
​
num=0
​
sign = s[i]
i += 1
output = 0
for j in range(len(stack)):
output += stack[j]
return output
​
1.         ``