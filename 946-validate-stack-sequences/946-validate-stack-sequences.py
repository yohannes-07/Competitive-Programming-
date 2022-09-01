class Solution(object):
    def validateStackSequences(self, pushed, popped):
        stack = []
        j=0
	
        for  i in range(len(pushed)):			
            stack.append(pushed[i])
            while stack and stack[-1] == popped[j]:
		
                stack.pop()
                j += 1
        
        return True if len(stack) == 0 else False
		

			

		

			
        
        

        