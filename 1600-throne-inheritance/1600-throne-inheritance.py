class ThroneInheritance:

    def __init__(self, kingName: str):
        
        self.king = kingName
        self.inheritance = defaultdict(list)
        
        self.dead = {}
        
    def birth(self, parentName: str, childName: str) -> None:
        self.inheritance[parentName].append(childName)

    def death(self, name: str) -> None:
       
        self.dead[name] = "dead"
      
                      
    def getInheritanceOrder(self) -> List[str]:
        order = []
        
        def dfs(curr):
            if curr not in self.dead: order.append(curr)
            
            for neighbour in self.inheritance[curr]:
                    dfs(neighbour)
                
        dfs(self.king)
        
        return order
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()