class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        str1 = str2 = ''
        i = j = 0
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                str1 += word1[i]
                
            if j < len(word2):
                str2 += word2[j]
                
            i += 1
            j += 1
        return str1 == str2