class Solution:
    def romanToInt(self, s: str) -> int:
        res, prev = 0, 0
        dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        for i in s[::-1]:          # rev the s
            if dict[i] >= prev:
                res += dict[i]     # sum the value iff previous value same or more
            else:
                res -= dict[i]     # substract when value is like "IV" --> 5-1, "IX" --> 10 -1 etc 
            prev = dict[i]
        return res