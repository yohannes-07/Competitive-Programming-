class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = [[position[i], speed[i]] for i in range(len(speed))]
        
        stack = []
        position_speed.sort()
      
        for pos, s in position_speed[::-1]:
            
            time_to_reach_target = (target - pos)/s
            stack.append(time_to_reach_target)
           
            if len(stack) >= 2 and stack[-1]  <= stack[-2]:
                stack.pop()
             
        return len(stack)