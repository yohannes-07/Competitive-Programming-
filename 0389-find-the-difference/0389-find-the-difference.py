class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if not s:
            return t
        
        # we use two dictionaries and store each strings' char as key and thier frequency 
        # as vlaue like {"a": 1, "b": 3}
        
        dic1 = {} # for string s
        dic2 = {} # for string t
        
        for char in s:
            if char in dic1:
                dic1[char] += 1    
            else:
                dic1[char] = 1
        
        for char in t:
            if char in dic2:
                dic2[char] += 1
                
            else:
                dic2[char] = 1 
        
        # check if one of the keys in dic2 is not in dic1
        # or if the key frequency in dic2 is greater than in dic1
        
        for key in dic2:
            if key in dic1 and dic2[key] > dic1[key]:
                return key
            if key not in dic1:
                return key
      