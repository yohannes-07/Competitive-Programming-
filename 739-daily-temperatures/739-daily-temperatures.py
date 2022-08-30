class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        mono_stack = []
        
        i = 0
        while i < len(temperatures):
            while mono_stack and temperatures[i] > mono_stack[-1][0]:
                
                stackT, stackidx = mono_stack.pop()
                output[stackidx] = (i- stackidx)
                
            mono_stack.append([temperatures[i], i])
            i += 1
            
        return output 
            