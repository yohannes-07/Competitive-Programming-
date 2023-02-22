class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return
        
        left, res = 0, []
        pcount = Counter(p)
        scount = defaultdict(int)
        
        for i in range(len(p)):
            scount[s[i]] += 1
        
        if scount == pcount:
            res.append(0)
       
        
        for i in range(len(p), len(s)):
            scount[s[i]] += 1
            scount[s[left]] -= 1
            
            if scount[s[left]] == 0:
                scount.pop(s[left])
                
            left += 1
            if scount == pcount:
                res.append(left)
                
        return res