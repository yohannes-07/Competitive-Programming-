class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        position = [0,0]
        direction = "North"
        
        for instruction in instructions:
            
            if direction == "North":
                if instruction == "G":
                    position[1] += 1
                    
                elif instruction == "L":
                    direction = "West"
                else:
                    direction = "East"
                
                
            elif direction == "South":
                if instruction == "G":
                    position[1] -= 1
                    
                elif instruction == "L":
                    direction = "East"
                else:
                    direction = "West"
                

            elif direction == "East":
                if instruction == "G":
                    position[0] += 1
                    
                elif instruction == "L":
                    direction = "North"
                else:
                    direction = "South"
                

            else:
                if instruction == "G":
                    position[0] -= 1
                    
                elif instruction == "L":
                    direction = "South"
                else:
                    direction = "North"
                    
        if position == [0,0] or direction != "North":
            return True
        
        return False
                

                
                