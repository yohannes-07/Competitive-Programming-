class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        short_string = min(strs,key=len)
        for i, char in enumerate(short_string):
            
            for word in strs:
                if word[i] != char:
                    
                    return short_string[:i]
                
        return short_string 