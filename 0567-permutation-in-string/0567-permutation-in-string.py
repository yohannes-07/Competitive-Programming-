class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)  < len(s1):
            return False
        
        left = 0
        
        s1count = Counter(s1)
        s2count = defaultdict(int)
        
        for i in range(len(s1)):
            s2count[s2[i]] += 1
        
        if s1count == s2count:
            return True
       
        for i in range(len(s1), len(s2)):
            s2count[s2[i]] += 1
            s2count[s2[left]] -= 1
            
            if s2count[s2[left]] == 0:
                s2count.pop(s2[left])    
            left += 1
            
            if s1count == s2count:
                return True
                
        return False