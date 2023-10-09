class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1Counter = Counter(s1)
        s2Counter = defaultdict(int)
        
        left = 0
        
        for i in range(len(s2)):
            s2Counter[s2[i]] += 1
            
            if i - left + 1 == len(s1):
                if s2Counter == s1Counter:
                    return True
                
                s2Counter[s2[left]] -= 1
                if s2Counter[s2[left]] == 0:
                    s2Counter.pop(s2[left])
                    
                left += 1
                
            
        return False
                