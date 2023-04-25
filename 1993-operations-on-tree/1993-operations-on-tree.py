class LockingTree:

    def __init__(self, parent: List[int]):
        
        self.parent = parent
        self.locked = {}
        
        self.graph = defaultdict(list)
        for i, v in enumerate(parent):
            self.graph[v].append(i)
 

    def lock(self, num: int, user: int) -> bool:
        if num in self.locked:
            return False
        
        self.locked[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if num not in self.locked or self.locked[num] != user:
            return False
        
        self.locked.pop(num)
        return True
        
    def upgrade(self, num: int, user: int) -> bool:
        if num in self.locked:
            return False
        
        def checkAncestors(num):
            if num in self.locked:
                return True
            
            elif num == -1:
                return False
            
            
            return checkAncestors(self.parent[num])
        
        def descendants(num):
            for node in self.graph[num]:
                if node in self.locked:
                    return True
                
                if descendants(node):
                    return True
                
            return False
                
        def unlockDescendants(num):
            for node in self.graph[num]:
                if node in self.locked:
                    
                    self.locked.pop(node)
                    
                unlockDescendants(node)
                
                
            
       
        
        if checkAncestors(self.parent[num]):
            return False
        
        if not descendants(num):
            return False
        
        
        unlockDescendants(num)
        
        self.locked[num] = user
        
        return True