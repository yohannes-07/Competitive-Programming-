class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        file_system = defaultdict(list)
        res = []
        
        for path in paths:
            path = path.split(" ")
            
            root = path[0]
            i = 1
            
            while i in range(len(path)):
                file_name, content = path[i].split("(")
                file_system[content[:len(content) - 1]].append(root + "/" + file_name)
                i += 1
                
        for file in file_system.values():
            if len(file) > 1:
                res.append(file)
                
        return res
            
                    
            