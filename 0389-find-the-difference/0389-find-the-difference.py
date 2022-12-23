class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if not s:
            return t
        dic = {}
        dic1 = {}
        
        for char in s:
            if char in dic:
                dic[char] += 1    
            else:
                dic[char] = 1
        
        for char in t:
            if char in dic1:
                dic1[char] += 1
                
            else:
                dic1[char] = 1 
        for key in dic1:
            if key in dic and dic1[key] > dic[key]:
                return key
            if key not in dic:
                return key
      