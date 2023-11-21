class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        res = ''
        for cand in d:
            if self.check(s, cand) and (len(cand) > len(res) or (len(cand) == len(res) and cand < res)):
                res = cand
        return res
            
    def check(self, s, cand):
        i, j = 0, 0
        while i < len(s) and j < len(cand):
            if s[i] == cand[j]:
                i += 1
                j += 1
                continue
            i += 1
        return j == len(cand)