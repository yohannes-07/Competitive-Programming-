class Solution(object):
    def maxVowels(self, s, k):
        ctr = res = i = 0
        vowels= "aeiou"
        
        while i < len(s):
            
            if s[i] in vowels:
                ctr += 1
                
            if i >= k:  
                if s[i - k] in vowels:
                    ctr -= 1
               
            res = max(res, ctr)
            i += 1
            
        return  res   