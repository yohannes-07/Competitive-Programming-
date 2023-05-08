class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        graph = defaultdict(list)
        incoming = defaultdict(int)
        
        queue = deque(supplies)
        order = []
        temp = set(recipes)
        for i in range(len(recipes)):
            for pre in ingredients[i]:
                graph[pre].append(recipes[i])
      
                incoming[recipes[i]] += 1
  
        
        while queue:
            food = queue.popleft()
            if food in temp:
                order.append(food)
            
            for neighbor in graph[food]:
                 incoming[neighbor] -= 1
                   
                 if incoming[neighbor] == 0:
                    queue.append(neighbor)

   
        return order

            
 