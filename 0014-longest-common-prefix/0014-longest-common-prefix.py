class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_common_prefix = ""
        min_len_word = min(strs)
        max_len_word = max(strs)
        
        
        for i in range(len(min_len_word)):
            if min_len_word[i] != max_len_word[i]:
                return longest_common_prefix
            
            longest_common_prefix += min_len_word[i]
            
            
        return longest_common_prefix