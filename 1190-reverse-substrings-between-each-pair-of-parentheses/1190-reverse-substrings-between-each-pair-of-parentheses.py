class Solution(object):
    def reverseParentheses(self, s):
        stackA = []
        stackB = []
        for i in s:

            if i == ")":
	
                while stackA and stackA[-1] != "(":
                    stackB.append(stackA.pop())
                    
                    
                stackA.pop()
                for char in stackB:
                    stackA.append(char)

                stackB = []
			
            else:
                stackA.append(i)

        return "".join(stackA)
        

        