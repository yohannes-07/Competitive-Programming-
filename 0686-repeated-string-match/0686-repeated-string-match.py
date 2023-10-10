class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        
        def  checker(needle, haystack):
            m, n = len(needle), len(haystack)
            prevLPS, i = 0, 1
            LPS = [0] * m

            while i < m:
                if needle[prevLPS] == needle[i]:
                    LPS[i] = prevLPS + 1
                    prevLPS += 1
                    i += 1

                elif prevLPS == 0:
                    i += 1

                else:
                    prevLPS = LPS[prevLPS - 1]

            i, j = 0, 0

            while i < n:
                if needle[j] == haystack[i]:
                    j += 1
                    i += 1

                elif j == 0:
                    i += 1

                else:
                    j = LPS[j - 1]

                if j == len(needle):
                    return i - j

            return -1
        
        times = (len(b) - 1) // len(a) + 1  
        
        for i in range(0, 2):
            if checker(b, a * (times + i)) != -1:
                return times + i
            
        return -1
        