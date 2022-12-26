class Solution(object):
    def interpret(self, command):
        n = len(command)
        i = 0
        res = []
        
        while i < n:
            if command[i] == "G":
                res.append(command[i])
                i += 1
                
            elif command[i] == "(" and  command[i + 1] == ")":
                res.append("o")
                i += 2
            
            elif command[i] == "(" and  command[i + 1] == "a":
                res.append("al")
                i += 4
                
        return "".join(res)