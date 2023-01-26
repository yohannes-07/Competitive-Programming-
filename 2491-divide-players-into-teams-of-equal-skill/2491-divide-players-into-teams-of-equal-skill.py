class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        left = 0
        right = len(skill) - 1
        chemistries = set()
        res = 0
        
        while left < right:
            chemistry = skill[left] + skill[right]
            chemistries.add(chemistry)
            res +=   skill[left] * skill[right]
          
            left += 1
            right -= 1
        
      
        if len(chemistries) == 1:
            return  res
        
        return -1