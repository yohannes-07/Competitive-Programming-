class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return
        pcount = Counter(p)
        scount = {}
        for i in range(len(p)):
            scount[s[i]] = 1 + scount.get(s[i], 0)
        
        res = [0] if scount == pcount else []
        left = 0
        for j in range(len(p), len(s)):
            scount[s[j]] = 1 + scount.get(s[j], 0)
            scount[s[left]] -= 1
            
            if scount[s[left]] == 0:
                scount.pop(s[left])
            left += 1
            if scount == pcount:
                res.append(left)
        return res